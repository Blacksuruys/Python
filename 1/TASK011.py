#    Напишите программу для печати всех уникальных значений в словаре.
# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ": "S009"}, {"VIII": "S007"}]



list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ": "S009"}, {"VIII": "S007"}]
list_2=set()
for item in list_1:
   for v in item.values():
      list_2.add(v)
print(list_2)

list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ": "S009"}, {"VIII": "S007"}]
print(set(v for i in range(len(list_1)) for (k,v) in list_1[i].items()))