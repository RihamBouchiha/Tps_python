class myString:
    def __init__(self, str):
        self.str = str

    def append(self, added_str):
        return self.str + added_str

    def pop(self, index):
        str = ""
        for i, value in enumerate(self.str):
            if i == index:
                continue
            str += value
        print(str)


s1 = myString("Hello")
print(s1.append(" world!"))
s1.pop(2)
