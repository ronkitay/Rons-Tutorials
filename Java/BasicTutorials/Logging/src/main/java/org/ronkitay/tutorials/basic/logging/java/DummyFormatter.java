package org.ronkitay.tutorials.basic.logging.java;

import java.util.logging.Formatter;
import java.util.logging.LogRecord;

public class DummyFormatter extends Formatter
{
	@Override
	public String format(LogRecord record)
	{
		return "[DUMMY FORMATTER] " + record.getLoggerName() + " - " + record.getMessage();
	}
}