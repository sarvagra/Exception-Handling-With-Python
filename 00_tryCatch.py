# put the suspected code in the try block.
import logging 
logging.basicConfig(filename="00a_Logs.log",  level= logging.DEBUG, format='%(asctime)s %(message)s')

try : #contains the main code.
    logging.info("entered into try block")
    f=open("test.txt", 'r')
except Exception as e : #goes into this only if try block has some error.
    logging.info("exception found, entered exception")
    logging.error("this is my exception block : {E}".format(E=e))

else : #executes only when try has no error.
    logging.info("no error found , entered else block")
    logging.info("this will execute only when when try block gets executed without error")

finally : #excutes in ant situatuon.
    logging.info("executing finally block")
    logging.info("finally will execute itself in any situation")



