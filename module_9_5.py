class MyClass:
    def __init__(self):
        self.state = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.state += 1
        if self.state > 4:
            raise StopIteration
        return self.state

myObj = MyClass()
for i in myObj:
    print(i)