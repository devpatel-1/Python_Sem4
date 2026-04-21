# Write programs to implement following scenarios where A, B, C, D, E and F are classes and check() is a method. In both scenarios, which check() method is called, when we execute statement- E().check()


class A:
    def check(self):
        print("A check")

class B(A):
    pass

class F:
    def check(self):
        print("F check")

class C(F):
    def check(self):
        print("C check")

class D(F):
    def check(self):
        print("D check")

class E(B, C, D):
    pass


obj = E()
obj.check()