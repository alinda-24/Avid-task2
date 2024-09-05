class Game {

    public static void main(String[] args) {
        // Create a new Player object
        Player hero = new Player("Hero", 0, 0);

        // Print the player's initial information
        hero.printInfo();

        // Move the player and update their score
        hero.move(5);
        hero.updateScore(10);

        // Initialize an Enemy at position 5 with attack power of 3
        Enemy villain = new Enemy(5, 3);

        // Simulate an interaction between the player and the enemy
        villain.interact(hero);

        // Print player's final state
        hero.printInfo();
    }
}
```

Each of these classes is contained within their respective `.java` files. You can compile and run the `Game` 