import os

#1
def list_content(path):
    all_items = os.listdir(path)  #Используется os.listdir(path), чтобы получить список всех элементов

    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))] #проверяем, является ли элемент папкой с помощью os.path.isdir(os.path.join(path, item))
    
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))] #проверяем os.path.isfile(), чтобы выбрать только файлы

    print("All elements:", all_items)
    print("Directories:", directories)
    print("Files:", files)

path = "." #текущая директория
list_content(path) #выполняет весь процесс


# #2
print('Exist:', os.access(path, os.F_OK))       #Проверяет, существует ли путь
print('Readable:', os.access(path, os.R_OK))    #Проверяет, можно ли читать файл или директорию.
print('Writable:', os.access(path, os.W_OK))    #Проверяет, можно ли записывать в файл или директорию.
print('Executable:', os.access(path, os.X_OK))  #Проверяет, можно ли выполнить файл


#3
path = input("=")
if os.path.exists(path):
    print(os.path.dirname(path)) #возвращает папку, в которой находится файл/каталог
    print(os.path.basename(path)) #возвращает имя файла или папки
else:
    print("path does not exist") #eсли путь не существует
    

#4
cnt = 0
with open('4tasks.txt', 'r', encoding='utf-8') as f:
    for _ in f: #Проходим по каждой строке, _ используется вместо переменной, так как сам текст строки не нужен
        cnt+=1
print(cnt)


#5
lst = [1,2,3,4,5,6,7,8]
with open('newfile.txt', 'w') as f:  #Если файла нет, он создастся автоматически
    for i in lst:                    #Проходим циклом по всем числам в lst
        f.write(str(i) + '\n')       #str(i) — Число преобразуется в строку


#6
for i in range(65, 91):
    with open(f'{chr(i)}.txt', 'w') as f: # f'{chr(i)}.txt' — Создает имя файла
        f.write(" ")


#7
with open('dir-and-files.txt', 'r') as rd, open('newfile.txt', 'w') as wt:
    wt.write(rd.read()) #wt.write(...) — Записывает это содержимое в newfile.txt, rd.read() — Читает всё содержимое как одну строку


#8
df = 'A.txt'
if os.path.exists(df):
    if os.access(df, os.F_OK):
        os.remove(df)
    else:
        print("Permision denied")
else:
    print("does not exist")