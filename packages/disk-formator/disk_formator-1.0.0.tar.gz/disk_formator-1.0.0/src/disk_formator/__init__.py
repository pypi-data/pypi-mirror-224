# SPDX-FileCopyrightText: 2023-present Thibault Savenkoff <thibault.savenkoff@outlook.fr>
#
# SPDX-License-Identifier: MIT
import subprocess
import platform
try:
    import psutil
except ImportError:
    subprocess.run('pip install psutil', shell=True)

def shred_drive(drive):
    if platform.system() == 'Windows':
        cmd = f'cipher /w:{drive}'
    elif platform.system() == 'Linux':
        cmd = f'sudo shred -v -n 1 -z {drive}'
    elif platform.system() == 'Darwin':
        cmd = f'sudo diskutil secureErase 0 {drive}'
    else:
        raise OSError('Unsupported platform')
    subprocess.run(cmd, shell=True)
    
def get_available_disks():
    partitions = psutil.disk_partitions()
    return [partition.device for partition in partitions if partition.fstype]

disks = get_available_disks()

print('Available disks:')
for i, disk in enumerate(disks):
    print(f'{i+1}. {disk}')
    
drive_num = input('Enter the number of the drive you would like to shred: ')
try:
    drive_num = int(drive_num)
    if drive_num < 1 or drive_num > len(disks):
        raise ValueError
except ValueError:
    print('Invalid input')
    exit()

drive = disks[drive_num-1]

if platform.system() == 'Windows':
    if drive == "C:":
        print('You cannot shred your root drive')
        exit()
elif platform.system() == 'Linux':
    if drive == "/":
        print('You cannot shred your root drive')
        exit()
elif platform.system() == 'Darwin':
    if drive == "/":
        print('You cannot shred your root drive')
        exit()

confirm = input(f'Are you sure you want to shred {drive}? (y/n): ')
if confirm.lower() == 'y':
    shred_drive(drive)
    print(f'{drive} has been securely erased')
else:
    print('Operation cancelled')