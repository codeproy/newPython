class Counter(object):

        instances = 0

        def __init__(self):
                print('constructor called')
                Counter.instances +=1
                self._value = 0
                self.reset()

        def reset(self):
                self._value = 0

        def increment(self,amount = 1):
                self._value += amount

        def decrement(self , amount = 1):
                self._value -= amount


        def getValue(self):
                return self._value

        def __str__(self):
                return str(self._value)
