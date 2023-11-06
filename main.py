def show_data(filename):
    print("\nПП | ФИО | Телефон")
    with open(filename, "r", encoding="utf-8") as data:
        print(data.read())
    print("")


def adding_contact(filename):
    with open(filename, "r", encoding="utf-8") as data:
        tel_file = data.read()
    num = len(tel_file.split("\n"))
    with open(filename, "a", encoding="utf-8") as data:
        fio = input("Введите ФИО: ")
        phone_number = input("Введите номер телефона: ")
        data.write(f"{num} | {fio} | {phone_number}\n")
        print(f"Добавлена запись: {num} | {fio} | {phone_number}\n")


def edit_contact(filename):
    print("\nПП | ФИО | Телефон")
    with open(filename, "r", encoding='utf-8') as data:
        tel_book = data.read()
    print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для редактирования: ")) - 1
    tel_book_lines = tel_book.split("\n")
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(" | ")
    fio = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    num = elements[0]
    if len(fio) == 0:
        fio = elements[1]
    if len(phone) == 0:
        phone = elements[2]
    edited_line = f"{num} | {fio} | {phone}"
    tel_book_lines[index_delete_data] = edited_line
    print(f"Запись - {edit_tel_book_lines}, изменена на - {edited_line}\n")
    with open(filename, "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))


def delete_contact(filename):
    print("\nПП | ФИО | Телефон")
    with open(filename, "r", encoding="utf-8") as data:
        tel_book = data.read()
        print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
    tel_book_lines = tel_book.split("\n")
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f"Удалена запись: {del_tel_book_lines}\n")
    with open(filename, "w", encoding='utf-8') as data:
        data.write("\n".join(tel_book_lines))


def copy_data(source_filename, destination_filename):
    try:
        with open(source_filename, "r", encoding="utf-8") as source_file:
            data_to_copy = source_file.read()

        with open(destination_filename, "a", encoding="utf-8") as destination_file:
            destination_file.write(data_to_copy)
            print(f"Data copied from {source_filename} to {destination_filename}")
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")


def main():
    my_choice = -1
    file_tel = "phonebook.txt"

    with open(file_tel, "a", encoding="utf-8") as file:
        file.write("")

    while my_choice != 0:
        print("Выберите одно из действий:")
        print("1 - Вывести инфо на экран")
        print("2 - Добавление контакта")
        print("3 - Изменение контакта")
        print("4 - Удаление контакта")
        print("5 - Копировать данные из файла")
        print("0 - Выход из программы")
        action = int(input("Действие: "))
        if action == 1:
            show_data(file_tel)
        elif action == 2:
            adding_contact(file_tel)
        elif action == 3:
            edit_contact(file_tel)
        elif action == 4:
            delete_contact(file_tel)
        elif action == 5:
            source_file = input("Введите имя файла, из которого хотите скопировать данные: ")
            destination_file = input("Введите имя файла, в который хотите скопировать данные: ")
            copy_data(source_file, destination_file)
        else:
            my_choice = 0

    print("До свидания")


if __name__ == "__main__":
    main()
