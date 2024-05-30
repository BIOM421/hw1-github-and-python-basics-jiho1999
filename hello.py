def hello_world():
	return "Hello World!"

def hello_world_n(N):
	n_hello = ''
	for i in range (0, N):
		n_hello += "Hello World!"
		if i != N-1:
			n_hello += ' '
	return n_hello
