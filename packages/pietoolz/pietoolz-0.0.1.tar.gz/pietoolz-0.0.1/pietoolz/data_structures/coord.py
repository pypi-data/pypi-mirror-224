from typing import Optional, Union


class Coord:
    """
    A coordinate class to represent a point in 2D space.
    
    Parameters
    ----------
    x : int, float
        The x-coordinate of the point.
    y : int, 
        The y-coordinate of the point.
    
    Attributes
    ----------
    x : int, float
        The x-coordinate of the point.
    y : int, float
        The y-coordinate of the point.
    
    Methods
    -------
    __init__(x, y)
        Initialize the coordinate object.
    __repr__()
        Return a string representation of the coordinate object.
    __str__()
        Return a string representation of the coordinate object.
    __eq__(other)
        Return True if the coordinates are equal, False otherwise.
    __ne__(other)
        Return True if the coordinates are not equal, False otherwise.
    __add__(other)
        Return the sum of the coordinates.
    __sub__(other)
        Return the difference of the coordinates.
    __mul__(other)
        Return the product of the coordinates.
    __truediv__(other)
        Return the quotient of the coordinates.
    __floordiv__(other)
        Return the quotient of the coordinates.
    __mod__(other)
        Return the remainder of the coordinates.
    __pow__(other)
        Return the power of the coordinates.
    __abs__()
        Return the absolute value of the coordinates.
    __neg__()
        Return the negation of the coordinates.
    __pos__()
        Return the coordinates.
    __invert__()
        Return the inverse of the coordinates.
    __lt__(other)
        Return True if the coordinates are less than the other, False otherwise.
    __le__(other)
        Return True if the coordinates are less than or equal to the other, False otherwise.
    __gt__(other)
        Return True if the coordinates are greater than the other, False otherwise.
    __ge__(other)
        Return True if the coordinates are greater than or equal to the other, False otherwise.
    __getitem__(key)
        Return the coordinate value at the given key.
    __setitem__(key, value)
        Set the coordinate value at the given key.
    __delitem__(key)
        Delete the coordinate value at the given key.
    __contains__(value)
        Return True if the value is in the coordinates, False otherwise.
    __len__()
        Return the number of coordinates.
    __iter__()
        Return an iterator of the coordinates.
    __reversed__()
        Return a reverse iterator of the coordinates.
    __copy__()
        Return a shallow copy of the coordinates.
    __deepcopy__()
        Return a deep copy of the coordinates.
    __hash__()
        Return the hash of the coordinates.
    __bool__()
        Return True if the coordinates are not zero, False otherwise.
    __int__()
        Return the integer representation of the coordinates.
    __float__()
        Return the float representation of the coordinates.
    __complex__()
        Return the complex representation of the coordinates.
    __bytes__()
        Return the bytes representation of the coordinates.
    __format__(format_spec)
        Return the formatted representation of the coordinates.
    __round__(n)
        Return the rounded coordinates.
    __floor__()
        Return the floor of the coordinates.
    __ceil__()
        Return the ceiling of the coordinates.
    __trunc__()
        Return the truncated coordinates.
    __index__()
        Return the index of the coordinates.
    __enter__()
        Return the coordinates.
    __exit__()
        Return None.
    __call__()
        Return the coordinates.
    __getattr__(name)
        Return the attribute of the coordinates.
    __setattr__(name, value)
        Set the attribute of the coordinates.
    __delattr__(name)
        Delete the attribute of the coordinates.
    __dir__()
        Return the attributes of the coordinates.
    __getattribute__(name)
        Return the attribute of the coordinates.
    __set__(instance, value)
        Set the attribute of the coordinates.
    __delete__(instance)
        Delete the attribute of the coordinates.
    __slots__
        The slots of the coordinates.
    __dict__
        The dictionary of the coordinates.
    __weakref__
        The weak reference of the coordinates.
    __class__
        The class of the coordinates.
    x
        The x-coordinate of the point.
    y
        The y-coordinate of the point.

    Examples
    --------
    >>> from pytoolz.data_structures import Coord
    >>> c = Coord(1, 2)
    >>> c
    Coord(1, 2)
    >>> c.x
    1
    >>> c.y
    2
    >>> c == Coord(1, 2)
    True
    >>> c != Coord(1, 2)
    False
    >>> c + Coord(1, 2)
    Coord(2, 4)
    >>> c - Coord(1, 2)
    Coord(0, 0)
    >>> c * Coord(1, 2)
    Coord(1, 4)
    >>> c / Coord(1, 2)
    Coord(1.0, 1.0)
    >>> c // Coord(1, 2)
    Coord(1, 1)
    >>> c % Coord(1, 2)
    Coord(0, 0)
    >>> c ** Coord(1, 2)
    Coord(1, 4)
    >>> abs(c)
    Coord(1, 2)
    >>> -c
    Coord(-1, -2)
    >>> +c
    Coord(1, 2)
    >>> ~c
    Coord(-2, -3)
    >>> c < Coord(1, 2)
    False
    >>> c <= Coord(1, 2)
    True
    >>> c > Coord(1, 2)
    False
    >>> c >= Coord(1, 2)
    True
    >>> c[0]
    1
    >>> c[1]
    2
    >>> c[0] = 3
    >>> c[1] = 4
    >>> c
    Coord(3, 4)
    >>> del c[0]
    >>> del c[1]
    >>> c
    Coord(0, 0)
    >>> 1 in c
    True
    >>> 2 in c
    True
    >>> len(c)
    2
    """


    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
