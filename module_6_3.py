class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance = self.x_distance + dx
        return int(self.x_distance)

class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance = self.y_distance + dy
        return int(self.y_distance)


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)
        self.x_distance = 0
        self.y_distance = 0


          
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        l = []
        l.append(self.x_distance)
        l.append(self.y_distance)
        return tuple(l)

    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()