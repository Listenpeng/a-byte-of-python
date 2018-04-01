#!/usr/bin/env python3
# Filename: backup_ver2.py

import os
import time

#备份目标
source = ['/home/listen/data']

target_dir = '/home/listen/backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

target = today + os.sep + now + '.zip'

zip_command = 'zip -qr {0} {1}'.format(target, ''.join(source))

if os.system(zip_command) == 0 :
    print('Successfully backup to', target)
else:
    print('Backup FAILED')

