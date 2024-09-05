package test;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

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

    public void interact(Player player) {
        if (this.position == player.getPosition()) {
            System.out.println("Enemy found " + player.getName() + " at position " + this.position +
                               " and reduces score by " + this.attackPower);
            player.updateScore(-this.attackPower);
        }
    }
}

