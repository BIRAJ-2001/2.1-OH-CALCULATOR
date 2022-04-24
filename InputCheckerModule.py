class inputbinary():
    def __init__(self, fingbin=[0,0,0,0,0]):
        self.fingbin = fingbin
    def statusprocessing(self, flist):
        s = 0
        op = ''
        if flist == [0,0,0,0,1]:
            op = '+'
        elif flist == [0,0,0,1,1]:
            op = '-'
        elif flist == [1,1,0,0,1]:
            op = '*'
        elif flist == [0,1,0,0,1]:
            op = '/'
        elif flist == [0,0,1,1,1]:
            op = '='
        elif flist == [1,0,0,0,0]:
            s = 6
        elif flist == [1,1,0,0,0]:
            s = 7
        elif flist == [1,1,1,0,0]:
            s = 8
        elif flist == [1,1,1,1,0]:
            s = 9
        elif flist == [0,0,0,0,0]:
            s = 0
        elif flist == []:
            op = '0'
        else:
            for i in range(0,len(flist)):
                s = s+ flist[i]
        return s, op

    def operation(self,a,b,op):
        s=0
        if op=='+' or op=='':
            s=a+b
        elif op == '-':
            s=a-b
        elif op == '*':
            s = a * b
        elif op == '/':
            if b!=0:
                s = a/b
        elif op == '=':
            s=a
        return s


def main():
    op = inputbinary()
    flist=[]
    print("enter the status of fingers in binary:")
    #fingers status is input as 0 or 1(0 means closed,1 means open),first index finger status
    #and last thumb status
    for i in range(0,5):
        ip = int(input())
        if ip == 0 or ip == 1:
            flist.append(ip)
        else:
            print("wrong input")
            break
    print(flist)
    x = op.statusprocessing(flist)
    print(x)
if __name__ == "__main__":
    main()
