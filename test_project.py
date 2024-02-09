from project import Rectangle, Triangle, Trapezoid, Circle, Ellipse     # to be able to use convert() & gauge()
import pytest   # to use pytest.raises


def test_Rectangle():
    #this checks the boundary conditions
    assert Rectangle(5,6) == 'Ix = 90.0, Iy = 62.5'


def test_Trapezoid():
    #this checks the boundary conditions
    assert Trapezoid(5,6,7) == 'Ix = 600.25, Iy = 444.354'


def test_Ellipse():
    assert Ellipse(5,6) == 'Ix = 848.23, Iy = 589.049'

    # assert Rectangle() == "E"
    # assert gauge(0) == "E"
    # assert gauge(99) == "F"
    # assert gauge(100) == "F"
    # #this checks that correct values are outputed
    # assert gauge(45) == "45%"



    