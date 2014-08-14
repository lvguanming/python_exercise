# -*- coding:utf-8 -*-
def fib(n):
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result

f100 = fib(n=100)
print(f100)