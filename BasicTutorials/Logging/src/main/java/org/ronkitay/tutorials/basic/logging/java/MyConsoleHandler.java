package org.ronkitay.tutorials.basic.logging.java;

import java.util.logging.LogRecord;
import java.util.logging.StreamHandler;

public class MyConsoleHandler extends StreamHandler
{
	public MyConsoleHandler()
	{
		setOutputStream(System.out);
	}

	public void publish(LogRecord record)
	{
		super.publish(record);
		flush();
	}

	public void close()
	{
		flush();
	}
}
