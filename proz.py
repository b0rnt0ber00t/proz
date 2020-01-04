#!/usr/bin/python3
#
# =============================================== #
#  Build By : b0rnt0ber00t                        #
#  Github Link : https://github.com/b0rnt0ber00t  #
# =============================================== #
#

# specific import library
from argparse import ArgumentParser

# from config folder
import config.MikroTik

# set variable for load data
MikroTik = config.MikroTik

# Main function
def main():
    parser = ArgumentParser(usage='%(prog)s [options]', epilog='Don\'t depend with this tool!', description='[!] Case character is very influential')
    parser.add_argument('-l', '--list', action='store_true', help='Use this flag to find out the list of modules and actions')
    parser.add_argument('-m', '--module', type=str)
    parser.add_argument('-a', '--action', type=str)
    parser.add_argument('-v', '--version', action='version', version='%(prog)s: Version 0.1')

    # retun parser
    args = parser.parse_args()

    # argument list
    if args.list:
        list_module_MikroTik = open('config/list/list_module.txt')
        print(list_module_MikroTik.read())
        list_module_MikroTik.close()

    # argumen module
    if args.module == 'MikroTik':

        # action provision
        if args.action == 'provision':
            MikroTik.provision()

        # action ztp
        if args.action == 'ztp':
            MikroTik.ztp()

# check if this file main execute
if __name__ == "__main__":
    try:
        main()
    except(KeyboardInterrupt):
        print('\nw: Program cenceled by user.')
else:
    print('w: Cant\'t run program if not main execution!')
