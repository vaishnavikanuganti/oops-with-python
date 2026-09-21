class__init__(self,name,branch):
self.name = name
self.branch = branch


def display(self):
  print(self.name, "-", self.branch)


s1 = student("vaishnavi", "AIML")
s2 = student("swathi", "CSE")
s3 = student("manasa", "ECE")

s1.diaplay()
s2.display()
s3.display()
