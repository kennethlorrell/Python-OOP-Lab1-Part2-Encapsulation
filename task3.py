class Product:
    def __init__(self, name: str, price: float, length: float, width: float, height: float, description: str=''):

        if type(name) is not str or type(price) is not float or \
          type(length) is not float or type(width) is not float or \
          type(height) is not float or type(description) is not str:
            raise Exception('Invalid value')

        self.name = name
        self.price = price
        self.length = length
        self.width = width
        self.height = height
        self.description = description

class Client:
    def __init__(self, name: str, surname: str, phone: str, email: str, patronymic: str=''):

        if type(name) is not str or type(patronymic) is not str or \
          type(surname) is not str or type(phone) is not str or \
          type(email) is not str:
            raise Exception('Invalid value')

        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.phone = phone
        self.email = email

class Order():
    def __init__(self, uid, client, goods):

        if not isinstance(client, Client) or \
          not all(map(lambda x: isinstance(x[0], Product), goods)):
            raise Exception('Invalid value')

        self.uid = uid
        self.client = client
        self.goods = goods

    def get_order_price(self):
        return sum(map(lambda x: x[0].price * x[1], self.goods))
