class RedAndAmberState implements TrafficLightState {
  
    public String display_light() {
        return "Red & Amber";
    }

    public void switch_light(TrafficLight trafficLight) {
        System.out.println("switching from amber to green");
        trafficLight.setState(new GreenState());
    }
}