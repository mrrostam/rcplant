# Recycling Plant Simulator Package

This project is structured as a standalone package so that it can easily be installed using `pip`.
However, it's not released yet anywhere.

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

For quick testing, you may go to the `src` folder and run the `main.py` script:

```console
python main.py
```

or 

```console
python3 main.py
```

## API

---

#### `RPSimulation`

```python
class RPSimulation:
    def __init__(self, sorting_function, final_time, time_step=1):
```

A class that manages everything.

##### Input parameters:
- sorting_function : A user_defined function that gets the sensors output and identifies the type of the the plastic based on given spectrum.
- final_time : The duration of simulation
- time_step : Time step

---

#### RPSimulation.`run`

```python
def run(self):
```

A simple function to run the simulation and output the results

##### Outputs:
- missed : Number of missed containers
- classified : Number of classified containers
- mistyped : Number of containers that classified incorrectly

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

An enum for all types of plastic

---


## TODO:
- Manage multiple sensors
- Sensors should return background spectrum instead of `None`
- Add more database and sensor type
- Add sampling time to sensors
- 