#! /usr/bin/env python3

import pandas as pd
import copy
import os

def courses2html(file, target_html):
    if os.path.exists(target_html):
        os.remove(target_html)
    test_html = './fsia09i32wr.txt'
    for idx in range(len(file)):
        tmp = file['教师'].values.tolist()[idx]
        tmp2 = file['职称'].values.tolist()[idx]
        tmp3 = file['课程序号'].values.tolist()[idx]
        tmp4 = file["课程名称"].values.tolist()[idx]
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
        file.iloc[idx, 1] = '<a href=\'https://fdu-math.github.io/courses/' + tmp3[0] + '\'>' + tmp4 + '</a>'
        file.iloc[idx, 0] = '<a href=\'https://fdu-math.github.io/courses/class-id/' + tmp3[0] + '-' + tmp3[1] + '\'>' + tmp5 + '</a>'
    file.to_html(test_html, index=False)
    temp1 = []
    with open(test_html,"r")as file1, open(target_html,"a")as file2:
        for line in file1:
            temp1.append(line)
        for line in temp1:
            file2.write(str(line).replace('&lt;','<').replace('&gt;','>'))
    os.remove(test_html)

target = '../docs/courses/courses_undergrad_2022_2023_Fall.csv'
to_target_html_revised = '../docs/courses/courses_undergrad_2022_2023_Fall_href_revised.html'
file_df = pd.read_csv(target, header=0)

courses2html(file_df, to_target_html_revised)