class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop():
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        f = file.read()
        file.close()
        return f

    def add(self, *products):
        file = open(self.__file_name, 'r+')
        n = []
        for i in products:
            m = []
            f = file.readlines()
            for l in f:
                m.append(l.split(', '))
            for j in range(len(m)):
                n.append(m[j][0])
                if len(f) == 0:
                    file.write(str(f'{i}\n'))
                else:
                    if str(i.name) in n:
                        print(f'Продукт {i} уже есть в магазине')
                    else:
                        file.write(str(f'{i}\n'))
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())