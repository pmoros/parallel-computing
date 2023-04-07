package co.edu.unal.paralela;

import org.junit.Test;
import static org.junit.Assert.*;

public class SetupTest {

    @Test
    public void shouldSetUpTest() {
        final int resultado = Setup.setup(42);
        assertEquals(42, resultado);
    }
}
