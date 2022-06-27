"""Provide a yWriter to MS Office converter.

Copyright (c) 2022 Peter Triesberger
For further information see https://github.com/peter88213/yW2OO
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
from pywriter.converter.yw_cnv_ff import YwCnvFf
from pywriter.yw.yw7_file import Yw7File
from yw2msolib.docx.docx_scenedesc import DocxSceneDesc
from yw2msolib.docx.docx_chapterdesc import DocxChapterDesc
from yw2msolib.docx.docx_partdesc import DocxPartDesc
from yw2msolib.docx.docx_brief_synopsis import DocxBriefSynopsis
from yw2msolib.docx.docx_export import DocxExport
from yw2msolib.docx.docx_characters import DocxCharacters
from yw2msolib.docx.docx_items import DocxItems
from yw2msolib.docx.docx_locations import DocxLocations
from yw2msolib.xlsx.xlsx_charlist import XlsxCharList
from yw2msolib.xlsx.xlsx_loclist import XlsxLocList
from yw2msolib.xlsx.xlsx_itemlist import XlsxItemList
from yw2msolib.xlsx.xlsx_scenelist import XlsxSceneList


class Yw2msoExporter(YwCnvFf):
    """A converter for universal export from a yWriter 7 project.

    Public methods:
        export_from_yw(sourceFile, targetFile) -- Convert from yWriter project to other file format.

    Instantiate a Yw7File object as sourceFile and a
    Novel subclass object as targetFile for file conversion.
    Shows the 'Open' button after conversion from yw.

    Overrides the superclass constants EXPORT_SOURCE_CLASSES, EXPORT_TARGET_CLASSES.    
    """
    EXPORT_SOURCE_CLASSES = [Yw7File]
    EXPORT_TARGET_CLASSES = [DocxBriefSynopsis,
                             DocxSceneDesc,
                             DocxChapterDesc,
                             DocxPartDesc,
                             DocxExport,
                             DocxCharacters,
                             DocxItems,
                             DocxLocations,
                             XlsxCharList,
                             XlsxLocList,
                             XlsxItemList,
                             XlsxSceneList,
                             ]

    def export_from_yw(self, source, target):
        """Convert from yWriter project to other file format.

        Positional arguments:
            source -- YwFile subclass instance.
            target -- Any Novel subclass instance.
        
        Extends the super class method, showing an 'open' button after conversion.
        """
        super().export_from_yw(source, target)
        if self.newFile:
            self.ui._show_open_button(self._open_newFile)
