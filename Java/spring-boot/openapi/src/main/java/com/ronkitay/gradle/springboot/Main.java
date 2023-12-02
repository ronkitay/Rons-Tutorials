package com.ronkitay.gradle.springboot;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@ComponentScan(basePackages = {
		// "org.openapitools.configuration",
		"com.ronkitay.openapidemo.invoker",
		// "com.ronkitay.openapidemo.model",
		"com.ronkitay.gradle.springboot" })
public class Main {

	public static void main(String[] args) {
		SpringApplication.run(Main.class, args);
	}

}
