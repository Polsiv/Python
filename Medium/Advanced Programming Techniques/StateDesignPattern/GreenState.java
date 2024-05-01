class GreenState implements TrafficLightState {
    
    public String display_light() {
        return "Green";
    }

    public void switch_light(TrafficLight trafficLight) {
        System.out.println("switching from green to amber");
        trafficLight.setState(new AmberState());
    }
}
