class father:
    def skill1(self):
        print("inside father's  skill method")
class mother:
    def skill2(self):
        print("inside mother's skill method")
class child(father,mother):
    def skill3(self):
        print("inside child's skill method")
ch=child()
ch.skill1()
ch.skill2()
ch.skill3()