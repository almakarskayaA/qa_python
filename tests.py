import random
import pytest


class TestBooksCollector:

    def test_books_genre_fav_dict_is_empty(self, books_collector):

        assert len(books_collector.books_genre) == 0 and len(books_collector.favorites) == 0

    def test_genre_list_is_not_empty(self, books_collector):

        assert books_collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating_list_is_not_empty(self, books_collector):

        assert books_collector.genre_age_rating == ['Ужасы', 'Детективы']

    @pytest.mark.parametrize('book', ['Книга', 'Три мушкетера'])
    def test_add_new_book_positive(self, books_collector, book):

        books_collector.add_new_book(book)
        assert books_collector.books_genre[book] == ''

    @pytest.mark.parametrize('book', ['', 'Преступление и наказание'])
    def test_add_new_book_more_negative_sizes(self, books_collector, book):

        assert not books_collector.add_new_book(book)

    def test_set_book_genre_valid_name(self, books_collector):

        books_collector.add_new_book('Война и мир')
        books_collector.set_book_genre('Война и мир', 'Детективы')
        assert books_collector.books_genre['Война и мир'] == 'Детективы'

    @pytest.mark.parametrize('name, genre', [
        ['Агата Кристи', 'Детективы'],
        ['Евгений Онегин', 'Народный эпос ']
    ])
    def test_set_book_genre_negative_case(self, books_collector, name, genre):

        books_collector.add_new_book(name)
        assert not books_collector.set_book_genre(name, genre)

    def test_get_book_genre_return_valid_name(self, books_collector):

        books_collector.add_new_book('Мастер и Маргарита')
        books_collector.set_book_genre('Мастер и Маргарита', 'Фантастика')
        assert books_collector.get_book_genre('Мастер и Маргарита') == 'Фантастика'

    def test_get_books_with_specific_genre_when_valid_genre(self, books_collector):

        books_collector.add_new_book('Отцы и дети')
        books_collector.set_book_genre('Отцы и дети', 'Мультфильмы')
        assert books_collector.get_books_with_specific_genre('Мультфильмы') \
               and type(books_collector.get_books_with_specific_genre('Мультфильмы')) == list

    @pytest.mark.parametrize('name, genre', [['', 'Фантастика'], ['Бирманский', 'Комедии']])
    def test_get_books_with_specific_genre_empty_list_book_false_genre(self, books_collector, name, genre):

        books_collector.add_new_book(name)
        assert not books_collector.get_books_with_specific_genre('Шутёхи')

    def test_get_books_genre_filled_dict(self, books_collector):

        books = ['Торадора', 'Закупяченский движ', 'Суета на ферме', 'Огорошен и ладно']
        for name in books:
            books_collector.add_new_book(name)

        random_book = random.choice(books)
        assert random_book in books_collector.get_books_genre() \
            and type(books_collector.get_books_genre()) == dict

    def test_get_books_genre_empty_dict(self, books_collector):

        assert not books_collector.get_books_genre()

    def test_get_books_for_children_correct_genre(self, books_collector):

        books = ['Шелок Холмс', 'Багряная комната', 'Багряный вечер', 'Утро в сосновом бору', 'ПРД']
        x = 0
        for name in books:
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, books_collector.genre[x])
            x += 1

        for rating in books_collector.genre_age_rating:
            assert rating not in books_collector.get_books_for_children()

    def test_get_books_for_children_adult_rating(self, books_collector):

        books = ['Дюймовочка', 'Снежная королева']
        x = 0
        for name in books:
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, books_collector.genre_age_rating[x])
            x += 1

        assert not books_collector.get_books_for_children()

    def test_add_book_in_favorites_when_books_in_list(self, books_collector):

        books_collector.add_new_book('Дуолинго')
        books_collector.add_book_in_favorites('Дуолинго')

        assert 'Дуолинго' in books_collector.favorites

    def test_add_book_in_favorites_when_book_not_in_list(self, books_collector):

        books = ['Ворчатель', 'Парфюмер', 'Оно']
        for name in books:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)

        assert not books_collector.add_book_in_favorites('Колобок')

    def test_delete_book_from_favorites(self, books_collector):

        books_collector.add_new_book('Убить Билла')
        books_collector.add_book_in_favorites('Убить Билла')

        books_collector.delete_book_from_favorites('Убить Билла')
        assert 'Убить Билла' not in books_collector.favorites

    def test_delete_book_from_favorites_no_name_in_list(self, books_collector):

        books_collector.add_new_book('Урюк в компоте')
        books_collector.add_book_in_favorites('Урюк в компоте')

        assert not books_collector.delete_book_from_favorites('Комплаенс в Слизерин')

    def test_get_list_of_favorites_books_not_empty(self, books_collector):

        books = ['Гарри Поттер', 'Гарри Поттер и Философский камень', 'Гарри Поттер и Тайная комната']
        for name in books:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)

        assert books_collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_empty_list(self, books_collector):

        books_collector.add_new_book('Гарри Поттер и Кубок Огня')
        books_collector.add_book_in_favorites('Гарри Поттер и Кубок Огня')
        books_collector.delete_book_from_favorites('Гарри Поттер и Кубок Огня')

        assert not books_collector.get_list_of_favorites_books()
