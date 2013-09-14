package org.ronkitay.tutorials.reflection.proxy;

public class Person implements IPerson
{

	private String name;

	public Person(String name)
	{
		super();
		this.name = name;
	}

	@Override
	public String getName()
	{
		return this.name;
	}

}
