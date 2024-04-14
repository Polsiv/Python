from abc import ABC, abstractmethod

#States

class TrafficLightState(ABC):
    
    @abstractmethod
    def display_light(self):
        pass
    
    def switch_light(self, traffic_light):
        pass

class RedState(TrafficLightState):
    def display_light(self):
        return "Red"

    def switch_light(self, traffic_light):
        print("switching from red to red & amber")
        traffic_light.state = RedAndAmberState()

class RedAndAmberState(TrafficLightState):
    def display_light(self):
        return "Red & Amber"

    def switch_light(self, traffic_light):
        print("switching from amber to green")
        traffic_light.state = GreenState()

class GreenState(TrafficLightState):
    def display_light(self):
        return "Green"

    def switch_light(self, traffic_light):
        print("switching from green to amber")
        traffic_light.state = AmberState()

class AmberState(TrafficLightState):
    def display_light(self):
        return "Amber"

    def switch_light(self, traffic_light):
        print("switching from amber to Red")
        traffic_light.state = RedState()

#context

class TrafficLight:
    def __init__(self):
        self.state = RedState()

    def display_light(self):
        return self.state.display_light()
    
    def switch_light(self):
        return self.state.switch_light(self)
    

traffic_light = TrafficLight()
traffic_light.switch_light()
print(traffic_light.display_light())
traffic_light.switch_light()
print(traffic_light.display_light())
traffic_light.switch_light()