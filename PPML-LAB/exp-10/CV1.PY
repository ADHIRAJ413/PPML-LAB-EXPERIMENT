class parent:
    def sam(self):
        print("sam is parent ")

class child(parent):
    def sam(self):
        print("i am son of sam")

s1=child()
s1.sam()        
s2=parent()
s2.sam()