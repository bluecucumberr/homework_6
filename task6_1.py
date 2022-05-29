import argparse
import os

parser = argparse.ArgumentParser(prog='Delete', description='Program for delete file')

parser.add_argument('name', help='user name')
parser.add_argument('path', help='path to file')
parser.add_argument('-s', '--silent', help='delete without questions', action='store_true')
args = parser.parse_args()
print(args)

user_name = args.name
path_to_file = args.path
silent_mode = args.silent

print(f"Hello, {user_name}. This program for deleting file")

if os.path.exists(path_to_file):
    if not silent_mode:
        while True:
            user_response = input(f"\nDo you want delete file {path_to_file}?\nPress 'Y' if you want or 'No' if you "
                                  f"dont want delete it\n")

            if user_response == 'Y':
                print("File will be deleted")
                break
            elif user_response == 'No':
                print("File dont delete")
                print('Program will be stop')
                exit(0)
            else:
                print("Command not found. Try again")
    if silent_mode:
        print('Silent mode activated. No questions will be asked. File will be deleted')
    os.remove(path_to_file)
    print('File was successfully removed.')
    print('Program will be stop')
    exit(0)
else:
    print("File not exist")
    print('Program will be stop')
    exit(0)
