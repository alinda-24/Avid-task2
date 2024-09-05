package test;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

class PlayerTest {
    private Player player;

    @Before
    public void setUp() {
        player = new Player("Hero", 0, 0);
    }

    @Test
    public void testInitialSetup() {
        assertEquals("Hero", player.getName());
        assertEquals(0, player.getPosition());
        assertEquals(0, player.getScore());
    }

    @Test
    public void testMovePlayer() {
        player.move(5);
        assertEquals(5, player.getPosition());
        player.move(-3);
        assertEquals(2, player.getPosition());
    }

    @Test
    public void testUpdateScore() {
        player.updateScore(10);
        assertEquals(10, player.getScore());
        player.updateScore(-5);
        assertEquals(5, player.getScore());
    }

    @Test
    public void testSetName() {
        player.setName("Champion");
        assertEquals("Champion", player.getName());
    }

    @Test
    public void testSetPosition() {
        player.setPosition(10);
        assertEquals(10, player.getPosition());
    }

    @Test
    public void testSetScore() {
        player.setScore(50);
        assertEquals(50, player.getScore());
    }
}

package test;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

public 