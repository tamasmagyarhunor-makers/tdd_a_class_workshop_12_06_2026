from lib.person import Person
import pytest

def test_create_person():
    """
    given I instantiate a Person, named Naima
    person will have the name and an empty list (items)
    """
    person = Person('Naima')

    assert person.items == []
    assert person.name == 'Naima'

def test_add_item():
    """
    given I have a Person and I try add_item('pencil')
    person will have 'pencil' stored in self.items
    """
    person = Person('Han')

    person.add_item('pencil')

    assert person.items == ['pencil']

def test_see_items_added_list():
    """
    given I want to see items in my list
    person will use display_items_list()
    """
    person = Person('Anton')
    person.add_item('pencil')
    person.add_item('pen')

    assert person.display_items_list() == ['pencil', 'pen']

def test_see_items_added_list2():
    """
    given I want to see items in my list
    person will use display_items_list()
    """
    person = Person('Johnny')
    person.add_item('mobile phone')
    person.add_item('post it notes')

    assert person.display_items_list() == ['mobile phone', 'post it notes']

def test_display_items_list_raises_exception_if_empty_items():
    """
    given I want to see items in my list
    person.display_items_list() will throw Exception if self.items is empty
    """
    person = Person('Anton')

    with pytest.raises(Exception) as error:
        person.display_items_list()

    error_message = error.value

    assert str(error_message) == 'This is an empty list!'

def test_test_raises_type_error_when_calls_add_item_with_not_string():
    """
    given I have a Person and I try add_item(2)
    add_item() will raise TypeError 'Item can only be string!'
    """
    person = Person('Trouli')

    with pytest.raises(TypeError) as error:
        person.add_item(2)

    error_message = str(error.value)

    assert error_message == 'item is not a string!'