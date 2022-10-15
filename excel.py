import xlsxwriter
import numpy as np
class excel:
    def __init__(self, name):
        self.workbook = xlsxwriter.Workbook(name)
        self.worksheet = self.workbook.add_worksheet()
        self.arr = []
        self.letter = 'A'
        self.globalCount = 1

    def charac(self, word):
        wordConveted = ""
        invertedWord = word[::-1]

        numeric = -1
        for i, charac in enumerate(invertedWord):
            if i-1 == numeric:
                if charac == "Z":
                    if(i == len(invertedWord)-1):
                        wordConveted += "A"
                    numeric = i
                    wordConveted += chr( ord(charac)-25 )
                else:
                    wordConveted += chr( ord(charac) + 1 )
            else:
                wordConveted += charac


        return wordConveted[::-1]

    def write(self, arr):
        key = sumArr = 0
        for ar in arr:
            if isinstance(ar, (int,np.integer)):
                sumArr += ar
            self.worksheet.write(self.letter + str(self.globalCount), ar)
            self.letter = self.charac(self.letter)
            key += 1
        print("Saved "+str(self.globalCount))
        self.globalCount += 1
        self.letter = 'A'
        return sumArr
    
    def close():
        self.workbook.close()

        