class HandStatus():
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def label(self, a, b):
        label = ""
        if a>b:
            label = "Left"
        else:
            label = "right"
        return label
def main():
    hs = HandStatus()
    x = input(int)
    y = input(int)
    label = ""
    label = hs.label(x,y)
    print(label)

if __name__ == "__main__":
    main()
