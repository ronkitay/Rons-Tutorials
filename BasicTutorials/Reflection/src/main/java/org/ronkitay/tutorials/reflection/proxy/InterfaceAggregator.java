package org.ronkitay.tutorials.reflection.proxy;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;

public class InterfaceAggregator implements InvocationHandler
{

	private Class<?> newInterface;
	private Object objectImplementingNewInterface;
	private Object existingObject;

	public InterfaceAggregator(Class<?> newInterface, Object objectImplementingNewInterface, Object existingObject)
	{
		this.newInterface = newInterface;
		this.objectImplementingNewInterface = objectImplementingNewInterface;
		this.existingObject = existingObject;
	}

	@Override
	public Object invoke(Object proxy, Method method, Object[] args) throws Throwable
	{
//		System.out.println("Method is <" + method.getDeclaringClass() +"." +method.getName() + ">");
//		System.out.println("newInterface is <" + newInterface.getName() +">");
		Object objectToUseForExecution = null;
		if (method.getDeclaringClass().equals(newInterface))
		{
			objectToUseForExecution = objectImplementingNewInterface;
		}
		else
		{
			objectToUseForExecution = existingObject;
		}

//		System.out.println("About to use <" + objectToUseForExecution.getClass() +"> for handling of the <" + method.getName() +"> method");
		Object result = method.invoke(objectToUseForExecution, args);
		return result;
	}

}
