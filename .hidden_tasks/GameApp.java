class GameApp {
    public static void main(String[] args) {
        // Create a Player instance
        Player player = new Player("Hero", 0, 0);

        // Create an Enemy instance
        Enemy enemy = new Enemy("Villain", 10, 5, 5);

        // Interact with Player and Enemy objects
        player.move(2, 3);
        player.printStatus();

        enemy.printStatus();
    }
}

// ShadowExample.java
public 