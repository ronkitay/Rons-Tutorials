package com.rsa.springcourse.webstore;

public class Item
{
	private int id;
	private String description;
	private double price;
	
	public Item(int id, String description, double price)
	{
		super();
		this.id = id;
		this.description = description;
		this.price = price;
	}
	
	public int getId()
	{
		return id;
	}
	public String getDescription()
	{
		return description;
	}

	public double getPrice()
	{
		return price;
	}
}
