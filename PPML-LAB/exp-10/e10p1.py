class parent:
    def parent_method(self):
        print("properties of parent ")
class child(parent):
    def child_method(self):
        print("properties of child")
ch=child()
ch.parent_method()
ch.child_method()