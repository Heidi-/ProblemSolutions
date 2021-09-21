import math

def f_i(i):
	return math.floor(math.log2(i))

def lead_term(i, fi):
	last_pow = 2**fi
	return (i-last_pow + 1) * last_pow

def calc(n):
	fi = f_i(n)
	val = lead_term(n, fi)
	for i in range(0, fi):
		val += (2**i)**2
	return val * 10 + n

def lin_calc(n):
	fi = f_i(n)
	valsum = 4*2**(fi) - 4
	return (lead_term(n, fi) + valsum) * 10 + n

def g_n(n, fn):
	return (2**(2*fn) - 1) / 3

def c_n(n, fn):
	return g_n(n, fn) +  (n - 2**fn + 1)*2**fn

def s_n(n):
	fn = f_i(n)
	return n + 10 * c_n(n, fn)

def pat_n(n):
	alpha = f_i(n)
	sm = 0
	for j in range(0, alpha):
		sm += 4**j
	sm += (n + 1 - 2**alpha) * 2**alpha
	return sm * 10 + n
