# Recycling Plant Simulator Package

This project is structured as a standalone package so that it can easily be installed using `pip`. However, it's not
released anywhere yet.

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

You may modify the [`user_sorting_function`](src/main.py) function and implement your logic for sorting plastic
containers.

## API

---

#### `RPSimulation`

```python
class RPSimulation:
    def __init__(
            self,
            sorting_function,
            final_time_min,
            sensors=None,
            conveyor=None
    )
```

A manager class for the recycling plant simulator.

##### Input parameters:

- [sorting_function](#sorting_function) : A user-defined function that gets the output of the sensors and identifies the type of plastic, based on the given spectrum.
- final_time_min : Duration of the simulation [minutes].
- sensors : An array of [Sensors](#sensor).
- conveyor : A user-defined [Conveyor](#conveyor) system.

---

#### RPSimulation.`run`

```python
def run(self)
```

A function to run the simulation and output the results

##### Outputs:

- missed : Number of missed containers.
- classified : Number of classified containers.
- mistyped : Number of containers classified incorrectly.

---

#### Sensor

```python
class Sensor:
    def __init__(self, location_cm, sensor_type)
```

A class to define a new sensor

##### Input parameters:

- location_cm : Location of the sensor [centimeter].
- sensor_type : Type of the sensor [[SpectrumType](#spectrumtype)].

---

#### Conveyor

```python
class Conveyor:
    def __init__(self, speed_cm_per_second, length_cm)
```

A class to define a new conveyor

##### Input parameters:

- speed_cm_per_second : Speed of the conveyor [centimeter per second].
- length_cm : The length of the conveyor [centimeter].

---

#### sorting_function

```python
def sorting_function(sensors_output)
```

A user-defined function that identifies the type of plastic, based on the given
spectrum.

##### Input parameters:

- sensors_output : An array containing all available types of spectrum for the detected container.

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