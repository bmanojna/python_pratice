'''
wrapping of variables methods in a single unit is called encapsulation.
public
private (__) double underscore means private
protected (_) single underscore means protected
'''
class demo():
    def __init__(self,a,b):
        self.__a=a # private
        self._b=b #protected
class demo2(demo):
    def output(self):
        print(self._b)
  d=demo2(3,4)
  d.output()



