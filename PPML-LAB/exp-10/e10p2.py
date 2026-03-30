class grand_parent:
    def gp_property(self):
     print("inside grandparent method")
class parent(grand_parent):
    def business(self):
     print("inside parent business method")
class child(parent):
    def education(self):
     print("inside child education method")
ch=child()
ch.gp_property()    
ch.business()
ch.education()