class parent:
    def sam(self):
        print("sam is parent ")

class child(parent):
    def saam(self):
        print("i am son of sam")

class pre(child):
    def das(self):
        print(" my family")

s1=pre()
s1.das()
s1.saam()
s1.sam()
