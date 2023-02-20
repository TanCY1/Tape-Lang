'''brainfuck compiler in python'''
import sys
try:
    file=open(sys.argv[1:2][0],"r").read()
except:
    file=""
try:
    param=sys.argv[2:3][0]
except:
    param=""

#file=""
pointer=0
tape={}
isLooping=False
loopStack=[]
innerLoops=0
skip=0
out=""

def listinit(offset=0):
    try:
        _=tape[pointer+offset]
    except KeyError:
        tape[pointer+offset]=0

def sortList(dictionary: dict) ->dict :
    pass
    

loopNumber=0
def evaluate(start=0,end=len(file)):
    global pointer
    global tape
    global innerLoops
    global isLooping
    global loopStack
    global loopNumber
    global skip
    global out
    i=0
    while i!=len(file):
        listinit()
        char=file[i]
        if param == "debug":
            print(f"tape pointer at {pointer} with data {tape[pointer]} executing code {file[i]}")
        if isLooping:
            if char=="[":
                innerLoops+=1
            if char=="]":
                if innerLoops==0:
                    isLooping=False
                else: innerLoops-=1
            continue
        if char==">":
            pointer+=1
        if char=="<":
            pointer-=1
        if char=="+":
            listinit()
            tape[pointer]=tape[pointer]+0b1
        if char=="-":
            listinit()
            tape[pointer]=int(tape[pointer])-1
        if char==".":
            listinit()
            out=out+chr(tape[pointer])
        if char==";":
            listinit()
            userinput=input()
            if userinput == "end":
                print(tape)
                break
            else:
                if len(userinput)>1:
                    for j in userinput:
                        tape[pointer+userinput.index(j)]=ord(j)
                else:
                    tape[pointer]=ord(userinput)
        if char==",":
            listinit()
            userinput=input()
            if userinput == "end":
                print(tape)
                break
            else:
                tape[pointer]=ord(userinput)
        if char==":":
            k=0
            while True:
                listinit(k)
                if tape[pointer+k]!=0:
                    listinit(k)
                    out=out+chr(tape[pointer+k])
                    k+=1
                else: break
        if char=="[":
            if tape[pointer]==0:
                isLooping=True
            else:
                loopStack.append(i)
        if char =="]":
            if tape[pointer]!=0:
                i=loopStack[len(loopStack)-1]
            else:
                loopStack.pop()
        i+=1
    print(out)
    
    if param=="debug":
        print(tape)

evaluate()




