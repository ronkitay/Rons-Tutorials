package org.ronkitay.tutorials.reflection.proxy;

public class Plant implements IPlant
{

	private String type;

	public Plant(String type)
	{
		super();
		this.type = type;
	}

	@Override
	public String getType()
	{
		return this.type;
	}

}
