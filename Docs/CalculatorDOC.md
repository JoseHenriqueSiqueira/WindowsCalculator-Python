## class Calculator (QWidget):
### def __init\__():
This is the constructor method of the Calculator class. It is called when a new object of the class is created.
In this method, some important things are done, such as:
- Calling the base class constructor, which initializes the object with default characteristics;
- Setting the fixed size of the calculator window;
- Loading the calculator user interface (UI);
- Defining the operations supported by the calculator in a dictionary;
- Defining variables used in other methods, such as the numbers to be calculated, user-chosen operations, and others.
Additionally, it connects the buttons of the graphical interface to different methods that will be executed when the user clicks on them. These methods are responsible for different functionalities of the calculator, such as adding numbers, performing operations, displaying results, etc.
In summary, the constructor method is important because it initializes the class object and defines all the necessary variables and functions for the calculator to function correctly.
   
### def number():
This method, "number" is responsible for handling input from the calculator's number buttons. When a user clicks a number button, this method is called and retrieves the text on the clicked button. It then checks if the text is "π" and sets the line edit text to "3.14" if so.
If the text is a decimal point, the method checks if the line edit text already contains a decimal point and returns if it does.
If an operation has been selected, the method checks if the first or second number is currently being entered, updates the line edit text accordingly, and sets the second number (nm2) if it is currently being entered. It then updates the num variable to indicate that the second number is being entered.
If no operation has been selected, the method updates the line edit text with the number clicked and sets the first number (nm1) if it is currently being entered. It then updates the num variable to indicate that the first number is being entered.
          
### def complex_operations():
The "complex_operations(self, op)" method performs arithmetic operations in a calculator. It receives a mathematical operation "op" as a parameter to be executed. The method handles two situations: when there are two numbers already entered and a pending operation, or when there is only one number entered.
In the first situation, the method converts the values "self.nm1" and "self.nm2" to float, uses the corresponding mathematical operation to "self.op", and updates the value "self.nm1" with the result. Next, the method formats the result using the QLocale().toString() function, removes trailing zeros from the number, updates the calculator screen with the operation and result, and clears the "self.nm2" and "self.op" variables. If a division by zero occurs, an error message is displayed.
In the second situation, the method converts the value "self.nm1" to float, executes the mathematical operation corresponding to op, and formats the result using the "QLocale().toString()" function. The formatted result is displayed on the calculator screen and the "self.nm2" variable is cleared. The "self.op" variable is updated with the operation that was just executed. If a division by zero occurs, an error message is displayed.

### def operation():
The operation method performs a mathematical operation based on the input operator (op) and the current values of nm1, nm2, and op.
If nm1, nm2, and op are all defined, it attempts to convert the values to floats, perform the calculation, and format the result before updating the display and resetting the variables.
If nm1 is defined and the negative flag is set, it negates nm1, sets op to the new operator, and updates the display.
If only nm1 is defined, it updates the display with the new operator.
If the display is "0" and the operator is "-" or not "-", it sets nm1 to "0", sets op to the new operator, and updates the display.
If a division by zero error occurs, it updates the display with an error message.
   
### def result():

### def clear():

### def reset():

### def updatefont():

### def delete():

### def keyPressEvent():
