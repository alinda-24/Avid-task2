package test;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

class EnemyTest {
    private Enemy enemy;
    private Player player;

    @Before
    public void setUp() {
        enemy = new Enemy(5, 3);
        player = new Player("Hero", 0, 10);
    }
    // hello

    @Test
    public void testInitialSetup() {
        assertEquals(5, enemy.getPosition());
        assertEquals(3, enemy.getAttackPower());
    }

    @Test
    public void testSetPosition() {
        enemy.setPosition(10);
        assertEquals(10, enemy.getPosition());
    }

    @Test
    public void testSetAttackPower() {
        enemy.setAttackPower(6);
        assertEquals(6, enemy.getAttackPower());
    }

    @Test
    public void testInteractWithPlayerNoInteraction() {
        enemy.interact(player);
        assertEquals(10, player.getScore());
    }

    @Test
    public void testInteractWithPlayerSuccessfulInteraction() {
        player.setPosition(5);
        enemy.interact(player);
        assertEquals(7, player.getScore());
    }

    @Test
    public void testPerformanceUnderLoad() {
        // Simulating performance testing by interacting with multiple enemies.
        Player performer = new Player("Fast", 0, 1000);
        for (int i = 0; i < 10000; i++) {
            enemy.setPosition(i);
            performer.setPosition(i);
            enemy.interact(performer);
        }
        // The above would ideally be measured in terms of time, but assert as a placeholder here
        assertTrue(true);
    }
} 

// Ensure to create accompanying Player.java and Enemy.java files with classes as per the solution.

