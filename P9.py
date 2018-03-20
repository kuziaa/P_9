class Car(object):

    created = 0

    def __init__(self, color='black'):
        self.color = color
        self.wheels = 5 if self.color == 'black' else 4
        Car.created += 1

    def diag(self):
        print('this is a {} car with {} wheels'.format(self.color, self.wheels))

print(Car.created)

car_1 = Car()
car_1.diag()
print(Car.created)

car_2 = Car('red')
car_2.diag()
print(Car.created)