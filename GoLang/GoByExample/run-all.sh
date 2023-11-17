#!/bin/sh

for dir in $(fd -t d  | sort -n); do 
	echo $dir; 
	cd $dir; 
	go run *.go; 
	cd ..; 
done
