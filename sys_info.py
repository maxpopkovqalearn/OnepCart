import subprocess
import os
import argparse

# Parser for arguments
parser = argparse.ArgumentParser()
parser.add_argument('--file-folder',
                    action='store',
                    default='C:\\PyCharm_projects\\System_status\\ff_folder',
                    help='Work directory')
args = parser.parse_args()

# System name
system_name = os.name
print(system_name)

# Current directory
current_folder = os.getcwd()
print(current_folder)

# List of file from working directory
files_list = os.listdir(args.file_folder)
print(files_list)

# System information
stdout_info = subprocess.Popen(['systeminfo'], stdout=subprocess.PIPE)
print("System Information: ")
stdin_info = subprocess.Popen(['findstr', '/C:OS Name', '/C:OS Version'], stdin=stdout_info.stdout)
result_info = stdin_info.communicate()

# Process list
stdout_proc = subprocess.Popen(['tasklist', '/NH'], stdout=subprocess.PIPE)
print('System Process: ')
stdin_proc = subprocess.Popen(['sort'], stdin=stdout_proc.stdout)
result_proc = stdin_proc.communicate()

# Network interfaces
print('Network Interfaces: ')
network_interfaces = subprocess.Popen('ipconfig')
network_interfaces.wait()