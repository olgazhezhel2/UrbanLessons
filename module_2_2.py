first = 343
second = 548
third = 343
if first != second and first != third and second != third:
    print(0)
elif first == second or first == third or second == third:
    print(2)
elif first == second and second == third and first == third:
    print(3)
