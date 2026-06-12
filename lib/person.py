class Person:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, item):
        if not isinstance(item, str):
            raise TypeError('item is not a string!')
        self.items.append(item)
    
    def display_items_list(self):
        if len(self.items) == 0:
            raise Exception('This is an empty list!')
        return self.items
