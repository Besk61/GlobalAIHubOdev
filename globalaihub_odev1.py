"""Bora Eskicioğlu"""

odd_list=[1,3,5,7,9,11,13,15,17,19]
even_list=[0,2,4,6,8,10,12,14,16,18]
sum_list=(odd_list+even_list)
i=0
while i<len(sum_list):
    sum_list[i]=2*sum_list[i]
    i=i+1

for j in sum_list:
    print(type(j))

