#  Write a program to find the largest and smallest element in a list without using built-inmin()/max()

l = [10 , 2 , 15 , 56 , 13 , 48]

largest=l[0]
smallest=l[0]

for i in l :
    if i >largest:
        largest= i
    if i<smallest:
        smallest=i

print(f"{largest} is largest no.")
print(f"{smallest} is smallest no.")