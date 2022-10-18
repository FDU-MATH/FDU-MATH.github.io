#! /usr/bin/env python3

import pandas as pd
import os
from itertools import compress
import readFile

course_csv = '../docs/courses/courses_undergrad_2022_2023_Fall.csv'
thisSemesterName = '2022-2023学年第1学期'
strSemester = '\n\n# ' + thisSemesterName + '\n'
strPartPosts = '\n## Posts\n\n'
target_folder = '../../courses/syllabus'
to_target_folder = '../docs/classes/'

courses = pd.read_csv(course_csv, header=0)
courses = courses.values.tolist()

syllabusFileSplitList = []
syllabusFileList = []
for line in os.popen('cd ' + target_folder + '; ls;'):
    data = line.split()
    syllabusFileSplitList.append(data[0].split('-'))
    syllabusFileList.append(line.rstrip('\n'))

webFileBeforeDotList = []
webFileList = []
for line in os.popen('cd ' + to_target_folder + '; ls;'):
    data = line.split('.')
    webFileBeforeDotList.append(data[0] + '.' + data[1])
    webFileList.append(line.rstrip('\n'))

for idx in range(len(courses)):
    thisClassNumber = courses[idx][0]
    thisClassTeacher = courses[idx][3].split(',')
    for idxx in range(len(thisClassTeacher)):
        thisClassTeacher[idxx] = '<a href=\'https://fdu-math.github.io/teachers/' + thisClassTeacher[idxx].replace(' ','_') + '\'>' + thisClassTeacher[idxx] + '</a>'
    thisClassTeacher = ', '.join(thisClassTeacher)
    boolSyllabus = [syllabusFileSplitList[idxx][0] == thisClassNumber for idxx in range(len(syllabusFileSplitList))]
    whereSyllabus = list(compress(range(len(boolSyllabus)), boolSyllabus))
    hasSyllabus = (len(whereSyllabus) > 0)
    print(thisClassNumber, 'Has Syllabus: ', hasSyllabus)
    if hasSyllabus:
        strSyllabus = '\nSyllabus: <a href=\'https://fdu-math.github.io/courses/syllabus/' + syllabusFileList[whereSyllabus[0]] + '\'>点此预览或下载</a> (密码: 苏步青星罗马字全小写)\n'
    strTeacher = '\nTeacher(s): ' + thisClassTeacher + '\n\n'
    boolWebList = [thisClassNumber == webFileBeforeDotList[idxx] for idxx in range(len(webFileBeforeDotList))]
    if (len(list(compress(range(len(boolWebList)), boolWebList))) > 0): # If there exists one web page for this class
        filePath = to_target_folder + webFileList[boolWebList.index(True)]
        linesManipulateWebFile = readFile.LinesManipulate(path=filePath)
        infoSemesterWebFile = linesManipulateWebFile.readDetectSemester()
        fileLines = linesManipulateWebFile.lineList
        boolSameSemester = False
        numberSemester = len(infoSemesterWebFile)
        for idxx in range(numberSemester):
            if (infoSemesterWebFile[idxx][0] == thisSemesterName):
                boolSameSemester = True
                indexSameSemester = idxx
        if (infoSemesterWebFile == []): # If there does not exist semester parts
            if hasSyllabus:
                fileLines.append( strSemester + strSyllabus + strTeacher + strPartPosts)
            else:
                fileLines.append( strSemester + strTeacher + strPartPosts)
        else: # If there exists semester parts
            if boolSameSemester: # If there exists a same semester
                findSyllabus = linesManipulateWebFile.detectWordBySemester(index=indexSameSemester, string='Syllabus')
                findTeacher = linesManipulateWebFile.detectWordBySemester(index=indexSameSemester, string='Teacher(s)')
                findPost = linesManipulateWebFile.detectWordBySemester(index=indexSameSemester, string='Posts')
                firstLineSameSemester = infoSemesterWebFile[indexSameSemester][1]
                if (findPost == []):
                    lastfirstLineSameSemester = infoSemesterWebFile[indexSameSemester][4]
                    if (lastfirstLineSameSemester  == -1):
                        fileLines.append(strPartPosts)
                    else:
                        fileLines.insert(lastfirstLineSameSemester + 1, strPartPosts)
                if hasSyllabus:
                    if (findSyllabus == []) & (findTeacher == []):
                        fileLines.insert(firstLineSameSemester+1, strSyllabus + strTeacher)
                    elif (not (findSyllabus == [])) & (findTeacher == []):
                        fileLines.insert(firstLineSameSemester+2, strTeacher)
                    elif (findSyllabus == []) & (not (findTeacher == [])):
                        fileLines.insert(firstLineSameSemester+1, strSyllabus)
                elif (findTeacher == []):
                        fileLines.insert(firstLineSameSemester+1, strTeacher)
            else: # If there does not exist a same semester
                firstLineFirstSemester = infoSemesterWebFile[0][1]
                if hasSyllabus:
                    fileLines.insert(firstLineFirstSemester, strSemester + strSyllabus + strTeacher + strPartPosts)
                else:
                    fileLines.insert(firstLineFirstSemester, strSemester + strTeacher + strPartPosts)
        with open(filePath, "w+") as fileAlter:
            fileAlter.write('\n'.join(fileLines))
    else:
        thisClassName = courses[idx][1]
        thisClassNumberBeforeDot = thisClassNumber.split('.')[0]
        thisClassNumberAfterDot = thisClassNumber.split('.')[1]
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