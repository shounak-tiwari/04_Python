class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        print("Single ton instance created ")

    
x = Singleton()
y = Singleton()

print(x is y )