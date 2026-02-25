# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt
# from pathlib import Path

# Здесь пишем код
path = open(r'C:\Users\user\project_auto\9_lection\test_file\task1_data.txt', mode='r', encoding='utf-8')
f_1 = path.readlines()
# print(f_1)

list_new = f_1.copy()
list_new2 = []
list_3 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_new3 = []
for i in range(len(list_new)):
    for j in range(len(list_new[i])):
        if list_new[i][j] in list_3:
            continue
        else:
            list_new2.append(list_new[i][j])
# print (list_new2)
j = ''.join(list_new2)

# print(j)
file = open(r'C:\Users\user\project_auto\9_lection\test_file\task1_answer.txt', mode='w', encoding='utf-8')
file.write(j)
file.seek(0)
file.close()
path.close()

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
