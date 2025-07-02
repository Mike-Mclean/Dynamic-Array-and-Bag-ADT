# Implementation of dynamic arrays and bags

This is an implementation of a dynamic array and bag alternate data structure (ADT). ```dynamic_array.py``` contains a dynamic array class which uses a StaticArray object as its underlying data storage, and will provide many methods similar to the functionality of a Python list. The following functionality is included in the class:

- ```resize(self, new_capacity: int) -> None``` : Changes the underlying storage capacity for the elements in the dynamic array. Does not change the values or the order of elements in the array.
- ```append(self, value: object) -> None``` : Adds a new value to the end of the dynamic array. If the internal storage of the dynamic array is already full, the capcaity of the array is doubled before adding a new value
- ```insert_at_index(self, index: int, value: object) -> None``` : Adds a new value at the specified index in the dynamic array. If the internal storage of the dynamic array is already full, the capcaity of the array is doubled before adding a new value. If the provided index is invlaid, a ```DynamicArrayException``` is raised.
- ```remove_at_index(self, index: int) -> None``` : Removes the element at the specified index. If the provided index is invlaid, a ```DynamicArrayException``` is raised.
- ```slice(self, start_index: int, size: int) -> object``` : Returns a new DynamicArray object that contains the requested number of elements from the original array, starting at the specified start index. If the start index or size are invalid, a ```DynamicArrayException``` is raised.
- ```merge(self, second_da: object) -> None``` : Takes another DynamicArray object as a parameter, and appends all elements from this array onto the current one, in the same order in which they are stored in the input array.
- ```map(self, map_func) ->object``` : Creates a new dynamic array where the value of each element is derived by applying a given ```map_func``` to the corresponding value from the original array.
- ```filter(self, filter_func) ->object``` : Creates a new dynamic array populated with elements from the original array for which filter_func returns True.
- ```reduce(self, reduce_func, initializer=None) ->object``` : Applies the ```reduce_func``` to all elements of the dynamic array and returns the resulting value. Takes an initializer parameter which is set to the first value in the array if none is provided. 

There is also a ```find_mode(arr: DynamicArray) -> tuple[DynamicArray, int]``` function outside of the dynamic array class which receives a dynamic array already in sorted order. The function will return a tuple containing a dynamic array comprising the mode value(s) of the array, and an integer representing the frequency of the mode. 


```bag_da.py``` contains a bag ADT class which uses a DynamicArray from ```dynamic_array.py``` as its underlying data storage. The following functionality is included in the class:

- ```add(self, value: object)``` : Adds a new element to the bag.
- ```remove(self, value: object)``` : Removes any element from the bag that matches the provided ```value```. Returns ```True``` if some object was actually removed from the bag, returns ```False``` otherwise. 
- ```count(self, value: object)``` : Returns the number of elements in the bag that match the provided ```value``` object.
- ```clear(self)``` : Clears the contents of the bag.
- ```equal(self, second_bag: "Bag")``` : Compares the contents of a bag with the contents of ```second_bag```. Returns ```True``` if the bags contain the same number of elements, and the same elements regardless of order. Returns ```False``` otherwise.
- ```__iter__``` : Enables the bag to iterate acress itself.
- ```__next__``` : Returns the next item in the Bag, based on the current location of the iterator.

The ```unit_tests.py``` file contains unit tests for each of the functions mentioned above using Python's ```unittest``` library. 
