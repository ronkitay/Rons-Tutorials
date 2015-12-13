package hello;

import java.util.HashSet;
import java.util.Set;

/**
 * @author Ron Kitay
 * @since 25/11/15
 */
public interface Parameters {
    String KUKU_PARAM = "kuku";
    String KUKU2_PARAM = "kuk2u";

    enum Valid {

        KUKU(KUKU_PARAM);

        private final String name;

        Valid(String name) {
            this.name = name;
        }

        private static Set<String> validNames;

        static {
            Valid.validNames = new HashSet<String>();
            for (Valid parameter : Valid.values()) {
                Valid.validNames.add(parameter.name);
            }
        }

        public static boolean isValid(String parameterName) {
            return validNames.contains(parameterName);
        }

    }
}
