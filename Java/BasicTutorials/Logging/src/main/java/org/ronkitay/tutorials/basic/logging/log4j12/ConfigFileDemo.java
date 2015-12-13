package org.ronkitay.tutorials.basic.logging.log4j12;

import java.io.File;

import org.apache.log4j.Level;
import org.apache.log4j.Logger;
import org.apache.log4j.MDC;
import org.apache.log4j.NDC;


public class ConfigFileDemo
{
	/**
	 * Runs several prints with several loggers to illustrate basic logging abilities
	 */
	public static void main(String[] args)
	{
		String log4jConfigPath = System.getProperty("log4j.configuration");
		System.out.println("Log4j configuration is defined under<" + log4jConfigPath + ">");
		System.out.println("Log4j configuration is physically located at <" + getRealPath(log4jConfigPath) + ">");
		System.out.println("A1 Log file should be written to <" + System.getProperty("java.io.tmpdir") + "ConfigFileDemo.log" +">");
		System.out.println("A2 Log file should be written to <" + System.getProperty("user.dir") + File.separator + "ConfigFileDemo.DEBUG.log" +">\n");

		MDC.put("myGlobalContext", "some very important context");
		Logger rootLogger = Logger.getRootLogger();
		print(rootLogger, true, true, false, false, false, false);

		// demoLogger - not directly defined, it inherits from the org.ronkitay.tutorials.basic.logging.log4j logger
		Logger demoLogger = Logger.getLogger(ConfigFileDemo.class.getName());
		print(demoLogger, true, true, true, true, false, false);
		MDC.remove("myGlobalContext");

		Logger debugLogger = Logger.getLogger(ConfigFileDemo.class.getPackage().getName() + ".debug");
		print(debugLogger, true, true, true, true, true, false);
	}
	

	private static void print(Logger logger, boolean fatal, boolean error, boolean warning, boolean info, boolean debug, boolean trace)
	{
		System.out.println("PRINT START for <" + logger.getName() + ">");
		
		log(logger, Level.FATAL, fatal);
		log(logger, Level.ERROR, error);
		log(logger, Level.WARN, warning);
		log(logger, Level.INFO, info);
		log(logger, Level.DEBUG, debug);
		log(logger, Level.TRACE, trace);
		
		waitForLogging();
		System.out.println("PRINT END for <" + logger.getName() + ">");
		System.out.println("");
	}
	
	private static void log(Logger logger, Level level, boolean expectThisLevel)
	{
		String loggerName = logger.getName();

		String message = loggerName + ": Logging a <" + level.toString() + "> message";
		
		if (expectThisLevel)
		{
			if (logger.isEnabledFor(level))
			{
				logger.log(level, message);
			}
			else
			{
				System.err.printf("Logger <%s> should have been enabled for level <%s> but was not!\n", loggerName, level.toString());
			}
		}
		else
		{
			if (logger.isEnabledFor(level))
			{
				System.err.printf("Logger <%s> should NOT have been enabled for level <%s> but it IS!\n", loggerName, level.toString());
			}
		}
	}

	private static void waitForLogging()
	{
		try
		{
			Thread.sleep(1);
		}
		catch (InterruptedException e)
		{
			e.printStackTrace();
		}
	}

	private static String getRealPath(String log4jConfigPath)
	{
		return ConfigFileDemo.class.getClassLoader().getResource(log4jConfigPath).getPath();
	}
}