#! /usr/bin/env python3

import pandas as pd
import os
import copy
from itertools import compress
import readFile

def courses2html(file, target_html):
    if os.path.exists(target_html):
        os.remove(target_html)
    test_html = './fsia09i32wr.txt'
    for idx in range(len(file)):
        tmp = file['教师'].values.tolist()[idx]
        tmp2 = file['职称'].values.tolist()[idx]
        tmp3 = file['课程序号'].values.tolist()[idx]
        # tmp4 = file["课程名称"].values.tolist()[idx]
        tmp5 = copy.deepcopy(tmp3)
        tmp = tmp.split(',')
        tmp2 = tmp2.split(',')
        tmp3 = tmp3.split('.')
        for idxx in range(len(tmp)):
            tmp[idxx] = '<a href=\'https://fdu-math.github.io/teachers/' + tmp[idxx].replace(' ','_') + '\'>' + tmp[idxx] + '</a>'
            if tmp2[idxx] == '':
                tmp2[idxx] = 'Null'
        file.iloc[idx, 3] = '<br />'.join(tmp)
        file.iloc[idx, 4] = '<br />'.join(tmp2)
        # file.iloc[idx, 1] = '<a href=\'https://fdu-math.github.io/courses/' + tmp3[0] + '\'>' + tmp4 + '</a>'
        file.iloc[idx, 0] = '<a href=\'https://fdu-math.github.io/courses/class-id/' + tmp3[0] + '-' + tmp3[1] + '\'>' + tmp5 + '</a>'
    file.to_html(test_html, index=False)
    temp1 = []
    with open(test_html,"r")as file1, open(target_html,"a")as file2:
        for line in file1:
            temp1.append(line)
        for line in temp1:
            file2.write(str(line).replace('&lt;','<').replace('&gt;','>'))
    os.remove(test_html)

course_csv = '../docs/courses/courses_undergrad_2022_2023_Fall.csv'
thisSemesterName = '2022-2023学年第1学期'
thisSemesterAbbreviation = '2223F'
strSemester = '\n### ' + thisSemesterName + '\n\n'
to_target_folder = '../docs/courses/'

courses_df = pd.read_csv(course_csv, header=0)
courses = courses_df.values.tolist()
allClassesThisSemesterBeforeDot = [courses[idxx][0].split('.')[0] for idxx in range(len(courses))]
allCoursesThisSemester = list(set(allClassesThisSemesterBeforeDot))

webFileBeforeDotList = []
webFileList = []
for line in os.popen('cd ' + to_target_folder + '; ls;'):
    webFileBeforeDotList.append(line.split('.')[0])
    webFileList.append(line.rstrip('\n'))

strPartClasses = '''## 开设课程\n
**站务提示:** 只提供近一学年的课程清单, 之前学期的课程清单参见<a href=\'https://fdu-math.github.io/courses/MATH130009/courses-archived\' style=\'color: blue; text-decoration: underline;\'>此处</a>, 但2022-2023学年之前的课程清单暂不提供.
{: .notice}
'''
strPartPosts = '\n#### Posts\n\n'

for idx in range(len(allCoursesThisSemester)):
    thisCourseNumber = allCoursesThisSemester[idx]
    boolClasses = [allClassesThisSemesterBeforeDot[idxx] == thisCourseNumber for idxx in range(len(allClassesThisSemesterBeforeDot))]
    thisCourseName = courses[list(compress(range(len(boolClasses)), boolClasses))[0]][1]
    courses2html(courses_df[courses_df['课程名称'] == thisCourseName], './test.txt')
    strTable = []
    index_line = 0
    with open('./test.txt', 'r') as file:
        for line in file:
            if (index_line == 0):
                strTable.append('\n#### 课程清单\n\n<div style=\'text-align: center;\' id=\'' + thisCourseNumber + '_' + thisSemesterAbbreviation + '\'> <table id=\'' + thisCourseNumber + '_' + thisSemesterAbbreviation + '_table\'>\n')
            else:
                strTable.append(line)
            index_line = index_line + 1
    strTable.append('</div>\n')
    strTable = ''.join(strTable)
    os.remove('./test.txt')
    boolWebList = [thisCourseNumber == webFileBeforeDotList[idxx] for idxx in range(len(webFileBeforeDotList))]
    if (len(list(compress(range(len(boolWebList)), boolWebList))) > 0): # If there exists one web page for this course
        filePath = to_target_folder + webFileList[boolWebList.index(True)]
        linesManipulateWebFile = readFile.LinesManipulate(path=filePath)
        infoSemesterWebFile = linesManipulateWebFile.readDetectSemester()
        fileLines = linesManipulateWebFile.lineList
        boolSameSemester = False
        for idxx in range(len(infoSemesterWebFile)):
            if (infoSemesterWebFile[idxx][0] == thisSemesterName):
                boolSameSemester = True
                indexSameSemester = idxx
        if (infoSemesterWebFile == []): # If there does not exist semester parts
            if (linesManipulateWebFile.fileStructure.items == []):
                fileLines.append( strPartClasses + strSemester + strTable + strPartPosts)
            else:
                fileLines.insert(linesManipulateWebFile.fileStructure.items[0][1], strPartClasses + strSemester + strTable + strPartPosts)
        elif not boolSameSemester: # If there exists semester parts and does not exist a same semester
            fileLines.insert(infoSemesterWebFile[0][1], strSemester + strTable + strPartPosts)
        with open(filePath, "w+") as fileAlter:
            fileAlter.write('\n'.join(fileLines))
    else:
        with open(to_target_folder + thisCourseNumber + '.md', "w") as file:
            strPartHead = '''---
title: \'''' + thisCourseName + '[' + thisCourseNumber + ''']\'
layout: single
permalink: /courses/''' + thisCourseNumber + '''
author_profile: true
toc: true
toc_label: \'目录\'
toc_sticky: true
---\n\n
<div class=\'notice--warning\'>
\t<p><i><a rel=\'license\' href=\'http://creativecommons.org/licenses/by-nc-sa/4.0/\'><img alt=\'Creative Commons License\' style=\'border-width:0\' src=\'https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png\' /></a><br /> The content of this webpage is licensed under a <a rel=\'license\' href=\'http://creativecommons.org/licenses/by-nc-sa/4.0/\'>Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.</i></p>
</div>\n'''
            file.write(strPartHead + strSemester + strTable + strPartPosts) 