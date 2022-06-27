"""Convert yWriter project to docx or xlsx. 

Version @release
Requires Python 3.6+
Copyright (c) 2022 Peter Triesberger
For further information see https://github.com/peter88213/yW2OO
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import sys
from pywriter.ui.ui_tk import UiTk
from yw2msolib.yw2mso_exporter import Yw2msoExporter


def run(sourcePath, suffix=None):
    converter = Yw2msoExporter()
    converter.ui = UiTk('Export from yWriter @release')
    kwargs = {'suffix': suffix}
    converter.run(sourcePath, **kwargs)
    converter.ui.start()


if __name__ == '__main__':
    try:
        sourcePath = sys.argv[1]
    except:
        sourcePath = ''
    try:
        suffix = sys.argv[2]
    except:
        suffix = ''
    run(sourcePath, suffix)