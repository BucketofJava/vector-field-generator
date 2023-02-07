import math
def empty(x):
    return x;
op_dict={'':empty, '_':None, '+':float.__add__, '-':float.__sub__, '*':float.__mul__, '/':float.__truediv__, 'sin':math.sin, 'cos':math.cos, 'tan':math.tan}
ops=list(op_dict.keys())
class func_parser():
    def __init__(self, func_unit):
        self.func_unit=func_unit;
    def __call__(self, x, y=None):
        return runProcess(self.func_unit, x, y)
def interpret(string):
    funcString=string.replace(" ", "")
    return func_parser(func_unit=processUnit(funcString))
def processUnit(string):
    prevop=0;
    paren=-1;
    func=empty;
    func_list=[]
    num_open=0;
    num_close=0;
    try:
        return [float(string)]
    except ValueError:
        pass
    except NotImplementedError as e:
        print(e.with_traceback())
    if(string=='x'):
        return ['x']
    if(string=='y'):
        return ['y']
    for i in range(len(string)):
        c=string[i]
        if(paren!=-1):
            if(c=='('):
                num_open+=1;
            if(c==')' and num_open==num_close):
                if(func!=None):
                    func_list.append(func)
             #   print(string[paren+1:i])
                func_list.append(processUnit(string[paren+1:i]))
                paren=-1
                num_open=0
                num_close=0;
            elif(c==')'):
                num_close+=1
            continue;
        #check for open parentheses
        if(c=='('):
            op=string[prevop:i]
            if(len(op)>0 and not op in ops):
                return fail
            paren=i
            func=op_dict[op]
        if(c in "+-*/_"):
            prevop=i
    return func_list
def runProcess(process, x, y=None):
    if(process==['x']):
      #  print(x)
        return x;
    if(process==['y']):
        return y;
  #  print(process)
    if(len(process)==1):
      #  print(int(process[0]))
        return float(process[0])
    if(str(type(process[0]))!="<class 'list'>"):
        ran=[]
        for i in range(1, len(process)):
            ran.append(runProcess(process[i], x, y))
       # print(process[0](*ran))
        return process[0](*ran)

            




        #check for operation
def fail():
    print("Failed to parse. Please check your syntax")

# process=interpret(input("Input equation:: ")).func_unit
# print(process)
# print(runProcess(process, float(input("x:: ")), float(input("y:: "))))
