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

def remove_book(books : list):
    print()

    if not books:
        print("Библиотека пустая!")
        return

    print("Доступные книги: ")

    for index, book in enumerate(books):
        print(f"{index}. {book["name"]}")

    print()

    user_book_id = input("Введите индекс книги: ")

    if not user_book_id.isnumeric():
        print("Введите число!")
        return

    user_book_id = int(user_book_id)

    if user_book_id >= len(books):
        print("Введите правильный индекс!")
        return

    books.pop(user_book_id)

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
                print("В разработке")

            case "2":
                print("В разработке")

            case "3":
                print("В разработке")

            case "4":
                print("В разработке")

            case "5":
                remove_book(books)

            case "6":
                save_books(books)
                print("Выход...")
                break

            case _:
                print("Неверный выбор!")

if __name__ == "__main__":
    main()