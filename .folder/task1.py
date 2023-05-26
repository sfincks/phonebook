file1 = 'numbers.txt'
file2 = 'numbers.scv'

def get_info():
    info = []
    lastname = input("Введите фамилию: ")
    info.append(lastname)
    firstname = input("Введите имя: ")
    info.append(firstname)
    phonenumber = ""
    valid = False
    while not valid:
        try:
            phonenumber = input("Введите номер телефона: ")
            if len(phonenumber) !=11:
                print("В номере дожно быть 11 цифр")
            else:
                phonenumber = int(phonenumber)
                valid = True
        except:
            print("В номере телефона дожны быть только цифры")
    info.append(phonenumber)
    return info

def writing_txt(info):
    file = 'numbers.txt'      
    with open (file,'a', encoding='utf-8') as data:
        data.write(f'\nФамилия: {info[0]}\nИмя: {info[1]}\nНомер телефона: {info[2]}\n')        

def writing_scv(info):
    file = 'numbers.scv'      
    with open (file,'a', encoding='utf-8') as data:
        data.write(f'{info[0]},{info[1]},{info[2]}\n') 

def reading_txt():
    file = 'numbers.txt'    
    with open (file,'r', encoding='utf-8') as file1:
        read = file1.read()
        print (read)

def reading_scv():
    data = []
    fields = ["Фамилия","Имя","Номер телефона"]
    with open('numbers.scv','r', encoding='utf-8') as file2:
        for line in file2:
            record = dict(zip(fields,line.strip().split(',')))
            data.append(record)
    return print(data)
            
def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Отобразить SCV файл\n"
          "6. Закончить работу\n")
    return int(input("Введите номер пункта меню: "))

def phonebook():
    choice = show_menu()    
    while(choice !=6):
        if (choice == 1):
            reading_txt()
        elif(choice == 2):
            name = input("\nВведите фамилию: ")
            next((x for x in file1 if x["Фамилия"]== name), "Не найдено")
        elif(choice == 3):
            num = int(input("\nВведите фамилию: "))
            next((x for x in file2 if x["Номер телефона"]== name), "Не найдено")
        elif(choice == 4):
            info = get_info()
            writing_scv(info)
            writing_txt(info)
        elif(choice == 5):
            reading_scv()
        choice = show_menu()
        
phonebook()
            