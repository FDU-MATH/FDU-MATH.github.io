#! /usr/bin/env python3

import pandas as pd

target = '../docs/courses/courses_undergrad_2022_2023_Fall.csv'
# to_target_csv = '../docs/courses/courses_undergrad_2022_2023_Fall_href.csv'
to_target_html = '../docs/courses/courses_undergrad_2022_2023_Fall_href.txt'
to_target_html_revised = '../docs/courses/courses_undergrad_2022_2023_Fall_href_revised.txt'

file = pd.read_csv(target, header=0)

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

# file.to_csv(to_target_csv, index=False)
file.to_html(to_target_html, index=False)

temp1 = []
with open(to_target_html,"r")as file1, open(to_target_html_revised,"a")as file2:
    for line in file1:
        temp1.append(line)
    for line in temp1:
        file2.write(str(line).replace('&lt;','<').replace('&gt;','>'))

import os
os.remove(to_target_html)