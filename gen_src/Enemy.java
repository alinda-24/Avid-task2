class Enemy {
    private String type;
    private int position;
    
    // Constructor to set enemy's type and position
    public Enemy(String type, int position) {
        this.type = type;
        this.position = position;
    }
    
    // Getter for type
    public String getType() {
        return type;
    }
    
    // Setter for type
    public void setType(String type) {
        this.type = type;
    }

    // Getter for position
    public int getPosition() {
        return position;
    }
    
    // Setter for position
    public void setPosition(int position) {
        this.position = position;
    }
    
    // Method to interact with the player
    public void interact(Player player) {
        if (this.position == player.getPosition()) {
            player.updateScore(-5); // Example penalty
            System.out.println(player.getName() + " encountered an enemy!");
        }
    }
}
```

Explanation:
- The `Player` 