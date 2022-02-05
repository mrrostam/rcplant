
# Mathematical Guide

## Loading area

The location (x, y) will be assigned to the containers. Where the x-direction is the width of the conveyor belt and the y-direction is the length of the conveyor belt. We can assume that the x-location of a container does not change with time. The y-location of the container moves according to `conveyor_speed`. 

The simulator simulates the recycling environment for `final_time_min` minutes. This period was divided into `int(self._final_time_sec // self._time_step_sec)` time slices where `self._time_step_sec = 0.1`.  

In each time slice, the y-location of containers will move forward at one `conveyor_speed`. The containers will be scanned by sensors when it arrives `sensing_zone_location`. The container generate function will be called and load new containers at a rate of X? based on random number generator

---

## Sensing area

Sensors will refresh its state based on its `sampling_rate`, if the state is active, it will output the spectra of containers  that are in the sensing area `sensors_output`. 

If `conveyor_speed` is too high or sensors' sampling rate is too low, containers might pass through `conveyor_length` without being scanned and result in an increase in `simulator.total_missed` 

---

## Sorting area

`user_sorting_function()` should return a dictionary, where the value of it should be one type in `Plastic` class, and the key should be x-value? The simulator will then take the return value of `user_sorting_function()` and determine whether the `Plastic` type and `container.location` match the correct type and location. If it is, `simulator.total_missed` will be added by 1, otherwise `simulator.mistyped_container` will be added by 1.

---