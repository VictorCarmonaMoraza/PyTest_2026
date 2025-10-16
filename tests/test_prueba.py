from mi_proyecto.main import sumar


class TestCalculadora:

    def test_sumar(self):
        assert sumar(1, 1) == 2

    def test_sumar_falla(self):
        assert sumar(1, 2) == 3
