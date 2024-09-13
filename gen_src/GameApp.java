class GameApp {
    public static void main(String[] args) {
        Player player = new Player("Hero", 0, 0);
        Enemy enemy = new Enemy("Villain", 10, 5, 5);

        player.move(2, 3);
        player.printStatus();

        player.setScore(10); // Example interaction updating player's score
        
        enemy.printStatus();
    }
}