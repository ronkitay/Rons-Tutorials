package hello;

import java.lang.reflect.Field;

import static org.junit.Assert.*;

/**
 * @author Ron Kitay
 * @since 25/11/15
 */
public class ParametersTest {

    @org.junit.Test
    public void test_AllConstantsHaveEnums() throws IllegalAccessException {

        final Field[] declaredFields = Parameters.class.getDeclaredFields();

        for (Field declaredField : declaredFields) {
            String constantValue = (String) declaredField.get(Parameters.class);
            assertTrue("<" + declaredField.getName() + "> is not valid", Parameters.Valid.isValid(constantValue));
        }

    }

}