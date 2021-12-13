numbers = [13,4,27,9,1994]

print("Format d'origine \n")
for num in numbers : print(num)

print("\nFormat croissant\n")
c_numbers = numbers.copy()
c_numbers.sort()
for num in c_numbers : print(num)

print("\nFormat d'origine\n")
for num in numbers : print(num)

print("\nFormat décroissant\n")
d_numbers = c_numbers.copy()
d_numbers.reverse()
for num in d_numbers : print(num)

print("\nFormat d'origine\n")
for num in numbers : print(num)

print("\nFormat inversé\n")
r_numbers = numbers.copy()
r_numbers.reverse()
for num in numbers : print(num)

print("\nFormat d'origine\n")
for num in numbers : print(num)

print("\nFormat croissant définitif\n")
numbers.sort()
for num in numbers : print(num)

print("\nFormat décroissant définitif\n")
numbers.reverse()
for num in numbers : print(num)
