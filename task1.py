''''
Its the task on strings dated 15th May 2022

s = "this is My First Python programming class and i am learNING python string and its function"

1 . Try to extract data from index one to index 300 with a jump of 3

2. Try to reverse a string without using reverse function

3. Try to split a string after conversion of entire string in uppercase

4. Try to convert the whole string into lower case

5 . Try to capitalize the whole string
'''

import logging
logging.basicConfig(filename='logTask_2022_05_15.log',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('This is a task on string manipulation given in the 15th May, 2022 class.')

class StringMan():
    '''This will extract data from a string and log the result.'''
    def __init__(self, task):
        '''Initialize the class with the string task.'''
        self._task = task


    def extractData(self, a, b, c):
        logging.info('The task is to extract a information from the string from a given index to other index with a jump.')
        try:
            res = self._task[a:b:c]
            logging.info('The result is:  %s.', res)
            return res
        except Exception as e:
            logging.error(e)


    def reverseString(self):
        logging.info('The task is to reverse the input without using reverse function.')
        try:
            x = -1
            y = None
            z = -1
            r = self.extractData(x,y,z)
            logging.info('The extracted string is:  %s', r)
            return r
        except Exception as e:
            logging.error(e)

    def upperSplit(self):
        logging.info('The task is to change the input string to uppercase and than split it.')
        try:
            a = self._task.upper().split(' ')
            logging.info('The result is: %s', a)
            return a
        except Exception as e:
            logging.error(e)

    def stringlower(self):
        logging.info('Task is to change the whole string to lower case.')
        try:
            a = self._task.lower()
            logging.info('The modified string is: %s', a)
            return a
        except Exception as e:
            logging.error(e)

    def stringCapi(self):
        logging.info('Task is to capitalize the whole string.')
        try:
            a = self._task.title()
            logging.info('The modified string is: %s', a)
            return a
        except Exception as e:
            logging.error(e)


s = "this is My First Python programming class and i am learNING python string and its function"

task = StringMan(s)

task.extractData(1,300,3)

task.reverseString()

task.upperSplit()

task.stringlower()

task.stringCapi()
