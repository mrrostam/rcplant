# McMaster Recycling Plant Simulator Handout

This handout introduces the structure and API for the simulator. You will be asked to write `user_sorting_function(sensors_output)` as required to complete the whole simulation.  
  
The accuracy of the simulator depends on the performance of `user_sorting_function(sensors_output)`

<br/>

## Loading Zone

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

    class Container:
        def __init__(self, plastic_type: Plastic, dimension: ContainerDimension, location: ContainerLocation):
            self._material = Material(plastic_type)
```

### Containers Generation Description:
The simulator will generate containers with random `Plastic` types at a rate of X, X is associated with `conveyor_speed`. To achieve the requirement of loading rate, you may need to choose an appropriate `conveyor_speed` in your design.  `ContainerDimension` is a class with attributes `self._length, self._width, self._height`, which are assigned randomly in the range of 5 to 15 cm. `ContainerLocation` is a class with default attributes `self._x = self._y = self._z = 0`

In our case, the envrionment simulates the sensors in 1D case and the containers will not overlap each other

<br/>

```python
    class Conveyor:
        def __init__(self, speed_cm_per_second: int, dimension: ConveyorDimension):
```

### Conveyor Description:   
Containers are assgined location (x, y) where y-direction is the `conveyor_length` of the belt and x-direction is `conveyor_width`. We assume `container.location.y` moves along the belt at a speed of `conveyor_speed` while `container.location.x` does not change with time.

The ratio of missed containers is inversely proportional to `conveyor_speed`  as the sensors' performance is limited by its sampling frequency, that is an item will be missed if it moves too fast to be scanned.

<br/>

```python
    num_containers = 100
```

### Parameter description:  
`num_containers` is the total number of containers the simulator will run

---

<br/>

## Sensing Zone

```python
    sensors = [
        Sensor.create(SpectrumType.FTIR, sensing_zone_location_1),
        Sensor.create(SpectrumType.Raman, sensing_zone_location_2),
    ]

    class Sensor:
        def __init__(self, sensor_type: SpectrumType, location_cm: int)
```

### Sensors description:  
Each sensor is associated with the `sensor_type` and `location_cm`. As introduced in the project module, sensors have two types -- `SpectrumType.FTIR` and `SpectrumType.Raman`. Their locations could be designed by yourself.

When the containers are passing the `sensing_zone_location`, the simulated environment will output the spectra of the containers -- `sensor_output` in a nested discionary. Thus, to access the actual spectra, you may need to use the correct indexing syntax. The spectra is stored in Pandas.Series data type.

For areas where there are no containers, an 0 that stands for blank spectrum will be outputted.

```python
    sensors_sampling_frequency = 1  # Hz

    VALID_SENSORS_FREQUENCIES_HZ = [10, 5, 2, 1]  # divisors of SIMULATION_FREQUENCY_HZ
```

### Sampling Frequency:
Sensors have 4 valid sampling frquency = [10, 5, 2, 1]. Higher frequency will decrease the ratio of missed containers when the conveyor speed is a constant. However, in `testing` mode, a signal noise will be introduced  that will increase proportionally to the sampling frequency. Thus, there is a trade-off among conveyor speed, sampling frequency and sorting accuracy. 

---

<br/>

## Sorting Zone

```python
    def user_sorting_function(sensors_output):
```

### Sorting Function description:  
Sensors scan and output containers' spectra in the sensing zone, which will be used as an input argument to `user_sorting_function()`. The function will be passed to `RPSimulation` class. The return value of `user_sorting_function()` will be used to sort containers.

### Input parameters:
- `sensor_output`  is a nested dictionary where the inside one contains SpectrumType class as key and Spectrum in Pandas.Series structure as value  
    e.g. 
```python
    class SpectrumType(enum.Enum):
        FTIR = 'FTIR'
        Raman = 'Raman'  

    sensors_output = {sensor_id: {'type': <SpectrumType.FTIR: 'FTIR'>, 'location': 500, 'spectrum': Spectrum of sensed containers in pandas.Series data type}}

    sensors_output[1]['spectrum'] example:    
        3600    0.001203
        3598    0.000943
        3596    0.000712
        3594    0.000733
        3592    0.000649
                ...
        1258    0.597359
        1256    0.619357
        1254    0.641317
        1252    0.663742
        1250    0.684752
        Name: PET, Length: 1176, dtype: float64 
 
```
- What you need to do is to analyze the value of sensors_output to determine the type of the containers by your own functions and return the result into the simulator

### Return value:
- The data type of return value is a dictionary, of which the key is **SpectrumType class** and the value is **Plastic class**  
```python 
    example:

    return {sensor_id: <Plastic.Polyester: 'Polyester'>}

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

### Simulation Mode
```python
    class SimulationMode(enum.Enum):
        Testing = 'testing'
        Training = 'training'

```
In training mode, the simulator runs nomrally to complete loading, sensing and sorting function. The spectra of containers come from the original source of the spectra database. While in testing mode, the noise will be introduced to the spectra of `sensor_output` when sensors read the containers to test the adaptability of the sorting function. The signal-to-noise ratio (SNR) is proportional to the sampling frequency, which means the higher sampling frequency you use, the more noise will be added during reading.


## Description
The model simultes different types of plastic containers loaded at a specific rate in the loading zone, moves along the belt and passes through the sensing zone, and then are sorted by the sorting function developed by your team in the sorting zone.

The input parameters you are going to deal with are:
- `conveyor_length` and `conveyor_width`
- `conveyor_speed`
- `num_containers`
- `sensing_zone_location_1` and/or `sensing_zone_location_2`
- `sensors_sampling_frequency`
- `simulation_mode`
- `user_sorting_function(sensor_output)`

