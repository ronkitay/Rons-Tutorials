package org.ronkitay.tutorials.jmx.basic.mbean;

import javax.management.*;
import java.lang.management.ManagementFactory;

/**
 * Based on: http://docs.oracle.com/javase/tutorial/jmx/mbeans/standard.html
 * @author Ron Kitay
 * @since 05/01/2014
 */
public class JmxAgent {

    /**
     * Run this and connect to the process using jconsole
     * @param args
     * @throws Exception
     */
    public static void main(String[] args) throws Exception {
        MBeanServer mbs = ManagementFactory.getPlatformMBeanServer();
        ObjectName name = new ObjectName("org.ronkitay.tutorials.jmx.basic.mbean:type=Test");
        Test mbean = new Test();
        mbs.registerMBean(mbean, name);

        System.out.println("Waiting forever...");

        while (mbean.shouldShutDown() == false) {
            Thread.sleep(1000);
        }

        System.out.println("Got shutdown request");
    }
}
