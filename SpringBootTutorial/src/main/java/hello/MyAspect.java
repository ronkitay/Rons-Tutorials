package hello;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.stereotype.Component;
import org.springframework.web.bind.annotation.RequestMapping;

/**
 * @author Ron Kitay
 * @since 28/10/15
 */
@Aspect
@Component
public class MyAspect {

    public MyAspect() {
        System.out.printf("Constructor");
    }

//    @Pointcut(value = "execution(* hello.SampleController.*(..))")
    @Pointcut(value = "execution(* hello..*.*(..))")
    public void anyControllerMethod() {}

//    @Around("anyControllerMethod() && @annotation(requestMapping)")
    @Around("anyControllerMethod()")
    public Object logTimeMethod(ProceedingJoinPoint joinPoint) throws Throwable {
        System.out.println("Hello trace!");
        return joinPoint.proceed();
    }
}
