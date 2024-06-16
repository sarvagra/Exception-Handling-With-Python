# always use a specific exception.
# always print a proper message.
# always try to log error.
#document all the error. 
# clean all the resources.


import logging 
logging.basicConfig(filename="03a_Logs.log", level=logging.DEBUG  , format='%(asctime)s%(message)s')

try :
    10/0
except ZeroDivisionError as e :
    logging.info("Error : {E}".format(E=e))
except FileNotFoundError as e:
    logging.info("Error : {E}".format(E=e))
except AttributeError as e :
    logging.info("Error : {E}".format(E=e)) #not a good practice to add all the exceptions.it will increase code complexity.

try :
    with open("test0.txt", "w") as f :
        f.write("this is the data to file")
except FileNotFoundError as e :
    logging.error("file not found : {E}".format(E=e))
finally :
    f.close()  #always close a file.

try :
    with open("test1.txt","r"):
        f.read(10)

except FileNotFoundError as e :
    logging.error("file not found : {E}".format(E=e))
                  
