public class Main {
    public static void main(String[] args) {
        TrafficLight my_traffic_light = new TrafficLight();
        System.out.println(my_traffic_light.displayLight());
        my_traffic_light.switch_light();
        System.out.println(my_traffic_light.displayLight());
        my_traffic_light.switch_light();
        System.out.println(my_traffic_light.displayLight());
        
    }
}
