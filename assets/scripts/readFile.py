#! /usr/bin/env python3

class fileStructure:
    def __init__(self, path: str = ''):
        self.path = path
        self.items = []

    def addItem(self, content: str, lineNum: int, level: int):
        self.items.append([content, lineNum, level, None, # Parent Line Number
        ])
        if (len(self.items) > 1):
            thisLevel = self.items[-1][2]
            for idx in range(len(self.items) - 1):
                idx = -(idx + 2)
                thatLevel = self.items[idx][2]
                if (thisLevel > thatLevel):
                    self.items[-1][3] = self.items[idx][1]
                    break
                elif (thisLevel == thatLevel):
                    self.items[-1][3] = self.items[idx][3]
                    break
    
    def checkLastLine(self) -> list:
        numItems = len(self.items)
        for idx in range(numItems):
            self.items[idx].append(-1)
        for idx in range(numItems):
            thisLevel = self.items[idx][2]
            for idxx in range(idx+1, numItems):
                thatLevel = self.items[idxx][2]
                if (thisLevel >= thatLevel):
                    self.items[idx][4] = self.items[idxx][1] - 1

    def detectSemesterFudan(self) -> list:
        self.semesterDetect = []
        for idx in range(len(self.items)):
            if (self.items[idx][0][0:4].isdigit()) & (self.items[idx][0][5:9].isdigit()):
                self.semesterDetect.append(self.items[idx])
        return self.semesterDetect
    
    def selectSemesterFudanLevelByIndex(self, index: int) -> list:
        list = []
        level = self.semesterDetect[index][2]
        for idx in range(len(self.semesterDetect)):
            if (self.semesterDetect[idx][2] == level):
                list.append(self.semesterDetect[idx])
        return list

class LinesManipulate:
    def __init__(self, path: str):
        self.path = path
        self.lineList = []
    
    def readLines(self, rstripChar: str = '', splitChar: str = ''):
        self.lineList = []
        with open(self.path, 'r') as file:
            for line in file:
                if splitChar == '':
                    self.lineList.append(line.rstrip(rstripChar))
                else:
                    self.lineList.append(line.rstrip(rstripChar).split(splitChar))

    def detectMarkdownStructure(self) -> fileStructure:
        self.fileStruct = fileStructure(path = self.path)
        for idx in range(len(self.lineList)):
            thisLine = self.lineList[idx].lstrip(' ').rstrip(' ').rstrip('#').rstrip(' ')
            numBefore = len(thisLine)
            thisLine = thisLine.lstrip('#')
            level = numBefore - len(thisLine) - 1
            if (level != -1):
                thisLine = thisLine.lstrip(' ')
                self.fileStruct.addItem(content=thisLine, lineNum=idx, level=level)
        self.fileStruct.checkLastLine()
        return self.fileStruct
    
    def detectWord(self, string: str = '', startLine: int = -1, endLine: int = -1) -> list:
        if (string == '') | (self.lineList == []):
            return []
        else:
            list = []
            theLength = len(self.lineList)
            theRange = range(theLength)
            if (startLine != -1) | (endLine != -1):
                if (startLine != -1) & (endLine == -1):
                    theRange = range(startLine, theLength)
                elif (startLine == -1) & (endLine != -1):
                    theRange = range(0, endLine + 1)
                else:
                    theRange = range(startLine, endLine + 1)
            for idx in theRange:
                if (self.lineList[idx].find(string) != -1):
                    list.append(idx)
            return list
        
    def readDetectSemester(self) -> list:
        self.readLines(rstripChar='\n')
        self.detectMarkdownStructure()
        return self.fileStruct.detectSemesterFudan()

    def selectItemsBySemesterLevel(self, index: int) -> list:
        return self.fileStruct.selectSemesterFudanLevelByIndex(index=index)

    def detectWordBySemester(self, string: str, index: int) -> list:
        return self.detectWord(string=string, startLine=self.fileStruct.semesterDetect[index][1], endLine=self.fileStruct.semesterDetect[index][4])

'''
MD = '../../_pages/courses.md'
A = LinesManipulate(path=MD)
List = A.readDetectSemester()
List2 = A.selectItemsBySemesterLevel(index=0)
List3 = A.detectWordBySemester(string = '泛函分析', index=0)
print(List, List2, List3)
'''
