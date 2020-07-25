from difflib import *

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# abcdefghijklmnopqrstuvwxyz
cipher1 =   [[679, 1078, 198, 500, 303],
            [1122, 721, 208, 315, 530],
            [749, 1188, 218, 550, 333],
            [1232, 791, 228, 345, 580],
            [819, 1298, 238, 600, 363],
            [854, 528, 96, 240, 144]]

# abcdefghijklmnopqrstuvwxyp
cipher2 =   [[194, 686, 1089, 300, 505],
            [714, 206, 1144, 525, 318],
            [214, 756, 1199, 330, 555],
            [784, 226, 1254, 575, 348],
            [234, 826, 1309, 360, 605],
            [224, 336, 528, 144, 240]]

for i in range(len(cipher1)):
    print(similar(cipher1[i],cipher2[i])*100)

