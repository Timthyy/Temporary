class Item:
    count_id = 0

    def __init__(self, item_name, item_quantity):
        Item.count_id += 1

        self.__order_id = Item.count_id
        self.__item_name = item_name
        self.__item_quantity = item_quantity

    # getters
    def get_order_id(self):
        return self.__order_id

    def get_item_name(self):
        return self.__item_name

    def get_item_quantity(self):
        return self.__item_quantity

    # setters
    def set_order_id(self, order_id):
        self.__order_id = order_id

    def set_item_name(self, item_name):
        self.__item_name = item_name

    def set_item_quantity(self, item_quantity):
        self.__item_quantity = item_quantity
