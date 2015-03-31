class queue(object):
    def __init__(self):
        self.vals=[]
    def insert(self,x):
        self.vals.append(x)
    def remove(self):
        try:
            print(str(self.vals[0]))
            self.vals.remove(self.vals[0])
        except:
            raise ValueError("queue is empty")
            