import threading

threads = []
numThreads = 50

def funcToThread():
	while true:
		print('Threading')

for i in range(numThreads):
	t  = threading.Thread(target = funcToThread)
	t.daemon = True
	threads.append(t)

for i in range(numThreads):
	threads[i].start()

for i in range(numThreads):
	threads[i].join()