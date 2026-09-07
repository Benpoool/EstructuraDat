import time

inicio = time.time()
def factorial(n):
        if(n==0):
            return 1;
        else:
            return n*factorial(n-1)
        
a = 996
print(factorial(a))

time.sleep(1)
fin = time.time()

print(f"Tiempo: {fin - inicio} segundos")