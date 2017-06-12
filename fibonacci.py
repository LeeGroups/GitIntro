def fib(N):
	if N <=1:
		return N
	else:
		return fib(N-1)+fib(N-2)

if __name__ == "__main__":
	print("Fibo(5)",fib(5))