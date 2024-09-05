class Player {
    private String name;
    private int position;
    private int score;
    
    // Constructor to initialize the player's attributes
    public Player(String name, int position, int score) {
        this.name = name;
        this.position = position;
        this.score = score;
    }
    
    // Getter for name
    public String getName() {
        return name;
    }

    // Setter for name
    public void setName(String name) {
        this.name = name;
    }

    // Getter for position
    public int getPosition() {
        return position;
    }

    // Setter for position
    public void setPosition(int position) {
        this.position = position;
    }

    // Getter for score
    public int getScore() {
        return score;
    }

    // Setter for score
    public void setScore(int score) {
        this.score = score;
    }
    
    // Method to move the player by a certain distance
    public void move(int distance) {
        this.position += distance;
    }

    // Method to update the player's score
    public void updateScore(int points) {
        this.score += points;
    }
    
    // Method to print player's current state
    public void printInfo() {
        System.out.println("Player Name: " + name);
        System.out.println("Position: " + position);
        System.out.println("Score: " + score);
    }
    
    public static void main(String[] args) {
        // Create a Player instance
        Player hero = new Player("Hero", 0, 0);
        hero.printInfo(); // Print initial state
        
        // Simulate player movement and score update
        hero.move(5);
        hero.updateScore(10);
        hero.printInfo(); // Print updated state
        
        // Creating an enemy and testing interaction
        Enemy monster = new Enemy("Monster", 5);
        monster.interact(hero);
        hero.printInfo(); // Print state after interaction
    }
}
```

Enemy.java
```java
public 