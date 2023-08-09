import time
from typing import Optional
from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(f'cooptools.timers')

class Decay(ABC):
    def __init__(self, init_value: float = 1):
        self.init_value = init_value

    @abstractmethod
    def val_at_t(self, t_ms: int):
        pass

    def progress_at_time(self, t_ms: int):
        return min((self.init_value - self.val_at_t(t_ms) )/ (self.init_value), 1)



class UniformDecay(Decay):

    def __init__(self, ms_to_zero: int, init_value: float = 1):
        self.ms_to_zero_start = ms_to_zero
        self._r = 1 / self.ms_to_zero_start

        super().__init__(init_value)

    def val_at_t(self, t_ms: int):
        return max((1 - self._r * t_ms), 0) * self.init_value



class TimedDecay:
    def __init__(self,
                 time_ms: int,
                 init_value: float = None,
                 start_perf: float = None):
        self.time_ms = time_ms
        self.start_perf = None
        self.decay_function = UniformDecay(ms_to_zero=time_ms, init_value=init_value)

        if start_perf is not None:
            self.set_start(start_perf)

    def set_start(self, at_time):
        self.start_perf = at_time

    def check(self, at_time) -> Optional[float]:
        if self.start_perf is None:
            return None
        t = at_time - self.start_perf

        return self.decay_function.val_at_t(at_time)

    @property
    def EndTime(self):
        if not self.start_perf:
            return None

        return self.start_perf + self.time_ms / 1000

    def progress_at_time(self, at_time):
        if not self.start_perf:
            return None

        return min((at_time - self.start_perf) / (self.EndTime - self.start_perf), 1)

    def progress_val(self, at_time):
        if not self.start_perf:
            return None

        return self.decay_function.progress_at_time(at_time)

    def time_until_zero_ms(self, at_time):
        return self.time_ms * (1 - self.progress_at_time(at_time))

from cooptools.asyncable import Asyncable
import uuid
class Timer:
    def __init__(self,
                 time_ms: int,
                 id: str = None,
                 start_on_init: bool = False,
                 as_async: bool = False,
                 reset_on_end: bool = False,
                 ):
        self._id = id if id else str(uuid.uuid4())
        self._time_ms = time_ms
        self._decayer: Optional[TimedDecay] = None
        self._start_thread_on_init = start_on_init
        self._started = start_on_init
        self._asyncable = Asyncable(
            loop_callback=self.update,
            start_on_init=True,
            as_async=as_async
        )
        self._accumulated_ms = 0
        self._last_update = None
        self._reset_on_end = reset_on_end

    def start(self):
        self._started = True

    def stop(self):
        self._started = False

    def reset(self):
        logger.info(f"Resetting timer {self._id} to {self.TimeMs}ms...")
        self._accumulated_ms = 0

    @property
    def TimeMs(self) -> int:
        return self._time_ms

    @property
    def AccummulatedMs(self) -> int:
        return self._accumulated_ms

    @property
    def MsRemaining(self) -> int:
        return max(0, self._time_ms - self.AccummulatedMs)

    def update(self, delta_ms: int = None):
        if not self._started:
            return

        now = time.perf_counter() * 1000
        if delta_ms is None:
            delta_ms = now - self._last_update if self._last_update is not None else 0

        self._accumulated_ms += delta_ms
        logger.debug(f"timer {self._id} update() ran at {now}")
        logger.info(f"timer {self._id} has {int(self.MsRemaining)}ms remaining")
        self._last_update = now

        if self.MsRemaining == 0:
            self._handle_ended()

    def _handle_ended(self):
        logger.info(f"Timer {self._id} ended at {self._last_update}.")

        if self._reset_on_end:
            self.reset()
        else:
            self.stop()

if __name__ == "__main__":
    start = time.perf_counter()

    timer = Timer(3000, start_on_init=True, as_async=True, reset_on_end=True)
    logging.basicConfig(level=logging.INFO)

    time.sleep(10)



    #
    # has_reset = False
    # while True:
    #     print(timer.finished)
    #     time.sleep(.5)
    #     if time.perf_counter() - start > 10 and not has_reset:
    #         timer.reset()
    #         has_reset = True
    #         print("reset")
    #
