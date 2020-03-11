import os 
import argparse

def file_delete(args_i):
    file_to_delete = args_i.delete[0]
    os.remove(file_to_delete)
    print('FILE DELETED SUCCESSFULLY')

def file_rename(args_i):
    old_file_name = args_i.rename[0]
    new_file_name = args_i.rename[1]
    os.rename(old_file_name, new_file_name)
    print('FILE RENAMED SUCCESSFULLY')

parser_obj = argparse.ArgumentParser(description='RENAMES AND DELETES USER SPECIFIC FILES')

parser_obj.add_argument('-r', '--rename', nargs=2, 
metavar=('old_fname' , 'new_fname'), type=str, help='RENAMES THE FILE')

parser_obj.add_argument('-d', '--delete', nargs=1, metavar='filename', type=str,

help='DELETES THE FILE')

args = parser_obj.parse_args()

if args.rename is not None:
    file_rename(args)
elif args.delete is not None:
    file_delete(args)