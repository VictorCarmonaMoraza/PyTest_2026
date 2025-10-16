import pytest

@pytest.mark.prueba
class TestDePrueba:
    def test_primero(self):
        assert True

    def test_segundo(self):
        assert True

@pytest.mark.prueba
@pytest.mark.magia
def test_tercero(self):
    assert True
