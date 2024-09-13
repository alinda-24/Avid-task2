class Enemy {
    private String name;
    private int damage;
    private int positionX;
    private int positionY;

    public Enemy(String name, int damage, int positionX, int positionY) {
        this.name = name; // Avoid variable shadowing by using 'this'
        this.damage = damage;
        this.positionX = positionX;
        this.positionY = positionY;
    }

    // Getters
    public String getName() {
        return name;
    }

    public int getDamage() {
        return damage;
    }

    public int getPositionX() {
        return positionX;
    }

    public int getPositionY() {
        return positionY;
    }

    // Setters
    public void setName(String name) {
        this.name = name;
    }

    public void setDamage(int damage) {
        this.damage = damage;
    }

    public void setPositionX(int positionX) {
        this.positionX = positionX;
    }

    public void setPositionY(int positionY) {
        this.positionY = positionY;
    }

    // Method to print enemy status
    public void printStatus() {
        System.out.println("Enemy: " + name + ", Damage: " + damage 
                           + ", Position: (" + positionX + "," + positionY + ")");
    }
}

// GameApp.java
public 