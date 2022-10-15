#! /usr/bin/env python3

import os
import copy
from itertools import compress

target_folder = '../../courses/syllabus'
to_target_folder = '../docs/classes/'
file = os.popen('cd ' + target_folder + '; ls;')
file2 = os.popen('cd ' + to_target_folder + '; ls;')

namelist0 = []
for line in file:
    data = line.split()
    namelist0.append(data[0].split('-'))
namelist = copy.deepcopy(namelist0)
for idx in range(len(namelist)):
    if (namelist[idx][3] == '1') or (namelist[idx][3] == '2'):
        namelist[idx][3] = '第' + namelist[idx][3]
namelist = [[namelist[idx][0], namelist[idx][1] + '-' + namelist[idx][2] + '学年' + namelist[idx][3] + '学期'] for idx in range(len(namelist))]

namelist2 = []
namelist3 = []
for line in file2:
    data = line.split('.')
    namelist2.append(data[0] + '.' + data[1])
    namelist3.append(line.rstrip('\n'))
for idx in range(len(namelist)):
    temp = namelist[idx][0].split('.')[0]
    temp2 = namelist[idx][0].split('.')[1]
    boolList = [namelist2[idxx] == namelist[idx][0] for idxx in range(len(namelist2))]
    if (len(list(compress(range(len(boolList)), boolList))) > 0):
        thisFileName = namelist3[boolList.index(True)]
        fileLines = []
        with open(to_target_folder + thisFileName, "r") as fileAlter:
            index_line = 0
            linesTag = []
            for line in fileAlter:
                fileLines.append(line)
                spacelessLine = line.replace(' ', '')
                if spacelessLine[0] == '#':
                    taglessLine = spacelessLine.replace('#', '').rstrip('\n')
                    if (taglessLine == namelist[idx][1]):
                        linesTag.append([index_line, True])
                    elif (taglessLine[0:4].isdigit()):
                        linesTag.append([index_line, False])
                index_line = index_line + 1
        if (len(linesTag) == 0):
            fileLines.append(
                '\n# ' + namelist[idx][1] + '\n'
                '<a href=\'https://fdu-math.github.io/courses/syllabus/' + namelist0[idx][0] + '-' + namelist0[idx][1] + '-' + namelist0[idx][2] + '-' + namelist0[idx][3] + ' (Encrypted).pdf\'>课程大纲</a>\n\n'
            )
        else:
            boolListLinesTag = [linesTag[idxx][1] for idxx in range(len(linesTag))]
            trueLinesTag = list(compress(range(len(boolListLinesTag)), boolListLinesTag))
            if (len(trueLinesTag) > 0):
                if (trueLinesTag[0] + 1 == len(boolListLinesTag)):
                    search_range = [linesTag[0][0], index_line]
                else:
                    search_range = [linesTag[trueLinesTag[0]][0], linesTag[trueLinesTag[0] + 1][0]]
                with open(to_target_folder + thisFileName, "r") as fileAlter:
                    index_line = 0
                    findBool = False
                    for line in fileAlter:
                        if (index_line >= search_range[0]) & (index_line <= search_range[1]):
                            if (line.find('课程大纲') != -1):
                                findBool = True
                        index_line = index_line + 1
                    if (findBool == False):
                        fileLines.insert(search_range[0]+1,
                            '<a href=\'https://fdu-math.github.io/courses/syllabus/' + namelist0[idx][0] + '-' + namelist0[idx][1] + '-' + namelist0[idx][2] + '-' + namelist0[idx][3] + ' (Encrypted).pdf\'>课程大纲</a>\n\n'
                        )
            else:
                fileLines.insert(linesTag[0][0], 
                    '\n# ' + namelist[idx][1] + '\n'
                    '<a href=\'https://fdu-math.github.io/courses/syllabus/' + namelist0[idx][0] + '-' + namelist0[idx][1] + '-' + namelist0[idx][2] + '-' + namelist0[idx][3] + ' (Encrypted).pdf\'>课程大纲</a>\n\n'
                )
        with open(to_target_folder + thisFileName, "w+") as fileAlter:
            fileAlter.write(''.join(fileLines))
    else:
        with open(to_target_folder + namelist[idx][0] + '.md', "w") as file:
            file.write(
                '---\n'
                'title: \'[' + namelist[idx][0] +']\'\n'
                'layout: single\n'
                'permalink: /courses/class-id/' + temp + '-' + temp2 + '\n'
                'author_profile: true\ntoc: true\n'
                'toc_label: \'目录\'\n'
                'toc_sticky: true\n'
                '---\n'
                '\n'
                '<div class=\'notice--warning\'>\n'
                '\t<p><i><a rel=\'license\' href=\'http://creativecommons.org/licenses/by-nc-sa/4.0/\'><img alt=\'Creative Commons License\' style=\'border-width:0\' src=\'https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png\' /></a><br /> The content of this webpage is licensed under a <a rel=\'license\' href=\'http://creativecommons.org/licenses/by-nc-sa/4.0/\'>Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.</i></p>\n'
                '</div>\n'
                '\n'
                '<a href=\'https://fdu-math.github.io/courses/' + temp +'\'>链接至[' + temp + ']课程页面</a>\n'
                '\n# ' + namelist[idx][1] + '\n'
                '<a href=\'https://fdu-math.github.io/courses/syllabus/' + namelist0[idx][0] + '-' + namelist0[idx][1] + '-' + namelist0[idx][2] + '-' + namelist0[idx][3] + ' (Encrypted).pdf\'>课程大纲</a>\n\n'
            )