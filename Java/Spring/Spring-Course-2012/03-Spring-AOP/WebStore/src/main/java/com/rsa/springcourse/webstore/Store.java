package com.rsa.springcourse.webstore;

import org.springframework.context.support.ClassPathXmlApplicationContext;

public enum Store 
{
	INSTANCE;
	
	private Catalog catalog;
	private ClassPathXmlApplicationContext factory;
	
	private Store()
	{
		this.factory = new ClassPathXmlApplicationContext("/META-INF/spring/store-context.xml");
		this.catalog = factory.getBean(Catalog.class);
	}
	
	public Catalog getCatalog()
	{
		return catalog;
	}

	public Cart createCart()
	{
		return this.factory.getBean(Cart.class);
	}

}
