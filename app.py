class Jar:

    def __init__(self, capacity = 12):

        self._cookie = ''
        self.__capacity = capacity

        return


    def __str__(self):
        return f"{self._cookie}"

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, x):

        '''
            #   Rules for how to use the capacity attribute
            #   Raising valueError if the capacity is less than 1

        '''

        if x < 1: raise ValueError("Capacity must be greater than 0")

        self.__capacity = x
        
        return self.__capacity

    @property
    def size(self):
        return self._cookie

    @size.setter
    def size(self, n):

        if (len(n) + len(self._cookie)) > self.__capacity: 
            raise ValueError("Exceeding the capacity of the jar")
        
        if (len(n) - len(self._cookie)) < 0: 
            raise ValueError("Can not have less than zero cookies")
        
        self._cookie = n if '🍪' in n else "zero cookies"

        return self._cookie

    def deposit(self, x):

        if x > self.__capacity or (len(self._cookie) + x) > self.__capacity:
            raise ValueError(f'Can only deposit between 1-{self.__capacity} cookie(s)')
        
        self._cookie = (len(self._cookie) + x) * '🍪'

    def withdraw(self, x):

        if x > len(self._cookie) or x < 1: 
            raise ValueError('Can not withdraw that much cookies')

        self._cookie = (len(self._cookie) - x) * '🍪'

if __name__ == "__main__":

    jar = Jar()
    jar.capacity = 13
    print(jar.capacity)
    print(jar.size)
    jar.deposit(10)
    print(jar.size)
    jar.withdraw(1)
    print(jar.size)