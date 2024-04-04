class RedState implements TrafficLightState {
    
    public String display_light() {
        return "Red";
    }

    public void switch_light(TrafficLight traffic_light) {
        System.out.println("switching from red to red & amber");
        traffic_light.setState(new RedAndAmberState());;
    }
}