package org.ronkitay.tutorials.jmx.basic.meannotification;

import javax.management.MBeanServer;
import javax.management.ObjectName;
import java.lang.management.ManagementFactory;

/**
 * Based on: http://docs.oracle.com/javase/tutorial/jmx/notifs/index.html
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
        ObjectName name = new ObjectName("org.ronkitay.tutorials.jmx.basic.mbeannotification:type=SomeMBeanAlias");
        Test mbean = new Test();
        mbs.registerMBean(mbean, name);

        System.out.println("Waiting forever...");

        while (mbean.shouldShutDown() == false) {
            Thread.sleep(1000);
        }

        System.out.println("Got shutdown request");
    }
}
