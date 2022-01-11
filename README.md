# Recycling Plant Simulator Package

This project is structured as a standalone package so that it can easily be installed using `pip`. However, it's not released anywhere yet.

## Setup

Install dependencies:

```console
pip install -r requirements.txt
```

or

```console
pip3 install -r requirements.txt
```

## Quick start

For quick testing, run the [main.py](main.py) script:

```console
python main.py
```

or

```console
python3 main.py
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
            mode: string
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
    def __init__(self, sensor_type: SpectrumType, location_cm: int)
```

A class to define a new sensor

##### Input parameters:

- location_cm : Location of the sensor [centimeter].
- sensor_type : Type of the sensor [[SpectrumType](#spectrumtype)].

---

#### Sensor.`create`

```python
def create(cls, sensor_type: SpectrumType, location: int)
```

A factory method to create a new [sensor](#sensor).

##### Input parameters:

- location_cm : Location of the sensor [centimeter].
- sensor_type : Type of the sensor [[SpectrumType](#spectrumtype)].

##### Returns
- A [sensor](#sensor) object.

---

#### Conveyor

```python
class Conveyor:
    def __init__(self, speed_cm_per_second: int, dimension:ConveyorDimension)
```

A class to define a new conveyor

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

- sensors_output : A dictionary with sensors information. The keys are the global unique identifier of each sensors.

```python
{
    sensor.guid: {
        'type': type,
        'location': location,
        'spectrum': spectrum,
    }
}
```

##### Return value:

- plastic_type: [[Plastic](#plastic)]

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
```

An enum for all types of plastics

---

#### SpectrumType

```python
class SpectrumType(enum.Enum):
    FTIR = 'FTIR'
    Raman = 'Raman'
```

An enum for all types of sensors

---


## TODO:

- Add real values for the background spectrum to the dataset files instead of `zeros`
- Implement simple 2D sensors
- Implement simple actuators