# 8) Write a program in which Python and Snake sub classes implement abstract methods- crawl() and sting() of the super class Reptile. What is the output of following statements? 
# i) issubclass(Python, Reptile)		ii) isinstance(Snake(), Reptile)


from abc import ABC, abstractmethod

class Reptile(ABC):

    @abstractmethod
    def crawl(self):
        pass

    @abstractmethod
    def sting(self):
        pass

class Python(Reptile):
    def crawl(self):
        print("Python crawls")

    def sting(self):
        print("Python does not sting")


class Snake(Reptile):
    def crawl(self):
        print("Snake crawls")

    def sting(self):
        print("Snake stings")

p = Python()
s = Snake()

p.crawl()
p.sting()

s.crawl()
s.sting()


print("\nChecks:")
print("issubclass(Python, Reptile):", issubclass(Python, Reptile))
print("isinstance(Snake(), Reptile):", isinstance(Snake(), Reptile))