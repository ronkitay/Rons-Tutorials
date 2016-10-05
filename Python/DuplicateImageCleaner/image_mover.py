#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

old_dir_name = '/Users/rkitay/Pictures/_Duplicates_To_Be_Deleted/zzzzzzzzzzzzzzzz/__________________Ron\'s Phone - probably duplicates (Old)'
new_root_dir = '/Users/rkitay/Pictures_From_Home-Sorted'
for file_name in os.listdir(old_dir_name):
    if file_name.endswith(".jpg") and not file_name.__contains__('-'):
        print "working on file: %s" % file_name
        year = file_name[0:4]
        month = file_name[4:6]
        print "year = %s" % (year)
        print "month = %s" % (month)
        target_dir = new_root_dir + '/' + year + '/' + month
        print "target dir = %s" % target_dir
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        os.rename(old_dir_name + '/' + file_name, target_dir + '/' + file_name)

        continue
    else:
        continue




