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

    @After
    public void tearDown() {
        player = null;
    }

    @Test
    public void testGetName() {
        assertEquals("Hero", player.getName());
    }

    @Test
    public void testGetScore() {
        assertEquals(0, player.getScore());
    }

    @Test
    public void testGetPositionX() {
        assertEquals(0, player.getPositionX());
    }

    @Test
    public void testGetPositionY() {
        assertEquals(0, player.getPositionY());
    }

    @Test
    public void testSetName() {
        player.setName("NewHero");
        assertEquals("NewHero", player.getName());
    }

    @Test
    public void testSetScore() {
        player.setScore(100);
        assertEquals(100, player.getScore());
    }

    @Test
    public void testSetPositionX() {
        player.setPositionX(10);
        assertEquals(10, player.getPositionX());
    }

    @Test
    public void testSetPositionY() {
        player.setPositionY(10);
        assertEquals(10, player.getPositionY());
    }

    @Test
    public void testMove() {
        player.move(3, 4);
        assertEquals(3, player.getPositionX());
        assertEquals(4, player.getPositionY());
    }

    @Test
    public void testContinuousMove() {
        player.move(3, 4);
        player.move(-1, -1);
        assertEquals(2, player.getPositionX());
        assertEquals(3, player.getPositionY());
    }
}

// ShadowExampleTest.java

package yourpackage;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public 