class A:
    def mit(self):
        return f"I am in class A"

class B(A):
    def mit(self):
        return f"I am in class B"

class C(A):
    def mit(self):
        return f"I am in class C"

class D(B,C):
    def mit(self):
        return f"I am in class D"

a=A()
b=B()
c=C()
d=D()

print(d.mit())

