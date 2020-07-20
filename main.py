import sympy
import random
import time

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

def mod_inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  
    else:
        return x % m

plaintext = input('Enter a Message : ')

m = int(input('Enter a positive integer m : '))

ascii_values = []
for c in plaintext:
    ascii_values.append(ord(c))
print('ASCII values : ',ascii_values)

q = sympy.prime(10*len(plaintext)+1)
print('q = ',q)

prime_list = []
count = 0
temp = []
while True:
    if count == len(plaintext):
        break
    p = sympy.prime(random.randint(1,10*len(plaintext)))
    if p not in prime_list and mod_inverse(p,q**m)!=None:
        prime_list.append(p)
        count += 1
print('Primes : ',prime_list)

t1 = time.time()

cipher = []
for c in range(len(plaintext)):
    cipher.append((ord(plaintext[c])*prime_list[c]) % (q**m))
print('Encrypted : ',cipher)

lst = []
for k in range(len(cipher)):
    lst.append((cipher[k] * mod_inverse(prime_list[k],q**m))%q**m)
print('Decrypted : ' + ''.join(map(lambda x: chr(x), lst)))

t2 = time.time()
print('Runtime : ',t2-t1)