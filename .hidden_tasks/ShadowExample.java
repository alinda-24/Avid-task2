class ShadowExample {
    private int value = 0;

    public void printValue() {
        int value = 100; // This local variable shadows the instance variable
        System.out.println(this.value); // Use 'this' to refer to the field value
    }

    public static void main(String[] args) {
        new ShadowExample().printValue();
    }
}