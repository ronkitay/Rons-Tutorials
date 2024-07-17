package com.rsa.springcourse.webstore.dao;

import java.util.List;

import com.rsa.springcourse.webstore.Order;

public interface IOrderDao
{
	public void closeOrder(Order order);
	
	public List<Order> gretOrders();
}
