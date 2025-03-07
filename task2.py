from abc import ABC, abstractmethod
import logging
from colorama import Fore, Style, init

# Ініціалізація colorama
init(autoreset=True)

# Налаштування системи логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Клас для зберігання інформації про книгу


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return (
            f"{Fore.CYAN}Title: {Fore.YELLOW}{self.title}, {Fore.CYAN}Author: {Fore.YELLOW}{self.author}, "
            f"{Fore.CYAN}Year: {Fore.YELLOW}{self.year}{Style.RESET_ALL}"
        )

# Інтерфейс бібліотеки для забезпечення чіткої специфікації


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass

# Реалізація бібліотеки


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logger.info(
            f"{Fore.GREEN}Book '{book.title}' added successfully.{Style.RESET_ALL}")

    def remove_book(self, title: str) -> None:
        self.books = [book for book in self.books if book.title != title]
        logger.info(
            f"{Fore.RED}Book '{title}' removed successfully.{Style.RESET_ALL}")

    def show_books(self) -> None:
        if not self.books:
            logger.info(f"{Fore.RED}Library is empty.{Style.RESET_ALL}")
        for book in self.books:
            logger.info(str(book))

# Менеджер бібліотеки для взаємодії з користувачем


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()

# Основна функція для роботи програми


def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input(
            f"{Fore.BLUE}Enter command (add, remove, show, exit): {Style.RESET_ALL}").strip().lower()

        if command == "add":
            title = input(
                f"{Fore.BLUE}Enter book title: {Style.RESET_ALL}").strip()
            author = input(
                f"{Fore.BLUE}Enter book author: {Style.RESET_ALL}").strip()
            year = int(
                input(f"{Fore.BLUE}Enter book year: {Style.RESET_ALL}").strip())
            manager.add_book(title, author, year)
        elif command == "remove":
            title = input(
                f"{Fore.BLUE}Enter book title to remove: {Style.RESET_ALL}").strip()
            manager.remove_book(title)
        elif command == "show":
            manager.show_books()
        elif command == "exit":
            logger.info(f"{Fore.RED}Exiting the program.{Style.RESET_ALL}")
            break
        else:
            logger.info(
                f"{Fore.RED}Invalid command. Please try again.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()

