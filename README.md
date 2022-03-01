# McMaster Recycling Plant Simulator Package


## Quick start

The following code is an example of how to use this package:

```python
import random

from rcplant import *


def user_sorting_function(sensors_output):
    # random identification
    decision = {sensor_id: random.choice(list(Plastic)) for (sensor_id, value) in sensors_output.items()}

    return decision


def main():

    # simulation parameters
    conveyor_length = 1000  # cm
    conveyor_width = 100  # cm
    conveyor_speed = 10  # cm per second
    num_containers = 100
    sensing_zone_location_1 = 500  # cm
    sensors_sampling_frequency = 1  # Hz
    simulation_mode = 'training'

    sensors = [
        Sensor.create(SpectrumType.FTIR, sensing_zone_location_1),
    ]

    conveyor = Conveyor.create(conveyor_speed, conveyor_length, conveyor_width)

    simulator = RPSimulation(
        sorting_function=user_sorting_function,
        num_containers=num_containers,
        sensors=sensors,
        sampling_frequency=sensors_sampling_frequency,
        conveyor=conveyor,
        mode=simulation_mode
    )

    elapsed_time = simulator.run()

    print(f'\nResults for running the simulation in "{simulation_mode}" mode:')

    for item_id, result in simulator.identification_result.items():
        print(result)

    print(f'Total missed containers = {simulator.total_missed}')
    print(f'Total sorted containers = {simulator.total_classified}')
    print(f'Total mistyped containers = {simulator.total_mistyped}')

    print(f'\n{num_containers} containers are processed in {elapsed_time:.2f} seconds')


if __name__ == '__main__':
    main()

```

You may modify the [`user_sorting_function`](src/main.py) function and implement new logic for sorting plastic containers.

## API

---

#### `RPSimulation`

```python
class RPSimulation:
    def __init__(
            self,
            sorting_function,
            num_containers: int,
            sensors: List[Sensor],
            sampling_frequency: int,
            conveyor: Conveyor,
            mode: str
    )
```

A manager class for the recycling plant simulator.

##### Input parameters:

- [sorting_function](#sorting_function) : A user-defined function that gets the [output of the sensors](#) and identifies the type of [plastic](#plastic), based on the given spectrum.
- num_containers : Number of input containers needed to be sorted.
- sensors : An array of [sensors](#sensor).
- sampling_frequency: The sampling frequency of sensors. Acceptable values: 10, 5, 2, and 1 Hz. In `testing` mode, increasing the sampling frequency increases added noise to spectrum.
- conveyor : A user-defined [conveyor](#conveyor) system.
- mode: A selector to run the simulation in either `training` or `testing` configuration.
---

#### RPSimulation.`run`

```python
def run(self)
```

A function to run the simulation.

##### Outputs:
- RPSimulation.`total_missed` : Number of missed containers.
- RPSimulation.`classified` : Number of classified containers.
- RPSimulation.`mistyped` : Number of containers classified incorrectly.

##### Returns:
- Amount of time required to process all containers [seconds].

---

#### Sensor

```python
class Sensor:
    def __init__(self, sensor_type: SpectrumType, location_cm: int, sensor_id: int = None)
```

A class to define a new sensor.

##### Input parameters:

- location_cm : Location of the sensor [centimeter].
- sensor_type : Type of the sensor [[SpectrumType](#spectrumtype)].
- sensor_id : Sensor ID, which is used in [sorting_function](#sorting_function) to identify each sensor. 
If no ID is provided, an ID will be generated based on the number of sensors.
---

#### Sensor.`create`

```python
def create(cls, sensor_type: SpectrumType, location: int, sensor_id: int = None)
```

A factory method to create a new [sensor](#sensor).

##### Input parameters:

- location : Location of the sensor [centimeter].
- sensor_type : Type of the sensor [[SpectrumType](#spectrumtype)].
- sensor_id : Sensor ID, which is used in [sorting_function](#sorting_function) to identify each sensor. 
If no ID is provided, an ID will be generated based on the number of sensors.

##### Returns
- A [sensor](#sensor) object.

---

#### Sensor.`reset_num`

```python
def reset_num(cls)
```

A class method to reset the number of created sensors. This would be helpful if you also want to reset IDs assigned to newly created sensors.

---

#### Conveyor

```python
class Conveyor:
    def __init__(self, speed_cm_per_second: int, dimension:ConveyorDimension)
```

A class to define a new conveyor.

##### Input parameters:

- speed_cm_per_second : Speed of the conveyor [centimeter per second].
- dimension : Dimensions of the conveyor in centimeter.
---

#### Conveyor.`create`

```python
def create(cls, speed_cm_per_second: int, length: int, width: int)
```

A factory method to create a new [conveyor](#conveyor).

##### Input parameters:

- speed_cm_per_second : Speed of the conveyor [centimeter per second].
- length : Length of the conveyor in centimeter.
- width : Width of the conveyor in centimeter.

##### Returns
- A [conveyor](#conveyor) object.

---

#### Sorting_function

```python
def sorting_function(sensors_output)
```

A user-defined function that identifies the type of plastic, based on the given spectrum.

##### Input parameters:

- sensors_output : A dictionary with sensors information. The keys are the id of each sensor.

```python
{
    sensor.id: {
        'type': type,
        'location': location,
        'spectrum': spectrum,
    }
}
```

##### Return value:

- plastic_type dict: [Plastic](#plastic)
```python
decision = {
    sensor_id: plastic_type
}
```

---

#### Plastic

```python
class Plastic(enum.Enum):
    HDPE = 'HDPE'
    LDPE = 'LDPE'
    PP = 'PP'
    PS = 'PS'
    PC = 'PC'
    PVC = 'PVC'
    Polyester = 'Polyester'
    PET = 'PET'
    PU = 'PU'
    Blank = 'background'
```

An enum for all types of plastics

---

#### SpectrumType

```python
class SpectrumType(enum.Enum):
    FTIR = 'FTIR'
    Raman = 'Raman'
```

An enum for all types of sensorss