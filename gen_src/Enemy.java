class Enemy {
    private String name;
    private int damage;
    private int positionX;
    private int positionY;

    // Constructor for initializing the Enemy
    public Enemy(String name, int damage, int positionX, int positionY) {
        this.name = name;
        this.damage = damage;
        this.positionX = positionX;
        this.positionY = positionY;
    }

    // Getter for name
    public String getName() {
        return name;
    }

    // Setter for name
    public void setName(String name) {
        this.name = name;
    }

    // Getter for damage
    public int getDamage() {
        return damage;
    }

    // Setter for damage
    public void setDamage(int damage) {
        this.damage = damage;
    }

    // Getter for positionX
    public int getPositionX() {
        return positionX;
    }

    // Setter for positionX
    public void setPositionX(int positionX) {
        this.positionX = positionX;
    }

    // Getter for positionY
    public int getPositionY() {
        return positionY;
    }

    // Setter for positionY
    public void setPositionY(int positionY) {
        this.positionY = positionY;
    }
    
    // Method to print enemy status
    public void printStatus() {
        System.out.println("Enemy: " + name + ", Damage: " + damage + ", Position: (" + positionX + "," + positionY + ")");
    }
}

// GameApp.java
public 