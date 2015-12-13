package org.ronkitay.tutorials.jmx.basic.client;

import javax.management.remote.JMXConnector;
import javax.management.remote.JMXConnectorFactory;
import javax.management.remote.JMXServiceURL;

/**
 * Based on: http://docs.oracle.com/javase/tutorial/jmx/remote/custom.html
 * @author Ron Kitay
 * @since 07/01/2014
 */
public class JMXClient {

    public static void main(String[] args) throws Exception{

        System.out.println("\nCreate an RMI connector client and connect it to the RMI connector server");
        JMXServiceURL url = new JMXServiceURL("service:jmx:rmi:///jndi/rmi://:9999/jmxrmi");
        JMXConnector jmxc = JMXConnectorFactory.connect(url, null);


    }
}
