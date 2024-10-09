class Info:
    Info_ = {}
    def __init__(self, obj):
        self.obj = obj

    def introspection_info(self):
        type_ = str(type(self.obj))[8:-2]
        self.Info_['type'] = type_
        if self.Info_['type'] == 'type' or self.Info_['type'][2:6] =='main':
            at = str(self.obj.__dict__.keys())[12:-3]
            self.Info_['attributes'] = at.split("', '")
            self.Info_['module'] = self.obj.__module__
        else:
            self.Info_['attributes'] = ['...']
        self.Info_['metods'] = []
        for i in dir(self.obj):
            if i not in self.Info_['attributes']:
                self.Info_['metods'].append(i)

    def __str__(self):
        self.introspection_info()
        return str(self.Info_)


class new_class():
    def __init__(self, number):
       self.multi = int(number) * 2
       self.str = str(number)

    def pri(self):
        print(self.multi, self.str)

class_info = Info(new_class)
number_info = Info(42)
function_info = Info(Info.introspection_info)
object_info = Info(new_class(2))

print(number_info) # Интроспекция числа
print(function_info) # Интроспекция  функции
print(class_info) # Интроспекция класса
print(object_info) # Интроспекция объекта класса
