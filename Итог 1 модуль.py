grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average1 = sum(grades[0]) / len(grades[0])
average2 = sum(grades[1]) / len(grades[1])
average3 = sum(grades[2]) / len(grades[2])
average4 = sum(grades[3]) / len(grades[3])
average5 = sum(grades[4]) / len(grades[4])
grades2 = [average1, average2, average3, average4, average5]
#print(grades2)
res = sorted(students)
#print(res)
res2 = zip(res,grades2)
Dic = dict(res2)
print(Dic)



