class Employee:
    no_of_leaves=15
    pass

ansh=Employee()
lewis=Employee()

ansh.name="Ansh"
ansh.salary=25000000
ansh.role="CEO"

lewis.name="Lewis"
lewis.salary=223343434
lewis.role="CEO 2nd"
lewis.no_of_leaves=Employee.no_of_leaves
print(lewis.__dict__)
# To change number of leaves
Employee.no_of_leaves=20
print(Employee.no_of_leaves)

# But you cannot change through ansh or harry in the class as they are objects.
ansh.no_of_leaves=30
print(ansh.no_of_leaves)