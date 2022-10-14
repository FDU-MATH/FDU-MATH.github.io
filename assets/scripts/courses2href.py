#! /usr/bin/env python3

import pandas as pd

file = pd.read_csv('test.csv', header=0)

for idx in range(len(file)):
    tmp = file['教师'][idx]
    tmp2 = file['职称'][idx]
    tmp3 = file['课程序号'][idx]
    tmp = tmp.split(',')
    tmp2 = tmp2.split(',')
    tmp3 = tmp3.split('.')
    for idxx in range(len(tmp)):
        tmp[idxx] = '<a href=\'https://fdu-math.github.io/teachers/' + tmp[idxx].replace(' ','_') + '\'>' + tmp[idxx] + '</a>'
        if tmp2[idxx] == '':
            tmp2[idxx] = 'Null'
    file['教师'][idx] = '<br />'.join(tmp)
    file['职称'][idx] = '<br />'.join(tmp2)
    file['课程名称'][idx] = '<a href=\'https://fdu-math.github.io/courses/' + tmp3[0] + '\'>' + file["课程名称"][idx] + '</a>'

file["课程序号"] = '<a href=\'https://fdu-math.github.io/courses/class-id/' + file["课程序号"] + '\'>' + file["课程序号"] + '</a>'

file.to_csv("test2.csv", index=False)
