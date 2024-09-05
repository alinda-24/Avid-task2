import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public class IndamonTest {
    private Indamon indamon1;
    private Indamon indamon2;

    @Before
    public void setUp() {
        indamon1 = new Indamon("Glassey", 10, 5, 5);
        indamon2 = new Indamon("Siberov", 10, 5, 5);
    }

    @Test
    public void testGetName() {
        assertEquals("Glassey", indamon1.getName());
        assertEquals("Siberov", indamon2.getName());
    }

    @Test
    public void testGetHp() {
        assertEquals(10, indamon1.getHp());
        assertEquals(10, indamon2.getHp());
    }

    @Test
    public void testGetAttack() {
        assertEquals(5, indamon1.getAttack());
        assertEquals(5, indamon2.getAttack());
    }

    @Test
    public void testGetDefense() {
        assertEquals(5, indamon1.getDefense());
        assertEquals(5, indamon2.getDefense());
    }

    @Test
    public void testGetFainted() {
        assertEquals(false, indamon1.getFainted());
        assertEquals(false, indamon2.getFainted());
    }

    @Test
    public void testSetName() {
        indamon1.setName("NewName");
        assertEquals("NewName", indamon1.getName());
    }

    @Test
    public void testSetHp() {
        indamon1.setHp(20);
        assertEquals(20, indamon1.getHp());
    }

    @Test
    public void testSetAttack() {
        indamon1.setAttack(7);
        assertEquals(7, indamon1.getAttack());
    }

    @Test
    public void testSetDefense() {
        indamon1.setDefense(8);
        assertEquals(8, indamon1.getDefense());
    }

    @Test
    public void testSetFainted() {
        indamon1.setFainted(true);
        assertEquals(true, indamon1.getFainted());
    }

    @Test
    public void testAttack() {
        indamon1 = new Indamon("Glassey", 10, 5, 5);
        indamon2 = new Indamon("Siberov", 10, 5, 5);
        indamon1.attack(indamon2);
        assertEquals(9, indamon2.getHp()); // As attack is 5 and defense is 5, damage should be 5/5=1, and thus HP should reduce by 1 from 10 to 9
        assertEquals(false, indamon2.getFainted());
    }
}
