#Instance method

class Student:
  def __init__( self, name, marks ):
   self.name = name 
   self.marks= marks
  def change_stream(cls, new_stream):
   cls.change_stream = new_stream
   print("Name :", {self.name})
   print("Marks: ", {self.marks})

Student.change_stream("MTECH")
s1 = Student.

#class method

