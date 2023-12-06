import multiprocessing
import os

def produzJobs(jobs):
	for i in range(100001,999999, 2):
		jobs.put(i) 
	for i in range(os.cpu_count()):
		jobs.put(None) 

def primo(jobs, results):
	while True:
		n = jobs.get()
		if n is None:
			jobs.task_done()
			break
		p = 1
		for i in range(3, int(n**0.5) + 1, 2):
			if n % i == 0:
				p = 0
		if p:
			results.put(n)
		jobs.task_done()

jobs = multiprocessing.JoinableQueue()
results = multiprocessing.JoinableQueue()
processos = []

produtor = multiprocessing.Process(target=produzJobs,args=(jobs,))  
produtor.start()

processos.append(produtor)

for _ in range(os.cpu_count()):
	worker = multiprocessing.Process(target=primo, args=(jobs,results))
	worker.start()

jobs.join()

print("TODOS OS JOBS FORAM PROCESSADOS!")

print("== RESULTADOS OBTIDOS ==")
	
t = results.qsize()

print(f"Existem {t} números primos com 6 dígitos!")

for i in range(t):
	n = results.get()
	print(f"Primo: {n}")
	results.task_done()
