''''
This was the task given in the class dated 21st May, 2022.

l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
1 . Try to reverse a list
2. try to access 234 out of this list
3 . try to access 456
4 . Try to extract only a list collection form list l
5 . Try to extract "sudh"
6 . Try to list all the key in dict element avaible in list
7 . Try to extract all the value element form dict available in list
'''

import logging
logging.basicConfig(filename='logTask_2022_05_21.log',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('This is a task on list manipulation given in the 21st May, 2022 class.')


class listMan():
    '''Manipulating an input list.'''

    def __init__(self, l):
        flatList = []
        self._l = l
        self._flatList = flatList

    def listReverse(self):
        logging.info('Task is to reverse the input list.')
        try:
            a = self._l[::-1]
            logging.info('The reversed list is: %s', a)
            return a
        except Exception as e:
            logging.error(e)

    def listAppend(self, x):
        '''Method to change a list to flat list. This is an internal method of the class.'''
        try:
            self._flatList.append(x)
        except Exception as e:
            logging.error(e)

    def listFlaten(self, y):
        '''This method will flaten the list and store all the values in a flat list.
        This is an internal method of the class.'''
        try:
            for i in y:
                if type(i) == int or type(i) == float or type(i) == str:
                    self.listAppend(i)
                elif type(i) == list or type(i) == set or type(i) == tuple:
                    for j in i:
                        if type(j) == list or type(j) == set or type(j) == tuple or type(j) == dict:
                            self.listFlaten(j)
                        else:
                            self.listAppend(j)

                elif type(i) == dict:
                    for k, v in i.items():
                        self.listAppend(k)
                        if type(v) == int or type(v) == float or type(v) == str:
                            self.listAppend(v)
                        else:
                            self.listFlaten(v)
        except Exception as e:
            logging.error(e)


    def listFind(self, a):
        logging.info('Task is to find a specific element from the input list.')

        try:
            self.listFlaten(self._l)
            f = self._flatList
            print(f)
            if a in f:
                logging.info('The item %s is present in the input list.', a)
                return True
            else:
                logging.info('The item %s is not in the input list.', a)
                return False
        except Exception as e:
            logging.error(e)

    def listList(self):
        logging.info('Task is to find the nested-lists present in the list.')
        nestList = []
        f = self._l
        try:
            counter = 0
            for i in f:
                if type(i) == list:
                    counter += 1
                    nestList.append(i)
                    # logging.info('Found %s number nested list.', counter)
            logging.info('There were %s number nested list in the input list.', counter)
            logging.info('The nested list elements in the input list are: %s', nestList)
            return nestList
        except Exception as e:
            logging.error(e)

    def listDict(self):
        '''This is an internal method to flatten a nested dictionary.'''
        try:
            ky = []
            vl = []
            m = self._l
            for i in m:
                if type(i) == dict:
                    for k,v in i.items():
                        ky.append(k)
                        vl.append(v)
            return ky, vl
        except Exception as e:
            logging.error(e)

    def dictKey(self):
        logging.info('Task is to find the keys of a nested dictionary inside the input list.')
        try:
            a, b = self.listDict()
            logging.info('The keys of the nested dictionaries are: %s', a)
            return a
        except Exception as e:
            logging.error(e)

    def dictValue(self):
        logging.info('Task is to find the values of a nested dictionary inside the input list.')
        try:
            a, b = self.listDict()
            logging.info('The values of the nested dictionaries are: %s', b)
            return b
        except Exception as e:
            logging.error(e)

l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]

a = listMan(l)
a.listReverse()

a.listFind(234)

a.listFind(456)

a.listList()

a.listFind('sudh')

a.dictKey()

a.dictValue()





