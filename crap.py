# def Rotate(lists, num): # Right is default
#     output_list = []       
#     for item in range(len(lists) - num, len(lists)): 
#         output_list.append(lists[item])       
#     for item in range(0, len(lists) - num):  
#         output_list.append(lists[item]) 
#     return output_list 

# def evolve_primes_list(sample,shift_factor):
#     right = sample[len(sample)//2+1:]
#     left = sample[:len(sample)//2]
#     rotated_right = Rotate(right,num=shift_factor%len(right))
#     rotated_left = Rotate(left,num=len(left)-(shift_factor%len(left)))
#     rotated_left.append(sample[len(sample)//2])
#     final = rotated_left + rotated_right
#     return final

# sample = [7, 2, 5, 11, 3, 17, 13, 19]

# # n = len(sample)
# n = 10
# for shift_factor in range(n):
#     temp = evolve_primes_list(sample,shift_factor%len(sample))
#     if shift_factor > n//2:
#         temp = temp[:n//2+shift_factor]
#     print(temp)

import numpy as np

n = int(input("Enter a number: "))
def calculate_blocksize(n):
    num = int(np.sqrt(n))
    if num**2<n**2:
        return int(np.sqrt(num**2))
    else:
        return(-1)
print(calculate_blocksize(n))