package org.ronkitay.tutorials.jmx.basic.mbean;

import org.ronkitay.tutorials.jmx.basic.mxbean.SomeInnerInput;

/**
 * Interface must end with "MBean" to make it work
 * @author Ron Kitay
 */
public interface TestMBean {

    public void shutDown();

    public void sayHi();

    public String getRandomString();

    public void changeSomething(int ignored);
}
