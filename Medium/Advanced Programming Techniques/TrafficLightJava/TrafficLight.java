
class TrafficLight {
    private TrafficLightState state;

    public TrafficLight() {
        this.state = new RedState();
    }

    public void setState(TrafficLightState state) {
        this.state = state;
    }

    public String displayLight() {
        return state.display_light();
    }

    public void switch_light() {
        state.switch_light(this);
    }
}