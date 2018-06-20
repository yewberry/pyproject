import time

class Timeit:
	def __init__(self):
		self.ts = time.time()
	
	def start(self):
		self.ts = time.time()
	
	def end(self):
		te = time.time()
		secs = te - self.ts
		msecs = secs * 1000
		return msecs
	