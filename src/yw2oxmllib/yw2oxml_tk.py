""""Provide a tkinter GUI framework for yWriter docx/xlsx export.

Copyright (c) 2022 Peter Triesberger
For further information see https://github.com/peter88213/yw-viewer
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import tkinter as tk

from pywriter.file.doc_open import open_document
from pywriter.ui.main_tk import MainTk
from yw2oxmllib.yw2oxml_exporter import Yw2msoExporter


class Yw2msoTk(MainTk):
    """A tkinter GUI class for yWriter docx/xlsx export.
    
    Public methods:
        disable_menu() -- disable menu entries when no project is open.
        enable_menu() -- enable menu entries when a project is open.
        open_project(fileName) -- create a yWriter project instance and read the file. 
        close_project() -- close the yWriter project without saving and reset the user interface.

    Public instance variables:
        treeWindow -- tk window for the project tree.

    Show titles, descriptions, and contents in a text box.
    """

    def __init__(self, title, **kwargs):
        """Put a text box to the GUI main window.
        
        Positional arguments:
            title -- application title to be displayed at the window frame.
         
        Required keyword arguments:
            yw_last_open -- str: initial file.
        
        Extends the superclass constructor.
        """
        self.kwargs = kwargs
        super().__init__(title, **kwargs)
        self.viewerWindow = tk.Frame(self.mainWindow)
        self.viewerWindow.pack(expand=True, fill='both')
        self._exporter = Yw2msoExporter()
        self._exporter.ui = self

    def _build_main_menu(self):
        """Add main menu entries.
        
        Extends the superclass template method. 
        """
        super()._build_main_menu()
        self._exportMenu = tk.Menu(self.mainMenu, title='my title', tearoff=0)
        self.mainMenu.add_cascade(label='Export', underline=0, menu=self._exportMenu)
        self.mainMenu.entryconfig('Export', state='disabled')
        self._exportMenu.add_command(label='Export to docx', underline=0,
                                        command=lambda: self._export_document(''))
        self._exportMenu.add_command(label='Brief synopsis', underline=0,
                                        command=lambda: self._export_document('_brf_synopsis'))
        self._exportMenu.add_command(label='Scene descriptions', underline=0,
                                       command=lambda: self._export_document('_scenes'))
        self._exportMenu.add_command(label='Chapter descriptions', underline=0,
                                        command=lambda: self._export_document('_chapters'))
        self._exportMenu.add_command(label='Part descriptions', underline=0,
                                       command=lambda: self._export_document('_parts'))
        self._exportMenu.add_command(label='Character descriptions', underline=3,
                                        command=lambda: self._export_document('_characters'))
        self._exportMenu.add_command(label='Location descriptions', underline=0,
                                        command=lambda: self._export_document('_locations'))
        self._exportMenu.add_command(label='Item descriptions', underline=0,
                                        command=lambda: self._export_document('_items'))
        self.root._openButton = tk.Button(text="Open exported document", state=tk.DISABLED, command=self._open_newFile)
        self.root._openButton.config(height=1)
        self.root._openButton.pack(pady=10)

    def disable_menu(self):
        """Disable menu entries when no project is open.
        
        Extends the superclass method.      
        """
        super().disable_menu()
        self.mainMenu.entryconfig('Export', state='disabled')
        self.hide_open_button()

    def enable_menu(self):
        """Enable menu entries when a project is open.
        
        Extends the superclass method.
        """
        super().enable_menu()
        self.mainMenu.entryconfig('Export', state='normal')

    def _export_document(self, suffix):
        self.kwargs['suffix'] = suffix
        self._exporter.run(self.ywPrj.filePath, **self.kwargs)

    def show_open_button(self):
        self.root._openButton['state'] = tk.NORMAL

    def hide_open_button(self):
        self.root._openButton['state'] = tk.DISABLED

    def _open_newFile(self):
        """Open the converted file for editing and exit the converter script."""
        open_document(self._exporter.newFile)
