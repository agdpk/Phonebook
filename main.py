# Открыть файл
# сохранить файл
# Создание контакта
# Изм контакт
# Найти контакт
# Удалить контакт
# показать контакт
# выход

def print_menu():
    print("1. Create contact")
    print("2. Change contact")
    print("3. Find contact")
    print("4. Delete contact")
    print("5. Show contacts")
    print("6. Add line")
    print("7. Exit")

def get_input_contact(file_name):
    information = list()
    information.append(input("Введите имя контакта: "))
    information.append(input("Введите номер контакта: "))
    information.append(input("Введите ник контакта: "))
    return information

def create_contact(file_name):
    contact = get_input_contact(file_name)
    with open(file_name, "a") as file:
        file.write(";".join(contact) + "\n")

def show_contacts(file_name):
    with open(file_name, "r") as file:
        x = 0
        for line in file:
            print(f"{str(x)};{line}", end="")
            x += 1

def change_contact(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    for line in lines:
        print(line, end="")
    id_for_change = int(input("Введите индекс контакта для изменения: "))
    if 0 <= id_for_change <= len(lines):
        contact = get_input_contact(file_name)
        contact[0] = str(id_for_change)
        contact = ";".join(contact) + "\n"
        lines[id_for_change] = contact

    with open(file_name, "w") as file:
        file.writelines(lines)

def find_contact(file_name):
    name = input("Введите имя человека: ")
    with open(file_name, "r") as file:
        lines = file.readlines()

    for line in lines:
        if name in line:
            print(line)

def delete_contact(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    show_contacts(file_name)

    id_for_change = int(input("Введите индекс контакта для удаления: "))
    if 0 <= id_for_change <= len(lines):
        del lines[id_for_change]

    with open(file_name, "w") as file:
        file.writelines(lines)

def select_files():
    print("Названия файлов contacts.txt и new.txt")
    source_file = input("Введите файл, из которого будет скопирована строка: ")
    target_file = input("Введите файл, в который скопировать строку: ")
    show_contacts(source_file)
    line_number = int(input("Введите индекс строки: "))
    add_line(source_file, target_file, line_number)
    print("Строка успешно добавлена!")
def add_line(file_name, new_file, line_number):
    with open(file_name, "r") as file:
        lines = file.readlines()

    with open(new_file, "a") as file:
        file.write(lines[line_number])



def main():
    file_name = "contacts.txt"
    while True:
        print_menu()
        input_number = int(input("Что вы выбираете? "))
        if input_number == 1:
            create_contact(file_name)
        elif input_number == 2:
            change_contact(file_name)
        elif input_number == 3:
            find_contact(file_name)
        elif input_number == 4:
            delete_contact(file_name)
        elif input_number == 5:
            show_contacts(file_name)
        elif input_number == 6:
            select_files()
        elif input_number == 7:
            break
        print("Телефонный справочник закрыт!")

if __name__ == '__main__':
    main()