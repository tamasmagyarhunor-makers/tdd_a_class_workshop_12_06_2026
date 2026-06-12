## 1 the problem
```text
As a User
So that I can represent a Person
I want to be create a Person with a name and items

As a User
So that I can get my Person to have items
I want to be able to store a Persons items

As a User
So that I can see what items my Person has
I want to be able to see a Persons items
```
## 2 class and function signature
```python
class Person:
    # name - string
    # items - []

    def __init__(self, name):
        self.name = name
        self.items = [pencil]
    
    def add_item(self, item):
        # parameters
        #  - item, string
        # returns
        # - None
        # side effects
        # - it puts the item to the self.items[]
        # - throws TypeError if item is not a str()
        pass

    def display_items_list(self):
        # parameters
        # - none
        # returns
        # - self.items
        # side
        # - raise Exception if list is empty
        pass

    def get_name(self):
        #
        #
        #
        pass

```

## 3 examples
```python
"""
given I instantiate a Person, named Naima
person will have the name and an empty list (items)
"""
person = Person('Naima')

person.items == []
person.name == 'Naima'

"""
given I have a Person and I try add_item('pencil')
person will have 'pencil' stored in self.items
"""
person = Person('Han')

person.add_item('pencil')

person.items == ['pencil']

"""
given I want to see items in my list
person will use display_items_list()
"""
person = Person('Anton')
person.add_item('pencil')
person.add_item('pen')

person.display_items_list() == ['pencil', 'pen']

"""
given I want to see items in my list
person.display_items_list() will throw Exception if self.items is empty
"""
person = Person('Anton')

with pytest.raises(Exception) as error:
    person.display_items_list():

error_message = error.value

assert str(error_message) == 'This is an empty list!'

"""
given I have a Person and I try add_item(2)
add_item() will raise TypeError 'Item can only be string!'
"""
person = Person('Trouli')

with pytest.raises(TypeError) as error:
    person.add_item(2)

error_message = str(error.value)

assert error_message == 'item is not a string!'
```
