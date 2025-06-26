#lab 1 
# Base class demonstrating Encapsulation 
class Employee: 
    def __init__(self, name, salary): 
        self.__name = name         # Private attribute 
        self.__salary = salary     # Private attribute 
 
    # Getter for name 
    def get_name(self): 
        return self.__name 
 
    # Setter for name 
    def set_name(self, name): 
        self.__name = name 
 
    # Getter for salary 
    def get_salary(self): 
        return self.__salary 
 
    # Setter for salary 
    def set_salary(self, salary): 
        if salary >= 0: 
            self.__salary = salary 
        else: 
            print("Invalid salary") 
 
    # Overloading the + operator to add salaries of two employees 
    def __add__(self, other): 
        return self.__salary + other.__salary 
 
# Derived class demonstrating Inheritance 
class Manager(Employee): 
    def __init__(self, name, salary, department): 
        super().__init__(name, salary)  # Call to base class constructor 
        self.department = department 
 
    # Method Overloading using default arguments 
    def display_info(self, show_department=True): 
        print("Name:", self.get_name()) 
        print("Salary:", self.get_salary()) 
        if show_department: 
            print("Department:", self.department) 
 
# Main function to demonstrate functionality 
def main(): 
    emp1 = Employee("Alice", 50000) 
    emp2 = Employee("Bob", 60000) 
 
    # Demonstrate encapsulation 
    print("Initial salary of emp1:", emp1.get_salary()) 
    emp1.set_salary(55000) 
    print("Updated salary of emp1:", emp1.get_salary()) 
 
    # Demonstrate operator overloading 
    total_salary = emp1 + emp2 
    print("Total salary of emp1 and emp2:", total_salary) 
 
    # Demonstrate inheritance and method overloading 
    mgr = Manager("Charlie", 80000, "IT") 
    print("\nManager Info:") 
    mgr.display_info() 
    print("\nManager Info (without department):") 
    mgr.display_info(show_department=False) 
 
if __name__ == "__main__": 
    main() 
 
 
 


 #lab2
 import numpy as np 
import matplotlib.pyplot as plt 
 
# a) Array Manipulation, Searching, Sorting, Splitting 
print("=== Array Manipulation ===") 
arr = np.array([[1, 2, 3], [4, 5, 6]]) 
print("Original Array:\n", arr) 
 
# Reshape 
reshaped = arr.reshape((3, 2)) 
print("Reshaped to 3x2:\n", reshaped) 
 
# Flatten 
flattened = arr.flatten() 
print("Flattened Array:\n", flattened) 
 
print("\n=== Searching ===") 
search_result = np.where(arr == 5) 
print("Position of element 5:", search_result) 
 
print("\n=== Sorting ===") 
unsorted = np.array([5, 2, 9, 1]) 
sorted_arr = np.sort(unsorted) 
print("Unsorted:", unsorted) 
print("Sorted:", sorted_arr) 
 
print("\n=== Splitting ===") 
split_array = np.array([10, 20, 30, 40, 50, 60]) 
split_result = np.split(split_array, 3) 
print("Split into 3 parts:", split_result) 
 
# b) Broadcasting and Plotting NumPy arrays 
print("\n=== Broadcasting ===") 
a = np.array([1, 2, 3]) 
b = 2 
broadcasted_result = a + b 
print("Broadcasted addition (a + 2):", broadcasted_result) 
 
# Plotting 
print("\n=== Plotting ===") 
10  
 
x = np.linspace(0, 2 * np.pi, 100) 
y = np.sin(x) 
 
plt.plot(x, y, label="sin(x)") 
plt.title("Sine Wave using NumPy") 
plt.xlabel("x") 
plt.ylabel("sin(x)") 
plt.legend() 
plt.grid(True) 
plt.show() 




#lab3

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Generate sample data using NumPy
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = np.sin(x)

data = {
    "Category": np.random.choice(['A', 'B', 'C'], 100),
    "Value": np.random.normal(loc=50, scale=15, size=100),
    "Score": np.random.rand(100) * 100
}
df = pd.DataFrame(data)

# Line plot
plt.figure(figsize=(6, 4))
sns.lineplot(x=x, y=y)
plt.title("Line Plot of sin(x)")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()

# Bar plot
plt.figure(figsize=(6, 4))
sns.barplot(x='Category', y='Value', data=df)
plt.title("Bar Plot of Value by Category")
plt.show()

# Histogram
plt.figure(figsize=(6, 4))
sns.histplot(df['Value'], kde=True, bins=15)
plt.title("Histogram of Value")
plt.show()

# Box plot
plt.figure(figsize=(6, 4))
sns.boxplot(x='Category', y='Value', data=df)
plt.title("Box Plot of Value by Category")
plt.show()

# Scatter plot
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Value', y='Score', hue='Category', data=df)
plt.title("Scatter Plot of Score vs Value")
plt.show()

# Heatmap (correlation matrix)
plt.figure(figsize=(6, 4))
corr = df[['Value', 'Score']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Heatmap of Correlation Matrix")
plt.show()