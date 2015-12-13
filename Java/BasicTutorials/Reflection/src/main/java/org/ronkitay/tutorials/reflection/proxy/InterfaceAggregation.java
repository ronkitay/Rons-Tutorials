package org.ronkitay.tutorials.reflection.proxy;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Proxy;

public class InterfaceAggregation
{

	/**
	 * @param args
	 */
	public static void main(String[] args)
	{
		IPerson person = new Person("luke");
		
		IAnimal animal = new Animal("lucky");
		
		IPlant plant = new Plant("Rose");
		
		Object aggregatedInterface = addInterface(IAnimal.class, animal, person);
		aggregatedInterface = addInterface(IPlant.class, plant, aggregatedInterface);
		
		if (aggregatedInterface instanceof IAnimal)
		{
			System.out.println("It is an animal!");
			IAnimal hiddenAnimal = (IAnimal)aggregatedInterface;
			System.out.println("Its name is <" + hiddenAnimal.getName() + ">");
		}

		if (aggregatedInterface instanceof IPerson)
		{
			System.out.println("It is a person!");
			System.out.println("His/Her name is <" + ((IPerson)aggregatedInterface).getName() + ">");
		}

		if (aggregatedInterface instanceof IPlant)
		{
			System.out.println("It is a plant!");
			System.out.println("It's type is <" + ((IPlant)aggregatedInterface).getType() + ">");
		}
		
		
	}
	
	public static Object addInterface(Class<?> newInterface, Object objectImplementingNewInterface, Object existingObject)
	{
		Class<?>[] existingInterfaces = existingObject.getClass().getInterfaces();
		Class<?>[] newInterfaces = new Class[existingInterfaces.length+1];
		System.arraycopy(existingInterfaces, 0, newInterfaces, 1, existingInterfaces.length);
		newInterfaces[0] = newInterface;
		
		InvocationHandler h = new InterfaceAggregator(newInterface, objectImplementingNewInterface, existingObject);
		Object proxy = Proxy.newProxyInstance(InterfaceAggregation.class.getClassLoader(), newInterfaces, h);
		
		return proxy;
	}

}
