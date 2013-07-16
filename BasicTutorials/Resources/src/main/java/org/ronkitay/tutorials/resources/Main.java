package org.ronkitay.tutorials.resources;

import java.util.Locale;
import java.util.ResourceBundle;

public class Main
{

	/**
	 * @param args
	 */
	public static void main(String[] args)
	{
		defaultLocaleStrings();
		
		frenchStrings();
		
		germanStrings();
	}

	private static void germanStrings()
	{
		// There is no resource file for German, so it should take the default locale instead 
		ResourceBundle germanStrings = ResourceBundle.getBundle("org/ronkitay/tutorials/resources/default_strings", Locale.GERMAN);
		
		String mainString = germanStrings.getString("main");
		
		System.out.println("German string is <" + mainString + "> (should be the default locale)");
		
	}

	private static void frenchStrings()
	{
		ResourceBundle frenchStrings = ResourceBundle.getBundle("org/ronkitay/tutorials/resources/default_strings", Locale.FRANCE);
		
		String mainString = frenchStrings.getString("main");
		
		System.out.println("French string is <" + mainString + ">");
		
	}

	private static void defaultLocaleStrings()
	{
		ResourceBundle defaultStrings = ResourceBundle.getBundle("org/ronkitay/tutorials/resources/default_strings");
		
		String mainString = defaultStrings.getString("main");
		
		System.out.println("Default string is <" + mainString + "> (if the default is english it should say English)");
	}

}
