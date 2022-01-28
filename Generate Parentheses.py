# Generate Parentheses
def __init__(self):
    self.para=[]

def generateParenthesis(self, n):
    self.genHelper('',n,n)
    return self.para

def genHelper(self,string,open,close):
    if open==0 and close==0:
        self.para.append(string)
    else:
        if open>0:
            self.genHelper(string+'(',open-1,close)
        if close>open:
            self.genHelper(string+')',open,close-1)
