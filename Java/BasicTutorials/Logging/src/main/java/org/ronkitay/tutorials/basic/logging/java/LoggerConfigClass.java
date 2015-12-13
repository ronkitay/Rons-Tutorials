package org.ronkitay.tutorials.basic.logging.java;

import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.net.URL;
import java.util.logging.LogManager;

/**
 * Class that loads logging configurations - this is just an example of how to use it - currently it loads
 * the exact same configuration file like the {@link ConfigFileDemo} does.
 * @author Ron Kitay
 *
 */
public class LoggerConfigClass
{
	/**
	 * Constructor - does the loading and should be discarded
	 * @throws Exception In case of any problems
	 */
	public LoggerConfigClass() throws Exception
	{
		URL resource = ConfigClassDemo.class.getResource("logging.properties");
		InputStream stream = new FileInputStream(new File(resource.toURI()));
		LogManager.getLogManager().readConfiguration(stream);
	}
}