from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # Тест для метода add_new_book:


import pytest
from main import BooksCollector


def test_add_new_book_success(collector):
    collector.add_new_book("Book1")
    assert "Book1" in collector.books_genre


def test_add_new_book_invalid_length(collector):
    long_title = "This is a book with a very long title exceeding 40 characters"
    collector.add_new_book(long_title)
    assert not collector.get_book_genre(long_title)


def test_add_new_book_duplicate(collector):
    title = "Book2"
    some_genre = collector.get_books_genre()[0]
    collector.add_new_book(title)
    collector.set_book_genre(title, some_genre)
    collector.add_new_book("Book2")
    assert collector.get_book_genre(title) == some_genre


# Тест для метода set_book_genre:
def test_set_book_genre_success(collector):
    collector.add_new_book("Book1")
    collector.set_book_genre("Book1", "Фантастика")
    assert collector.get_book_genre("Book1") == "Фантастика"


def test_set_book_genre_invalid_book(collector):
    title = "NonexistentBook"
    collector.set_book_genre(title, "Фантастика")
    assert collector.get_book_genre(title) is None


def test_set_book_genre_invalid_genre(collector):
    collector.add_new_book("Book2")
    collector.set_book_genre("Book2", "Музыка")
    assert collector.get_book_genre("Book2") == ''


# Тесты для метода get_book_genre:
def test_get_book_genre_existing_book(collector):   
    collector.add_new_book("Book1")
    collector.set_book_genre("Book1", "Фантастика")
    assert collector.get_book_genre("Book1") == "Фантастика"


def test_get_book_genre_non_existing_book(collector):
    assert collector.get_book_genre("NonexistentBook") is None


# Тесты для метода get_books_with_specific_genre:
def test_get_books_with_specific_genre(collector):
    collector.add_new_book("Fantasy Book")
    collector.set_book_genre("Fantasy Book", "Фантастика")
    collector.add_new_book("Sci-Fi Book")
    collector.set_book_genre("Sci-Fi Book", "Фантастика")
    assert set(collector.get_books_with_specific_genre("Фантастика")) == {"Fantasy Book", "Sci-Fi Book"}


def test_get_books_with_non_existent_genre(collector):
    assert collector.get_books_with_specific_genre("Музыка") == []


# Тест для метода get_books_genre:
def test_get_books_genre(collector):
    collector.add_new_book("Book1")
    collector.set_book_genre("Book1", "Фантастика")
    assert collector.get_books_genre() == {"Book1": "Фантастика"}


# Тесты для метода get_books_for_children:
def test_get_books_for_children(collector):
    collector.add_new_book("Cartoon Book")
    collector.set_book_genre("Cartoon Book", "Мультфильмы")
    collector.add_new_book("Horror Book")
    collector.set_book_genre("Horror Book", "Ужасы")
    assert set(collector.get_books_for_children()) == {"Cartoon Book"}


# Тесты для метода add_book_in_favorites:
def test_add_book_in_favorites_success(collector):
    collector.add_new_book("Book1")
    collector.add_book_in_favorites("Book1")
    assert "Book1" in collector.get_list_of_favorites_books()


def test_add_book_in_favorites_nonexistent_book(collector):
    collector.add_book_in_favorites("NonexistentBook")
    assert "NonexistentBook" not in collector.get_list_of_favorites_books()


def test_add_book_in_favorites_duplicate(collector):
    collector.add_new_book("Book1")
    collector.add_book_in_favorites("Book1")
    collector.add_book_in_favorites("Book1")
    assert collector.get_list_of_favorites_books().count("Book1") == 1


# Тесты для метода delete_book_from_favorites:
def test_delete_book_from_favorites_success(collector):
    collector.add_new_book("Book1")
    collector.add_book_in_favorites("Book1")
    collector.delete_book_from_favorites("Book1")
    assert "Book1" not in collector.get_list_of_favorites_books()


def test_delete_nonexistent_book_from_favorites(collector):
    collector.delete_book_from_favorites("NonexistentBook")


# Тест для метода get_list_of_favorites_books:
def test_get_list_of_favorites_books(collector):
    collector.add_new_book("Book1")
    collector.add_book_in_favorites("Book1")
    collector.add_new_book("Book2")
    collector.add_book_in_favorites("Book2")
    assert set(collector.get_list_of_favorites_books()) == {"Book1", "Book2"}

@pytest.mark.parametrize("test_input,expected", [('', False), ('a', True), (40 * 'a', True),  (41 * 'a', False)])
def test_add_new_book_invalid_length_boundary(test_input, expected):
    collector.add_new_book(test_input)
    assert (collector.get_book_genre is not None) is expected

