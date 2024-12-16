class Cat:
    def sleep(self):
        return "*sleeping*"
    
    def speak(self):
        return "Meow!"
    
    def eat(self):
        return "*eating*"
    
    def hunt(self):
        return "*hunting*"
    
class Persian(Cat):
    def talk(self):
        return super().speak()
    
kitty = Persian()
print(kitty.talk())