The outputs from the simulator are:
- Total missed containers
- Total sorted containers
- Total mistyped containers
- Total elapsed time

### Loading Zone
Types of plastic:
- PET (Polyethylene Terephthalate) 
- HDPE (High-Density Polyethylene) 
- PVC (Polyvinyl Chloride) 
- LDPE (Low-Density Polyethylene) 
- PP (Polypropylene) 
- PS (Polystyrene) 
- Polyester     combine to others?
- PV ()
- PU ()

The type of container will be represented by the spectrum associated with the type of plastic and are assigned a random size in the range of 5 to 15 cm in length. To simplify the problem, we will assume that the containers do not overlap each other. The containers must fit on the conveyor belt and once they are loaded they do not move or roll on the belt.

To simulate the containers on a conveyor belt, the location (x.y) will be assigned to the containers. Where the x-direction is the width of the conveyor belt and the y-direction is the length of the conveyor belt. We can assume that the x-location of a container does not change with time. The y-location of the container moves according to the conveyor speed. 

Several parameters you could adjust here are the conveyor_length and conveyor_width, conveyor_speed and num_containers.
-  `conveyor_length` and `conveyor_width` 
   -  They are not critical in the simulation but you need to concern the physical constraints like the space for the recycling plant that were introduced in the previous design studio
  
-  `conveyor_speed` 
   -  This is associated with the rate of generating containers. To achieve the reqirement for the amount of daily recycling waste, the recycling plant need to have sufficient throughput to process waste. However, the throughput is limited by the sampling frequency of the sensors. If the conveyor moves too fast, there will be no enough time for sensors to get the spectrum of the containers. Thus, there is a trade-off between conveyor_speed and sensors_sampling_frequency you need to be aware of.
  
- `num_container` 
  - This is the total amount of container the simulator will run. You can determine the throughput of your design based on num_container and the output - total elasped time .

### Sensing Zone
When the containers are in the sensing zone, the simulated environment will output the properties of the containers. For areas where there are no containers, the simulated environment will output a blank spectrum. 

You can choose sensors between FTIR and Raman or even both, but in our case, only one sensor can be installed on one conveyor. That is, if you choose to use two sensors, your deisgn will be a convoyer belt with one type of sensor connected by a pneumatic system, below which, another conveyor belt is installed with one type of sensor to determine the remaining unsorted containers, at the end of it there will be another pneumatic system as well. 

You will need to interpret the sensors_output in your user_sorting_function() to determine the plastic types of the containers. The result will be passed back to the simulated environment to sort the containers. 

You will also need to adjust an appropriate sensors_sampling_frequency. In addition to the trade-off between throughput and total missed containers mentioned before, the sampling frequency will also impact sensor's resolution on obatining the container's spectrum. In the training mode, the sensors will run ideally to get rid of the impact and obtain the original spectrum from the database. However, in the testing mode, a noise that is proportional to the sampling frequency will be added to the spectrum. That is, the resolution will decrease if the sampling frequency increases.

Parameters you should adjust here are the sensing_zone_location_1 and/or sensing_zone_location_2, sensors_sampling_frequency and simulation_mode
- `sensing_zone_location_1` and/or `sensing_zone_location_2`
  - You can choose between FTIR sensor and Raman sensor or even both sensors. Each of those will be assigned a location where the containers passes through, the spectrum will be obained if the conveyor speed does not go beyond the sampling frequency.
- `sensors_sampling_frequency`
  - Available sampling frequency are [1, 2, 5, 10] Hz. The ideal equation will be container_length / conveyor_speed > sensor_sampling_frequency to make sure there is no container missed. However, some missed containers are tolerant if you prefer the trade-off for more throughput or less mistyped containers, as long as your design idea is reasonable and practical. 
- `simulation_mode`
  - There are two types of simulation mode: training and testing. Only difference between them is that in testing mode, a noise that is proportional to sampling frequency will be introduced and added to the spectrum when sensors read the containers, which makes the sensor's resolution worse. while in the training mode, you don't need to be concerned about the trade-off between sampling frequency and the resolution.


### Sorting Zone
We will assume that sorting will take place at the end of the conveyor belt.**(Need code updated)** The sorting mechanism will be based on the user_sorting_function developed by your group. The function should analyze the sensor data that stores the spectrum (black or material spectrum) the sensor reads in a nested dictionary and return the type of plastic to the simulated environment for sorting.

The simulated environment takes the return value and determine whether the container is accurately sorted. Total mistyped containers or total sorted containers will be added by one if it is either correctly sorted or incorrectly sorted. If the container moves too fast to be read, no plastic type will be associated to that container, such that the container will end up running off the conveyor and the total missed containers will be added by one. 

The simulated environment will store actual plastic type and the plastic type identified by your sorting function of the entire set of containers. You can easily compare these two sets to see the actual accuracy rate. Since it record every plastic type, you can determine the problems like if only one type of plastic are always mistyped.

Parameter you should adjust here is
- `user_sorting_function(sensor_output)`
  - `sensor_output` is a nested dictionary where the inside dictionary contains SpectrumType class as key and Spectrum in Pandas.Series structure as value. 
  - e.g.,
```python
    sensors_output = {sensor_id: {'type': <SpectrumType.FTIR: 'FTIR'>, 'location': 500, 'spectrum': spectrum of sensed containers in pandas.Series data type}}
```

  - One way to access the spectrum:
```python 
    >>>print(sensors_output[1]['spectrum'])
    >>>
        3600    0.001203
        3598    0.000943
        3596    0.000712
        3594    0.000733
        3592    0.000649
                ...
        1258    0.597359
        1256    0.619357
        1254    0.641317
        1252    0.663742
        1250    0.684752
        Name: PET, Length: 1176, dtype: float64 
 
```
