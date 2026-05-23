import json
import os

BOOKS_FILE = "books.json"

def load_books() -> list:
    if not os.path.exists(BOOKS_FILE):
        return []

    with open(BOOKS_FILE, "r", encoding="utf-8") as save_file:
        return json.load(save_file)

def save_books(books : list):
    with open(BOOKS_FILE, "w", encoding="utf-8") as save_file:
        json.dump(books, save_file, indent=4, ensure_ascii=False)

def add_book(books : list):
    print()

    author = input("Введите автора: ")
    name = input("Ввведите название: ")

    for book in books:
        if book["author"] == author and book["name"] == name:
            print("\nКнига с тем же автором и названием уже существует!")
            return

    rate = input("Введите оценку: ")

    if not rate.isnumeric():
        print("\nВведите число от 1 до 5!")
        return

    rate = int(rate)
    if not (1 <= rate <= 5):
        print("\nВведите число от 1 до 5!")
        return

    date = input("Введите дату: ")

    books.append({
        "author" : author,
        "name" : name,
        "rate" : rate,
        "date" : date,
    })

def main():
    books = load_books()

    while True:
        print("\n1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Средняя оценка")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")

        choice = input("Выберите действие: ")

        match choice:
            case "1":
                add_book(books)

            case "2":
                print("В разработке")

            case "3":
                print("В разработке")

            case "4":
                print("В разработке")

            case "5":
                print("В разработке")

            case "6":
                save_books(books)
                print("Выход...")
                break

            case _:
                print("Неверный выбор!")

if __name__ == "__main__":
    main()