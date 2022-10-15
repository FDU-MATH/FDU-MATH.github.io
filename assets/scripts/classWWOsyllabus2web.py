#! /usr/bin/env python3

import pandas as pd
import os
from itertools import compress

course_csv = '../docs/courses/courses_undergrad_2022_2023_Fall.csv'
thisSemesterName = '2022-2023学年第1学期'
strSemester = '\n\n# ' + thisSemesterName + '\n'
strPartPosts = '\n## Posts\n\n'
target_folder = '../../courses/syllabus'
to_target_folder = '../docs/classes/'

courses = pd.read_csv(course_csv, header=0)
courses = courses.values.tolist()
allClassesThisSemester = [courses[idxx][0] for idxx in range(len(courses))]

terminalSyllabusFileIntegral = os.popen('cd ' + target_folder + '; ls;')
syllabusFileSplitList = []
syllabusFileList = []
for line in terminalSyllabusFileIntegral:
    data = line.split()
    syllabusFileSplitList.append(data[0].split('-'))
    syllabusFileList.append(line.rstrip('\n'))

terminalWebFileIntegral = os.popen('cd ' + to_target_folder + '; ls;')
webFileBeforeDotList = []
webFileList = []
for line in terminalWebFileIntegral:
    data = line.split('.')
    webFileBeforeDotList.append(data[0] + '.' + data[1])
    webFileList.append(line.rstrip('\n'))

for idx in range(len(allClassesThisSemester)):
    thisClassNumber = courses[idx][0]
    thisClassName = courses[idx][1]
    thisClassTeacher = courses[idx][3].split(',')
    for idxx in range(len(thisClassTeacher)):
        thisClassTeacher[idxx] = '<a href=\'https://fdu-math.github.io/teachers/' + thisClassTeacher[idxx].replace(' ','_') + '\'>' + thisClassTeacher[idxx] + '</a>'
    thisClassTeacher = ', '.join(thisClassTeacher)
    boolSyllabus = [syllabusFileSplitList[idxx][0] == thisClassNumber for idxx in range(len(syllabusFileSplitList))]
    whereSyllabus = list(compress(range(len(boolSyllabus)), boolSyllabus))
    hasSyllabus = (len(whereSyllabus) > 0)
    print(thisClassNumber, hasSyllabus)
    if hasSyllabus:
        strSyllabus = '<a href=\'https://fdu-math.github.io/courses/syllabus/' + syllabusFileList[whereSyllabus[0]] + '\'>课程大纲</a>\n'
    strTeacher = '\n任课教师: ' + thisClassTeacher + '\n\n'
    thisClassNumberBeforeDot = thisClassNumber.split('.')[0]
    thisClassNumberAfterDot = thisClassNumber.split('.')[1]
    boolWebList = [thisClassNumber == webFileBeforeDotList[idxx] for idxx in range(len(webFileBeforeDotList))]
    if (len(list(compress(range(len(boolWebList)), boolWebList))) > 0): # If there exists one web page for this class
        thisFileName = webFileList[boolWebList.index(True)]
        fileLines = []
        with open(to_target_folder + thisFileName, "r") as fileAlter:
            index_line = 0
            linesTag = []
            for line in fileAlter:
                fileLines.append(line)
                spacelessLine = line.replace(' ', '')
                if spacelessLine[0] == '#':
                    taglessLine = spacelessLine.replace('#', '').rstrip('\n')
                    if (taglessLine == thisSemesterName):
                        linesTag.append([index_line, True])
                    elif (taglessLine[0:4].isdigit()):
                        linesTag.append([index_line, False])
                index_line = index_line + 1
        if (len(linesTag) == 0): # If there does not exist semester parts
            if hasSyllabus:
                fileLines.append( strSemester + strSyllabus + strTeacher + strPartPosts)
            else:
                fileLines.append( strSemester + strTeacher + strPartPosts)
        else: # If there exists semester parts
            boolWebListLinesTag = [linesTag[idxx][1] for idxx in range(len(linesTag))]
            trueLinesTag = list(compress(range(len(boolWebListLinesTag)), boolWebListLinesTag))
            if (len(trueLinesTag) > 0): # If there exists a same semester
                if (trueLinesTag[0] + 1 == len(boolWebListLinesTag)):
                    search_range = [linesTag[0][0], index_line]
                else:
                    search_range = [linesTag[trueLinesTag[0]][0], linesTag[trueLinesTag[0] + 1][0]]
                with open(to_target_folder + thisFileName, "r") as fileAlter:
                    index_line = 0
                    findSyllabusBool = False
                    findTeacherBool = False
                    findPostBool = False
                    for line in fileAlter:
                        if (index_line >= search_range[0]) & (index_line <= search_range[1]):
                            if (line.find('课程大纲') != -1):
                                findSyllabusBool = True
                            if (line.find('任课教师') != -1):
                                findTeacherBool = True
                                thisLine = index_line
                            if (line.find('Post') != -1):
                                findPostBool = True
                        index_line = index_line + 1
                    if hasSyllabus:
                        if (findSyllabusBool == False) & (findTeacherBool == False):
                            if (findPostBool == False):
                                fileLines.insert(search_range[0]+1, strSyllabus + strTeacher)
                            else:
                                fileLines.insert(search_range[0]+1, strSyllabus + strTeacher)
                        elif (findSyllabusBool == True) & (findTeacherBool == False):
                            if (findPostBool == False):
                                fileLines.insert(search_range[0]+2, strTeacher + strPartPosts)
                            else:
                                fileLines.insert(search_range[0]+2, strTeacher)
                        elif (findSyllabusBool == False) & (findTeacherBool == True):
                            if (findPostBool == False):
                                fileLines.insert(thisLine+1, strPost)
                                fileLines.insert(search_range[0]+1, strSyllabus)
                            else:
                                fileLines.insert(search_range[0]+1, strSyllabus)
                    else:
                        if (findTeacherBool == False):
                            fileLines.insert(search_range[0]+1, strTeacher)
            else: # If there does not exist a same semester
                if hasSyllabus:
                    fileLines.insert(linesTag[0][0], strSemester + strSyllabus + strTeacher + strPartPosts)
                else:
                    fileLines.insert(linesTag[0][0], strSemester + strTeacher + strPartPosts)
        with open(to_target_folder + thisFileName, "w+") as fileAlter:
            fileAlter.write(''.join(fileLines))
    else:
        with open(to_target_folder + thisClassNumber + '.md', "w") as file:
            strPartHead = '''---
title: \'''' + thisClassName + '[' + thisClassNumber + ''']\'
layout: single
permalink: /courses/class-id/''' + thisClassNumberBeforeDot + '-' +  thisClassNumberAfterDot + '''
author_profile: true
toc: true
toc_label: \'目录\'
toc_sticky: true
---\n\n
<div class=\'notice--warning\'>
\t<p><i><a rel=\'license\' href=\'http://creativecommons.org/licenses/by-nc-sa/4.0/\'><img alt=\'Creative Commons License\' style=\'border-width:0\' src=\'https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png\' /></a><br /> The content of this webpage is licensed under a <a rel=\'license\' href=\'http://creativecommons.org/licenses/by-nc-sa/4.0/\'>Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.</i></p>
</div>\n
<a href=\'https://fdu-math.github.io/courses/''' + thisClassNumberBeforeDot + '\'>链接至[' + thisClassNumberBeforeDot + ']课程页面</a>\n'
            if hasSyllabus:
                file.write(strPartHead + strSemester + strSyllabus + strTeacher + strPartPosts)
            else:
                file.write(strPartHead + strSemester + strTeacher + strPartPosts)