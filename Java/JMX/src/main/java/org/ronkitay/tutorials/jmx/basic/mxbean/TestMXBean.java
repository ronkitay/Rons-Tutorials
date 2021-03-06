package org.ronkitay.tutorials.jmx.basic.mxbean;

/**
 * MXBean interface - allows to publish non standard objects like {@link SomeInnerInput}
 * Interface must end with "MXBean" to make it work
 *
 * @author Ron Kitay
 */
public interface TestMXBean {

    public void shutDown();

    public void sayHi();

    public String getRandomString();

    public void changeSomething(int ignored);

    public SomeInnerInput getSomethingPropeitry();

    public int doSomething(SomeInnerInput someInnerInput);
}
