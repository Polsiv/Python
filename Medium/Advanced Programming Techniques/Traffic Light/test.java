// Importing necessary packages
import java.util.*;

// Defining TrafficLightState interface
interface TrafficLightState {
    String displayLight();
    void switchLight(TrafficLight trafficLight);
}

// Defining abstract class TrafficLightStateAdapter implementing TrafficLightState
abstract class TrafficLightStateAdapter implements TrafficLightState {
    public void switchLight(TrafficLight trafficLight) {
        // Default implementation does nothing
    }
}

// Defining RedState class implementing TrafficLightState
class RedState extends TrafficLightStateAdapter {
    public String displayLight() {
        return "Red";
    }

    public void switchLight(TrafficLight trafficLight) {
        System.out.println("switching from red to red & amber");
        trafficLight.setState(new RedAndAmberState());
    }
}

// Defining RedAndAmberState class implementing TrafficLightState
class RedAndAmberState extends TrafficLightStateAdapter {
    public String displayLight() {
        return "Red & Amber";
    }

    public void switchLight(TrafficLight trafficLight) {
        System.out.println("switching from amber to green");
        trafficLight.setState(new GreenState());
    }
}

// Defining GreenState class implementing TrafficLightState
class GreenState extends TrafficLightStateAdapter {
    public String displayLight() {
        return "Green";
    }

    public void switchLight(TrafficLight trafficLight) {
        System.out.println("switching from green to amber");
        trafficLight.setState(new AmberState());
    }
}

// Defining AmberState class implementing TrafficLightState
class AmberState extends TrafficLightStateAdapter {
    public String displayLight() {
        return "Amber";
    }

    public void switchLight(TrafficLight trafficLight) {
        System.out.println("switching from amber to red");
        trafficLight.setState(new RedState());
    }
}

// Defining TrafficLight class
class TrafficLight {
    private TrafficLightState state;

    public TrafficLight() {
        this.state = new RedState();
    }

    public void setState(TrafficLightState state) {
        this.state = state;
    }

    public String displayLight() {
        return state.displayLight();
    }

    public void switchLight() {
        state.switchLight(this);
    }
}

// Main class to test the traffic light functionality
public class Main {
    public static void main(String[] args) {
        TrafficLight trafficLight = new TrafficLight();
        trafficLight.switchLight();
    }
}
