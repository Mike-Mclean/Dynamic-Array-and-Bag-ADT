
class StaticArrayException(Exception):
    """
    Custom exception for Static Array class.

    """
    pass


class StaticArray:
    """
    Implementation of Static Array Data Structure.
    Implemented methods: get(), set(), length()
    """

    def __init__(self, size: int = 10) -> None:
        """
        Create array of given size.
        Initialize all elements with values of None.
        If requested size is not a positive number,
        raise StaticArray Exception.
        """
        if size < 1:
            raise StaticArrayException('Array size must be a positive integer')

        # The underscore denotes this as a private variable and
        # private variables should not be accessed directly.
        # Use the length() method to get the size of a StaticArray.
        self._size = size

        # Remember, this is a built-in list and is used here
        # because Python doesn't have a fixed-size array type.
        # Don't initialize variables like this in your assignments!
        self._data = [None] * size

    def __iter__(self) -> None:
        """
        Disable iterator capability for StaticArray class.
        This means loops and aggregate functions like
        those shown below won't work:

        arr = StaticArray()
        for value in arr:     # will not work
        min(arr)              # will not work
        max(arr)              # will not work
        sort(arr)             # will not work
        """
        return None

    def __str__(self) -> str:
        """Override string method to provide more readable output."""
        return f"STAT_ARR Size: {self._size} {self._data}"

    def get(self, index: int):
        """
        Return value from given index position.
        Invalid index raises StaticArrayException.
        """
        if index < 0 or index >= self.length():
            raise StaticArrayException('Index out of bounds')
        return self._data[index]

    def set(self, index: int, value) -> None:
        """
        Store value at given index in the array.
        Invalid index raises StaticArrayException.
        """
        if index < 0 or index >= self.length():
            raise StaticArrayException('Index out of bounds')
        self._data[index] = value

    def __getitem__(self, index: int):
        """Enable bracketed indexing."""
        return self.get(index)

    def __setitem__(self, index: int, value: object) -> None:
        """Enable bracketed indexing."""
        self.set(index, value)

    def length(self) -> int:
        """Return length of the array (number of elements)."""
        return self._size


