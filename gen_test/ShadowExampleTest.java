package test;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

class ShadowExampleTest {
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;

    @Before
    public void setUp() {
        System.setOut(new PrintStream(outContent));
    }

    @After
    public void tearDown() {
        System.setOut(originalOut);
    }

    @Test
    public void testPrintValue() {
        ShadowExample example = new ShadowExample();
        example.printValue();
        assertEquals("0\n", outContent.toString());
    }
}