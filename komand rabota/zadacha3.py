main_list=[]
spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
# main_list = list(set(spisok_2)-set(spisok_1))
for i in spisok_2:
    if i not in spisok_1:
        main_list.append(i)
for i in spisok_1:
    if i not in spisok_2:
        main_list.append(i)

print(main_list)
