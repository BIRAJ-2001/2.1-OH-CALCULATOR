
class BinaryListMaker():
    def __init__(self, lmlist = [], label = ''):
        self.lmlist = lmlist
        self.label = label

    def BinaryList(self, lmlist, label):
        fing = []
        tips = [4, 8, 12, 16, 20]
        if len(lmlist) != 0:
            for i in range(0,5):
                if i == 0 and lmlist[tips[i]][1] > lmlist[3][1] and label == 'Left':
                   fing.append(1)
                elif i == 0 and lmlist[tips[i]][1] < lmlist[3][1] and label == 'right':
                   fing.append(1)
                elif lmlist[tips[i]][2] < lmlist[tips[i]-2][2] and i!=0:
                   fing.append(1)
                else:
                   fing.append(0)
        return fing

