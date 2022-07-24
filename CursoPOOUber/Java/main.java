class main {
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
        Car car = new Car("AMQ123", new Account("Andres Herrera", "1045802365"));
        car.passegenger = 4;
        car.printDataCar();

        Car car2 = new Car("AAQ145", new Account("Andrea Herrera", "1054823646"));
        car2.passegenger = 3;
        car2.printDataCar();
    }
}