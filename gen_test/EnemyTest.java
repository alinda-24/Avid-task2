package test;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

class EnemyTest {
    private Enemy enemy;

    @Before
    public void setUp() {
        enemy = new Enemy("Villain", 10, 5, 5);
    }

    @After
    public void tearDown() {
        enemy = null;
    }

    @Test
    public void testGetName() {
        assertEquals("Villain", enemy.getName());
    }

    @Test
    public void testGetDamage() {
        assertEquals(10, enemy.getDamage());
    }

    @Test
    public void testGetPositionX() {
        assertEquals(5, enemy.getPositionX());
    }

    @Test
    public void testGetPositionY() {
        assertEquals(5, enemy.getPositionY());
    }

    @Test
    public void testSetName() {
        enemy.setName("NewVillain");
        assertEquals("NewVillain", enemy.getName());
    }

    @Test
    public void testSetDamage() {
        enemy.setDamage(15);
        assertEquals(15, enemy.getDamage());
    }

    @Test
    public void testSetPositionX() {
        enemy.setPositionX(10);
        assertEquals(10, enemy.getPositionX());
    }

    @Test
    public void testSetPositionY() {
        enemy.setPositionY(10);
        assertEquals(10, enemy.getPositionY());
    }

    @Test
    public void testInitialPosition() {
        assertEquals(5, enemy.getPositionX());
        assertEquals(5, enemy.getPositionY());
    }

    @Test
    public void testNegativePosition() {
        enemy.setPositionX(-5);
        enemy.setPositionY(-5);
        assertEquals(-5, enemy.getPositionX());
        assertEquals(-5, enemy.getPositionY());
    }

    @Test
    public void testZeroDamage() {
        enemy.setDamage(0);
        assertEquals(0, enemy.getDamage());
    }
}

// PlayerTest.java

package yourpackage;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public 