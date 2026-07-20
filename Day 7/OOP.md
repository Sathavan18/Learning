Method Overriding
When a child class defines its own version of an inherited method
Example:
class Employee:
    def work(self):
        return 'Employee is working'
class Developer(Employee):
    def work(self):
        return 'Developer is writing code'