class Player {
    private String name;
    private int score;
    private int positionX;
    private int positionY;

    // Constructor for initializing the Player
    public Player(String name, int positionX, int positionY) {
        this.name = name;
        this.positionX = positionX;
        this.positionY = positionY;
        this.score = 0; // Initialize the score to 0
    }

    // Getter for name
    public String getName() {
        return name;
    }

    // Setter for name
    public void setName(String name) {
        this.name = name;
    }

    // Getter for score
    public int getScore() {
        return score;
    }

    // Setter for score
    public void setScore(int score) {
        this.score = score;
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
    
    // Method to move the player
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