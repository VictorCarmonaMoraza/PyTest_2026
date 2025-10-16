from mi_proyecto.main import  sumar


def test_sumar():
    assert sumar(1,1) == 2

def test_sumar_falla():
    assert  sumar(1,2) == 4