package org.ronkitay.tutorials.jmx.basic.meannotification;

import javax.management.*;

/**
 * Getters are considered "Attributes"
 * Other methods are "Operations"
 *
 * Added a notification via {@link NotificationBroadcasterSupport}
 * @author Ron Kitay
 * @since 05/01/2014
 */
public class Test extends NotificationBroadcasterSupport implements TestMBean{

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

        // Send a notification when a something happens
        Notification n = new AttributeChangeNotification(this,
                0, System.currentTimeMillis(),
                "Something changed", "RandomString", "java.lang.String",
                "N/A", String.valueOf(ignored));      // TODO: The event details are not displayed in jConsole - need to figure out what I did wrong here

        sendNotification(n);

        System.out.println("Ignored the value <" + ignored + ">");
    }

    /**
     * Provide metadata about what types of notifications this MBean provides
     * @return
     */
    @Override
    public MBeanNotificationInfo[] getNotificationInfo() {

        String[] types = new String[]{AttributeChangeNotification.ATTRIBUTE_CHANGE};
        String name = AttributeChangeNotification.class.getName();
        String description = "An attribute of this MBean has changed";
        MBeanNotificationInfo info = new MBeanNotificationInfo(types, name, description);

        MBeanNotificationInfo[] notificationInfo = new MBeanNotificationInfo[1];
        notificationInfo[0] = info;
        return notificationInfo;
    }
}
