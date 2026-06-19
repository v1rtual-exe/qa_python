import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('book_name', ['Война и мир', 'Марсианин', 'Гарри Поттер'])
    def test_add_new_book_success(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    def test_add_new_book_duplicate(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_max_length(self, collector):
        long_name = 'А' * 41
        collector.add_new_book(long_name)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_empty_name(self, collector):
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        assert collector.get_book_genre('Война и мир') == 'Фантастика'

    def test_get_book_genre(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        assert collector.get_book_genre('Война и мир') == 'Фантастика'

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_new_book('Марсианин')
        collector.set_book_genre('Война и мир', 'Фантастика')
        collector.set_book_genre('Марсианин', 'Фантастика')
        books = collector.get_books_with_specific_genre('Фантастика')
        assert len(books) == 2
        assert 'Война и мир' in books
        assert 'Марсианин' in books

    def test_get_books_for_children(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_new_book('Оно')
        collector.set_book_genre('Война и мир', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert 'Война и мир' in children_books
        assert 'Оно' not in children_books

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        assert 'Война и мир' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        collector.delete_book_from_favorites('Война и мир')
        assert 'Война и мир' not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_in_books(self, collector):
        collector.add_book_in_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 0