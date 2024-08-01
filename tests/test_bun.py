from praktikum.bun import Bun


class TestBun:

    def test_get_correct_name(self):
        bun = Bun('Мини-салат Экзо-Плантаго', 4400)
        assert bun.get_name() == 'Мини-салат Экзо-Плантаго'

    def test_get_correct_price(self):
        bun = Bun('Хрустящие минеральные кольца', 300)
        assert bun.get_price() == 300
