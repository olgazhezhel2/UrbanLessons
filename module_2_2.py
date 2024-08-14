first = 343
second = 548
third = 343
if first == second or first == third or second == third:
    print(2)
elif first == second and second == third:
    print(3)
elif first != second and first != third and second != third:
    print(0)