package com.rsa.springcourse.webstore;

import java.util.List;

import com.rsa.springcourse.webstore.dao.IOrderDao;

public class Cart
{
	private Order order;
	private IOrderDao orderDao;
	
	public void setOrderDao(IOrderDao orderDao)
	{
		this.orderDao = orderDao;
		order = new Order();
	}

	public void add(Item item, int quantity)
	{
		order.add(item, quantity);
	}
	
	public Order checkOut()
	{
		orderDao.closeOrder(order);
		Order currentOrder = order;
		this.order = new Order();
		
		return currentOrder;
	}

	public List<OrderItem> getOrderItems()
	{
		return this.order.getOrderItems();
	}
	
	public double totalCost()
	{
		return this.order.calculateCost();
	}
}
