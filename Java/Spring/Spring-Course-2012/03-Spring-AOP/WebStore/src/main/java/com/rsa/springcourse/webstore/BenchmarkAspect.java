package com.rsa.springcourse.webstore;

import java.util.Arrays;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;

@Aspect
public class BenchmarkAspect
{
	@Around("execution(* com.rsa.springcourse.webstore..*.*(..))")
	public Object measureTime(ProceedingJoinPoint pjp) throws Throwable
	{
		long startTime = System.nanoTime();
		try
		{
			return pjp.proceed();
		}
		finally
		{
			long endTime = System.nanoTime();
			Exception ex = new Exception();
			ex.fillInStackTrace();
			StackTraceElement caller = ex.getStackTrace()[13];
			String callerName = caller.getClassName() + "." + caller.getMethodName() + "(" + caller.getLineNumber() + ")";
			System.out.printf("Method <%s(%s)> took <%d> nano seconds (<%d>ms).\n\t->Method was called by <%s>.\n\n", pjp.getSignature().getName(), Arrays.toString(pjp.getArgs()), endTime-startTime, (endTime-startTime)/1000000, callerName);
		}
	}

}
