package com.rsa.springcourse.webstore.dao;

import java.util.LinkedList;
import java.util.List;

import com.rsa.springcourse.webstore.Order;

public class InMemoryOrderDao implements IOrderDao
{
	private List<Order> orders;
	
	public InMemoryOrderDao()
	{
		this.orders = new LinkedList<Order>();
	}
	
	@Override
	public void closeOrder(Order order)
	{
		this.orders.add(order);
	}

	@Override
	public List<Order> gretOrders()
	{
		return this.orders;
	}
}