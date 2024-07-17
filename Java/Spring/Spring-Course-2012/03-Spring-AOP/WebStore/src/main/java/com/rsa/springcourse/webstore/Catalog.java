package com.rsa.springcourse.webstore;

import java.util.List;

import com.rsa.springcourse.webstore.dao.IItemDao;

public class Catalog
{
	private IItemDao itemDao;
	private List<Item> items;
	
	public void setItemDao(IItemDao itemDao)
	{
		this.itemDao = itemDao;
	}

	public void loadItems()
	{
		items = itemDao.getItems();
	}
	
	public List<Item> getItems()
	{
		return this.items;
	}
}
