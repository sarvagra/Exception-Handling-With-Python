# raising a custom exception:
import logging 
logging.basicConfig(filename="01a_Logs.log",level=logging.DEBUG, format='%(asctime)s %(message)s')

class validateage(Exception):
    logging.info("Created an exception class and raising method")
    def __init__(self, msg):
        self.msg= msg

def validateage(age):
    logging.info("created a method to check if age entered is valid or raises an exception, checking...")
    if age<0:
        logging.error("Error found, age is negative.")
        raise validateage("entered age is negative")
        
    
    elif age>100:
        logging.error("Error found, age is very high")
        raise validateage("entered age is very high")
    else :
        logging.info("All data correct, no error <3")
        print("age is valid")

try :
    logging.info("entered try block, checking for exceptons...")
    age = int(input("enter your age")) 
    validateage(age) 
except validateage as e :
    print(e)

