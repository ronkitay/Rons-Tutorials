package org.ronkitay.tutorials.basic.logging.java;

import java.io.File;
import java.util.logging.Level;
import java.util.logging.LogManager;
import java.util.logging.Logger;

public class ConfigClassDemo
{
	/**
	 * Runs several prints with several loggers to illustrate basic logging abilities
	 * @throws Exception if "LogManager.getLogManager().readConfiguration()" fails
	 */
	public static void main(String[] args) throws Exception
	{
		System.setProperty("java.util.logging.config.class", LoggerConfigClass.class.getName());
		LogManager.getLogManager().readConfiguration(); // Not needed normally - but needed since we define the system property at this phase
		
		System.out.println("Log file should be written to <" + System.getProperty("java.io.tmpdir") + File.separator + "ConfigFileDemo_0.log" +">\n");
		
		// Logs SEVERE messages only
		Logger rootLogger = Logger.getLogger("");
		print(rootLogger, true, false, false, false, false, false, false);
		
		// demoLogger - not directly defined, it inherits from the org.ronkitay.tutorials.basic.logging.java logger
		Logger demoLogger = Logger.getLogger(ConfigFileDemo.class.getName());
		print(demoLogger, true, true, false, false, false, false, false);
		
		String packageName = ConfigFileDemo.class.getPackage().getName();
		
		Logger fineLogger = Logger.getLogger(packageName + ".debug1");
		print(fineLogger, true, true, true, true, true, false, false);
		
		Logger finerLogger = Logger.getLogger(packageName + ".debug2");
		print(finerLogger, true, true, true, true, true, true, false);
		
		Logger finestLogger = Logger.getLogger(packageName + ".debug3");
		print(finestLogger, true, true, true, true, true, true, true);
	}
	
	private static void print(Logger logger, boolean severe, boolean warning, boolean info, boolean config, boolean fine, boolean finer, boolean finest)
	{
		String loggerName = logger.getName();
		if ("".equals(loggerName))
		{
			loggerName = "ROOT";
		}
		System.out.println("PRINT START for <" + loggerName + ">");

		log(logger, Level.SEVERE, severe);
		log(logger, Level.WARNING, warning);
		log(logger, Level.INFO, info);
		log(logger, Level.CONFIG, config);
		log(logger, Level.FINE, fine);
		log(logger, Level.FINER, finer);
		log(logger, Level.FINEST, finest);

		waitForLogging();
		System.out.println("PRINT END for <" + loggerName + ">");
		System.out.println("");
	}
	
	private static void log(Logger logger, Level level, boolean expectThisLevel)
	{
		String loggerName = logger.getName();
		if ("".equals(loggerName))
		{
			loggerName = "ROOT";
		}

		String message = loggerName + ": Logging a <" + level.toString() + "> message";
		
		if (expectThisLevel)
		{
			if (logger.isLoggable(level))
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
			if (logger.isLoggable(level))
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
}
