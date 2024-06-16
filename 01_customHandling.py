#implementing custom exception handling.
import logging
logging.basicConfig(filename="01a_Logs.log", level=logging.DEBUG, format='%(asctime)s %(message)s')

class ValidateAge(Exception):  # Use PascalCase for class names
    def __init__(self, msg):
        self.msg = msg

def validate_age(age):
    logging.info("Created a method to check if age entered is valid or raises an exception, checking...")
    if age < 0:
        logging.error("Error")
        raise ValidateAge("Entered age is negative")

    elif age > 100:
        logging.error("Error")
        raise ValidateAge("Entered age is very high")
    else:
        logging.info("All data correct, no error <3")
        logging.info("Age is valid")

try:
    logging.info("Entered try block, checking for exceptions...")
    age = int(input("Enter your age: "))  # Clearer prompt
    validate_age(age)
except ValidateAge as e:
    logging.info("Error is : {E}".format(E=e))