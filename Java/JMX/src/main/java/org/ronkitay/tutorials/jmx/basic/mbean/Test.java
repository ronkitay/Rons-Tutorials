package org.ronkitay.tutorials.jmx.basic.mbean;

/**
 * Getters are considered "Attributes"
 * Other methods are "Operations"
 * @author Ron Kitay
 * @since 05/01/2014
 */
public class Test implements TestMBean {

    private volatile boolean shouldShutDown;

    public boolean shouldShutDown() {
        return shouldShutDown;
    }

    @Override
    public void shutDown() {
        System.out.println("Got shutdown request");
        this.shouldShutDown = true;
    }

    @Override
    public void sayHi() {
        System.out.println("Saying HI from MBean!");
    }

    @Override
    public String getRandomString() {
        return "Not so random ...";
    }

    @Override
    public void changeSomething(int ignored) {
        System.out.println("Ignored the value <" + ignored + ">");
    }

}
