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

        self._sorting_function = sorting_function
        self._num_containers = num_containers
        self._conveyor = conveyor
        self._sensors = sensors
        self._mode = mode

        self._recycling_plant = None

        self._total_missed = 0
        self._total_classified = 0
        self._total_mistyped = 0
        self._current_iteration = 0
        self._identification_result = {}

        self._init_recycling_plant()
        # to start from 1 for the next simulation
        Sensor.reset_num()

    def _init_recycling_plant(self):
        self._recycling_plant = RecyclingPlant(
            self._sorting_function,
            self._num_containers,
            self._conveyor,
            self._sensors,
            self._mode)

    @property
    def total_missed(self):
        return self._total_missed

    @property
    def total_classified(self):
        return self._total_classified

    @property
    def total_mistyped(self):
        return self._total_mistyped

    @property
    def identification_result(self):
        return self._identification_result

    def reset(self):
        self._init_recycling_plant()

        self._total_missed = 0
        self._total_classified = 0
        self._total_mistyped = 0
        self._current_iteration = 0
        self._identification_result = {}

    def _update(self):
        missed, classified, mistyped, identification_result, is_done = self._recycling_plant.update(
            self._current_iteration,
            self._simulation_frequency_hz,
            self._sensors_frequency_hz
        )
        self._current_iteration += 1
        self._total_missed += missed
        self._total_classified += classified
        self._total_mistyped += mistyped
        self._identification_result.update(identification_result)

        return is_done

    def run(self):
        self.reset()
        while not self._update():
            pass
        return self._current_iteration * (1 / self._simulation_frequency_hz)
