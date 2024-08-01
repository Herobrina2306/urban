def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function() # При вызове функции test_function внутреняя функция inner_function работает коректно
# inner_function() # При попытке вызвать фукцию отдельно выходит ошибка, что функция не определена
