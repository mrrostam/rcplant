from _recycling_plant import *


class RPSimulation:
    def __init__(self, sorting_function, final_time, time_step=1):
        self.time_step = time_step
        self.final_time = final_time
        self.recycling_plant = RecyclingPlant(sorting_function)
        self.total_missed = 0
        self.total_classified = 0
        self.total_mistyped = 0

    def update(self, active=True):
        missed, classified, mistyped = self.recycling_plant.update(self.time_step, active)
        self.total_missed += missed
        self.total_classified += classified
        self.total_mistyped += mistyped

    def run(self):
        for time in range(0, self.final_time, self.time_step):
            self.update()
        for time in range(0, self.final_time, self.time_step):
            self.update(False)