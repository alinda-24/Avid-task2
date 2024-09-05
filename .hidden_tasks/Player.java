class Player {
    private String name;
    private int position;
    private int score;

    public Player(String name, int position, int score) {
        this.name = name;
        this.position = position;
        this.score = score;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }

    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }

    // Move the player by a certain distance on the grid
    public void move(int distance) {
        this.position += distance;
        System.out.println(name + " moved to position " + this.position);
    }

    // Update the player's score by a certain number of points
    public void updateScore(int points) {
        this.score += points;
        System.out.println(name + "'s new score is " + this.score);
    }

    // Print player's information
    public void printInfo() {
        System.out.println("Player: " + name + ", Position: " + position + ", Score: " + score);
    }
}
```

**Enemy.java**
```java
public 