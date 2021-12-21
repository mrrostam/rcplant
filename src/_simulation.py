from ._enums import SimulationMode
from ._recycling_plant import *

DEFAULT_TIME_STEP_SEC = 0.1


class RPSimulation:
    def __init__(
            self,
            sorting_function,
            final_time_min: int,
            sensors: Sensor = None,
            conveyor: Conveyor = None,
            mode='training'
    ):
        if not any(mode == simulation_mode.value for simulation_mode in SimulationMode):
            raise ValueError(f'Invalid simulation mode,\n'
                             f'valid options: {[mode.value for mode in SimulationMode]}')

        self._time_step_sec = DEFAULT_TIME_STEP_SEC
        self._final_time_sec = final_time_min * 60
        self._recycling_plant = RecyclingPlant(sorting_function, conveyor, sensors, mode)
        self._total_missed = 0
        self._total_classified = 0
        self._total_mistyped = 0

    @property
    def total_missed(self):
        return self._total_missed

    @property
    def total_classified(self):
        return self._total_classified

    @property
    def total_mistyped(self):
        return self._total_mistyped

    def update(self, generate_container=True):
        missed, classified, mistyped = self._recycling_plant.update(self._time_step_sec, generate_container)
        self._total_missed += missed
        self._total_classified += classified
        self._total_mistyped += mistyped

    def run(self):
        for time in range(0, int(self._final_time_sec // self._time_step_sec)):
            self.update()
        for time in range(0, int(self._final_time_sec // self._time_step_sec)):
            self.update(False)
