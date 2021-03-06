""" Build python script for the OpenOffice "convert yWriter" script.
        
In order to distribute single scripts without dependencies, 
this script "inlines" all modules imported from the pywriter package.

For further information see https://github.com/peter88213/yw2oxml
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import os
import sys
sys.path.insert(0, f'{os.getcwd()}/../../yw2oxml/src')
import inliner

SRC = '../src/'
BUILD = '../test/'
SOURCE_FILE = f'{SRC}yw2oxml_.pyw'
TARGET_FILE = f'{BUILD}yw2oxml.pyw'


def main():
    inliner.run(SOURCE_FILE, TARGET_FILE, 'yw2oxmllib', '../src/')
    inliner.run(TARGET_FILE, TARGET_FILE, 'pywriter', '../src/')
    print('Done.')


if __name__ == '__main__':
    main()
