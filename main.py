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

def print_books(books : list):
    print()

    for book in books:
        print(f"'{book["name"]}'")
        print(f"    Автор:  {book["author"]}")
        print(f"    Дата:  {book["date"]}")
        print(f"    оценка:  {book["rate"]}")

def calculate_average_rating(books : list):
    print()

    if not books:
        print("Библиотека пустая!")
        return

    rating_len = len(books)
    rating_sum = sum([book["rate"] for book in books])

    average_rating = rating_sum / rating_len

    print(f"Средняя оценка книг: {average_rating}")

def author_statistics(books : list):
    print()

    author_books_count = {}
    for book in books:
        author = book["author"]

        if author not in author_books_count:
            author_books_count[author] = 0

        author_books_count[author] += 1

    for author, count in author_books_count.items():
        print(f"Автор: {author}")
        print(f"    Количество книг: {count}")
        print()

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
                print_books(books)

            case "3":
                calculate_average_rating(books)

            case "4":
                author_statistics(books)

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