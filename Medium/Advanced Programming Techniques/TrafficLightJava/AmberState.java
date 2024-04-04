class AmberState implements TrafficLightState {
    
    public String display_light() {
        return "Amber";
    }

    public void switch_light(TrafficLight trafficLight) {
        System.out.println("switching from amber to red");
        trafficLight.setState(new RedState());
    }
}