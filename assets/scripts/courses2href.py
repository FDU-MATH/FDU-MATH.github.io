#! /usr/bin/env python3

import pandas as pd

file = pd.read_csv('test.csv', header=0)

file["课程名称"] = '<a href=\'https://fdu-math.github.io/courses/' + file["课程序号"].str[0:10] + '\'>' + file["课程名称"] + '</a>'

file["课程序号"] = '<a href=\'https://fdu-math.github.io/courses/course-id/' + file["课程序号"] + '\'>' + file["课程序号"] + '</a>'

file["职称"] = file["职称"].str.replace(',','<br />')

for idx in range(len(file)):
    tmp = file['教师'][idx]
    tmp = tmp.split(',')
    for idxx in range(len(tmp)):
        tmp[idxx] = '<a href=\'https://fdu-math.github.io/teachers/' + tmp[idxx].replace(' ','_') + '\'>' + tmp[idxx] + '</a>'
    file['教师'][idx] = '<br />'.join(tmp)

file.to_csv("test2.csv", index=False)
