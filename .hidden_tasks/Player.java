class Player {
    private String name;
    private int score;
    private int positionX;
    private int positionY;

    public Player(String name, int positionX, int positionY) {
        this.name = name; // Avoid variable shadowing by using 'this'
        this.positionX = positionX;
        this.positionY = positionY;
        this.score = 0; // Score initialized to 0
    }

    // Getters
    public String getName() {
        return name;
    }

    public int getScore() {
        return score;
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

    public void setScore(int score) {
        this.score = score;
    }

    public void setPositionX(int positionX) {
        this.positionX = positionX;
    }

    public void setPositionY(int positionY) {
        this.positionY = positionY;
    }

    // Methods to move the player
    public void move(int deltaX, int deltaY) {
        this.positionX += deltaX;
        this.positionY += deltaY;
        System.out.println(name + " moved to position (" + positionX + "," + positionY + ")");
    }

    // Method to print player status
    public void printStatus() {
        System.out.println("Player: " + name + ", Score: " + score);
    }
}

// Enemy.java
public 