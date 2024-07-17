package com.rsa.springcourse.webstore;

import java.util.LinkedList;
import java.util.List;

public class Order
{
	private List<OrderItem> orderItems;
	
	public Order()
	{
		this.orderItems = new LinkedList<OrderItem>();
	}
	
	void add(Item item, int quantity)
	{
		OrderItem orderItem = new OrderItem(item, quantity);
		
		orderItems.add(orderItem);
	}
	
	public List<OrderItem> getOrderItems()
	{
		return this.orderItems;
	}
	
	public double calculateCost()
	{
		double sum = 0d;
		for (OrderItem orderItem : this.orderItems)
		{
			sum += orderItem.getQuantity()*orderItem.getItem().getPrice();
		}
		return sum;
	}

}
