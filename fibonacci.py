def fib(N):
	if N <=1:
		return N
	else:
		n=1
		m1=0
		m2=1
		m3=1
		while n != N:
			m1 = m2
			m2 = m3
			m3 = m1+m2
			n+=1
		return m3

if __name__ == "__main__":
	print("Fibo(5)",fib(5))