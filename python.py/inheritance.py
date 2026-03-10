'''
single inheritence
multilevel inheritance
multiple inheritance
hierachical inheritance
'''
#class owner():
    def output(self):
        print("i am the owner")
#class emp(owner):
  #  def outputemp(self):
   #     print("i am the employee")
        
#emp=emp()
#emp.outputemp()
#emp.output()

class father():
    def output(self):
        print("i am the father")

class mother():
    def output(self):
        print("i am the mother")

class child(father,mother):
    def outputc(self):
        print("i am the child")
child=child()
child.outputc()
child.outputfather()
child.outputmother()
child.output()