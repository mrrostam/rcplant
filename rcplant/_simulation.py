from ._constants import *
from ._recycling_plant import *
from ._types import SimulationMode


class RPSimulation:
    def __init__(
            self,
            sorting_function,
            num_containers: int,
            sensors: List[Sensor],
            sampling_frequency: int,
            conveyor: Conveyor,
            mode
    ):
        if not any(mode == simulation_mode.value for simulation_mode in SimulationMode):
            raise ValueError(f'Invalid simulation mode,\n'
                             f'valid options: {[mode.value for mode in SimulationMode]}')

        if sampling_frequency not in VALID_SENSORS_FREQUENCIES_HZ:
            raise ValueError(f'Invalid sampling frequency,\n'
                             f'valid options: {[frequency for frequency in VALID_FREQUENCIES]}')

        self._simulation_frequency_hz = SIMULATION_FREQUENCY_HZ
        self._sensors_frequency_hz = sampling_frequency
        self._current_iteration = 0
        self._recycling_plant = RecyclingPlant(
            sorting_function,
            num_containers,
            conveyor,
            sensors,
            mode)
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

    def update(self):
        missed, classified, mistyped, is_done = self._recycling_plant.update(
            self._current_iteration,
            self._simulation_frequency_hz,
            self._sensors_frequency_hz
        )
        self._current_iteration += 1
        self._total_missed += missed
        self._total_classified += classified
        self._total_mistyped += mistyped
        return is_done

    def run(self):
        while not self.update():
            pass
        return self._current_iteration * (1 / self._simulation_frequency_hz)
