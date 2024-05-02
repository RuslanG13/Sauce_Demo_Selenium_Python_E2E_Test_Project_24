from data.base_data import BaseData


class MainData(BaseData):
    catalog_items_names = ('Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt',
                           'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)')
    catalog_items_price = ('$29.99', '$9.99', '$15.99', '$49.99', '$7.99', '$15.99')
    filter_dropdown = ("Name (A to Z)", "Name (Z to A)", "Price (low to high)", "Price (high to low)")
    products_title = "Products"
