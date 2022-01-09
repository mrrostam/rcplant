# upper and lower bound in cm
MIN_CONTAINER_SIZE = 5
MAX_CONTAINER_SIZE = 15

# init location in cm
INIT_CONTAINER_X = 0
INIT_CONTAINER_Y = 0
INIT_CONTAINER_Z = 0

# min gap between generated containers in cm
MIN_CONTAINERS_GAP = 5

SIMULATION_FREQUENCY_HZ = 10
VALID_SENSORS_FREQUENCIES_HZ = [10, 5, 2, 1]  # divisor of the simulation freq

SAMPLING_FREQUENCY_TO_SNR_DB = {freq: 50 // freq for freq in VALID_SENSORS_FREQUENCIES_HZ}

NOISE_MU_VALUE = 0
EPSILON_POWER = 0.0001
