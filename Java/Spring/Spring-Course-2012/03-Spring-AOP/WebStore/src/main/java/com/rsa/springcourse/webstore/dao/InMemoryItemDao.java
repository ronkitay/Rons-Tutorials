package com.rsa.springcourse.webstore.dao;

import java.util.LinkedList;
import java.util.List;

import com.rsa.springcourse.webstore.Item;

public class InMemoryItemDao implements IItemDao
{
	private List<Item> items;
	
	public InMemoryItemDao()
	{
		this.items = new LinkedList<Item>();
		
		items.add(new Item(1, "IPhone", 10d));
		items.add(new Item(2, "IPad", 20d));
		items.add(new Item(3, "IMac", 30d));
	}

	@Override
	public List<Item> getItems()
	{
		return this.items;
	}
}