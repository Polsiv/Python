class RedAndAmberState implements TrafficLightState {
  
    public String display_light() {
        return "Red & Amber";
    }

    public void switch_light(TrafficLight traffic_light) {
        System.out.println("switching from amber to green");
        traffic_light.setState(new GreenState());
    }
}