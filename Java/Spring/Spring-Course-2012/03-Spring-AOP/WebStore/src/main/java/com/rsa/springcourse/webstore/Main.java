package com.rsa.springcourse.webstore;

import java.util.List;

public class Main
{

	/**
	 * @param args
	 */
	public static void main(String[] args)
	{
		Store store = Store.INSTANCE;
		
		Catalog catalog = store.getCatalog();
		Cart cart1 = store.createCart();
		Cart cart2 = store.createCart();
		
		List<Item> items = catalog.getItems();
		int quantity = 1;
		for (Item item : items)
		{
			cart1.add(item, quantity++);
		}
		
		System.out.println("\nBefore check out - cart #1 is:");
		printCart(cart1);
		System.out.println("Cart #1 cost: <" + cart1.totalCost() + ">");
		
		System.out.println("\nBefore check out - cart #2 is:");
		printCart(cart2);
		System.out.println("Cart #2 cost: <" + cart2.totalCost() + ">");
		
		Order order = cart1.checkOut();
		System.out.println("Performed check out - current order is:");
		printOrder(order);
		
		System.out.println("\nAfter check out - cart #1 is:");
		printCart(cart1);
	}

	private static void printOrder(Order order)
	{
		List<OrderItem> orderItems = order.getOrderItems();
		for (OrderItem orderItem : orderItems)
		{
			System.out.printf("Item <%s>, Quantity <%d>, Total Price <%d>\n", 
					orderItem.getItem().getDescription(),
					orderItem.getQuantity(),
					(int)(orderItem.getQuantity()*orderItem.getItem().getPrice()));
		}
	}

	private static void printCart(Cart cart1)
	{
		List<OrderItem> itemsAfterCheckout = cart1.getOrderItems();
		for (OrderItem orderItem : itemsAfterCheckout)
		{
			System.out.printf("Item <%s>, Quantity <%d>\n", 
					orderItem.getItem().getDescription(),
					orderItem.getQuantity());
		}
	}

}
