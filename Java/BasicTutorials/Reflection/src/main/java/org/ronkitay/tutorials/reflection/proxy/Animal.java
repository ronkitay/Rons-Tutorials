package org.ronkitay.tutorials.reflection.proxy;

public class Animal implements IAnimal
{
	private String name;

	public Animal(String name)
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
