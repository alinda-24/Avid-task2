class Enemy {
    private int position;
    private int attackPower;

    public Enemy(int position, int attackPower) {
        this.position = position;
        this.attackPower = attackPower;
    }

    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }

    public int getAttackPower() {
        return attackPower;
    }

    public void setAttackPower(int attackPower) {
        this.attackPower = attackPower;
    }

    // Interact with a player by reducing their score if they are at the same position
    public void interact(Player player) {
        if (this.position == player.getPosition()) {
            System.out.println("Enemy found " + player.getName() + " at position " + this.position +
                               " and reduces score by " + this.attackPower);
            player.updateScore(-this.attackPower);
        }
    }
}
```

**Game.java**
```java
public 