package org.ronkitay.tutorials.jmx.basic.mxbean;

import java.beans.ConstructorProperties;

/**
 * @author Ron Kitay
 * @since 06/01/2014
 */
public class SomeInnerInput {

    private String a;
    private int b;

    // The annotation allows the MXBean to be published correctly
    @ConstructorProperties({"a", "b"})
    public SomeInnerInput(String a, int b) {
        this.a = a;
        this.b = b;
    }

    public String getA() {
        return a;
    }

    public int getB() {
        return b;
    }
}
