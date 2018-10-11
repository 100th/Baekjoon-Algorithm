class Stack:
    def __init__(self):
        self.A=[]

    def isEmpty(self):
        return self.A==[]

    def push(self,item):
        self.A.append(item)

    def pop(self):
        n=len(self.A)
        temp = ""
        if n!=0:
            temp= self.A[n-1]
            del self.A[n-1]
        return temp

    def clear(self):
        self.A=[]

    def peek(self):
        n=len(self.A)
        if n>0: return self.A[n-1]

    def stackPrint(self):
        n = len(self.A)
        if n>0:
            for i in range(0,n):
                print(self.A[n-1-i])



class eqCalc:
    def __init__(self, eq):
        self.eq=eq
        A = Stack()
        self.synError = False
        for ch in eq:
            if ch == "(":
                A.push("(")
            elif ch == ")":
                if A.isEmpty() == False:
                    popCh = A.pop()
                else:
                    self.synError = True
        if A.isEmpty() == False: self.synError = True

    def getPostCalc(self):
        eqStack=Stack()
        tokens=self.eq.split(" ")
        postFix=""
        print(tokens)
        for ch in tokens:
            if ch=="(": eqStack.push(ch)
            elif ch==")":
                while(True):
                    temp = eqStack.pop()
                    if temp!="(": postFix += temp+" "
                    else: break
            elif ch=="+" or ch=="-":
                while(True):
                    if self.operYN(eqStack.peek())==True:
                        postFix += eqStack.pop()+" "
                    else:
                        break
                eqStack.push(ch)
            elif ch == "*" or ch == "/":
                while(True):
                    if eqStack.peek()=="*" or eqStack.peek()=="/":
                        postFix += eqStack.pop() +" "
                    else:
                        break
                eqStack.push(ch)
            else:
                postFix += ch+" "

        while (eqStack.isEmpty()!=True): postFix += eqStack.pop() + " "
        print(postFix)

        tokens=postFix.split(" ")
        eqStack.clear()
        for ch in tokens:
            if self.operYN(ch)==False:
                eqStack.push(ch)
            else:
                b=float(eqStack.pop())
                a=float(eqStack.pop())
                if ch=="*": eqStack.push(a*b)
                elif ch=="/": eqStack.push(a/b)
                elif ch == "+": eqStack.push(a+b)
                else: eqStack.push(a-b)

        result=""
        while(eqStack.isEmpty()!=True):  result += str(eqStack.pop())
        return (result)

    def operYN(self,item):
        if item=="*": return True
        elif item=="/": return True
        elif item=="+": return True
        elif item == "-": return True
        else: return False

A="( 6 + 5 * ( 2 - 8 ) / 2 )"
eq1=eqCalc(A)
print(eq1.synError)
print(eq1.getPostCalc())
