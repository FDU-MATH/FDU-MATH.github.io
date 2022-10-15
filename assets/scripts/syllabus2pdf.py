#! /usr/bin/env python3

import doc2pdf as dp
import os

target_folder = '../docs/courses/syllabus/test'
file = os.popen('cd ' + target_folder + '; ls;')

for line in file:
    name = line.rstrip('\n')
    dp.convert(target_folder + '/' + name)
    os.remove(target_folder + '/' + name)
    print('Successfully Convert ' + name + ' to PDF.')
print('You are all set.')