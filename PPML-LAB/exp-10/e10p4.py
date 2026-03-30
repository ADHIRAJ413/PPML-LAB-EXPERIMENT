class parent:
  def show(self):
     print("inside parent show method")
class child(parent):
    def show(self):
         print("inside child show method")
ch=child()
ch.show()