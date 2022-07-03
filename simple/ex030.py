import time

t1 = time.time()

_ = [i*2 for i in range(99999999)]

t2 = time.time()

print(f"Temps d'exécution: {t2-t1}")