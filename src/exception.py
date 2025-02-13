# custom exception
import sys

def error_msg_details(error, error_detail: sys):
    _, _, exc_tb =  error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_msg = "Error occured in python script [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_msg

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super.__init__(error_message) #The super().__init__() call is used in Python within a subclass's __init__ method to initialize attributes inherited from a parent class. It ensures that the parent class's initialization logic is executed, preventing potential issues with uninitialized inherited attributes. This is particularly important in scenarios involving multiple inheritance or complex class hierarchies. By using super().__init__(), the code becomes more maintainable and avoids redundancy.
        self.error_message = error_message_details(error=error_message, error_detail=error_detail)

    def __str__(self): #In Python, def __str__(self) is a special method used to define how an object of a class should be represented as a human-readable string when you try to print it directly, essentially providing a user-friendly way to display the object's information; it's called automatically whenever you use the print() function on an object or when the str() function is applied to it. 
        return self.error_message 

