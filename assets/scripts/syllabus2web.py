#! /usr/bin/env python3

import os
import copy

target_folder = '../docs/courses/syllabus'
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
for line in file2:
    data = line.split()
    namelist2.append(data[0])
for idx in range(len(namelist)):
    temp = namelist[idx][0].split('.')[0]
    if (namelist2 == namelist[idx][0]):
        print(namelist[idx][0])
    else:
        with open(to_target_folder + namelist[idx][0] + '.md', "w") as file:
            file.write(
                '---\ntitle: \'[' + namelist[idx][0] +']\'\nlayout: single\npermalink: /courses/class-id/' + namelist[idx][0] + '\nauthor_profile: true\ntoc: true\ntoc_label: \'目录\'\ntoc_sticky: true\n---\n\n<div class=\'notice--warning\'>\n<p><i><a rel=\'license\' href=\'http://creativecommons.org/licenses/by-nc-sa/4.0/\'><img alt=\'Creative Commons License\' style=\'border-width:0\' src=\'https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png\' /></a><br /> The content of this webpage is licensed under a <a rel=\'license\' href=\'http://creativecommons.org/licenses/by-nc-sa/4.0/\'>Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.</i></p>\n</div>\n\n<a href=\'https://fdu-math.github.io/courses/' + temp +'\'>链接至[' + temp + ']课程页面<a>\n\n# ' + namelist[idx][1] + '\n\n<a href=\'https://fdu-math.github.io/assets/docs/courses/' + namelist0[idx][0] + '-' + namelist0[idx][1] + '-' + namelist0[idx][2] + '-' + namelist0[idx][3] + ' (Encrypted).pdf\'>课程大纲</a>'
            )