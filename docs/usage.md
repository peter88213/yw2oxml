------------------------------------------------------------------

## Command reference

-   [Export to docx](#export-to-docx)
-   [Scene list](#scene-list)


yWriter to OpenOffice/LibreOffice converter - yWriter export to docx/xlsx documents. 

# Instructions for use

## How to install yw2mso

1. If you have already installed an older version of yw2mso, please run the uninstaller for it. 

2. Unzip `yw2mso_<version number>.zip` within your user profile.

3. Move into the `yw2mso_<version number>` folder and run `setup.pyw` (double click).
   This will copy all needed files to the right places. 
   
4. If everything works well, an Explorer window will open, showing the installation folder.
   Now, add the context menu entries by double-clicking  `add_context_menu.reg`. 
   You may be asked for approval to modify  the Windows registry. Please accept.

You can remove the context menu entries by double-clicking  `rem_context_menu.reg`.

Please note that these context menus depend on the currently installed Python version. After a major Python update you may need to run the setup program again and renew the registry entries.

## How to use yw2mso

1. Move into your yWriter project folder, and right-click your .yw7 project file. 
   In the context menu, choose `Export to OpenOffice`. 
   
2. A sub menu with document types will open. Select the desired one.

3. If everything goes well, a success message pops up. The newly created file is located 
   in the same folder as your yWriter project. If you want to edit your new document immediately, 
   just click on the `open` button. 


## How to uninstall yw2mso

Move into the installation folder `~\.yw2oo` and double click on `rem_context_menu.reg`. 
You may be asked for approval to modify the registry. Please accept to remove the Explorer context
menu entry. 


# Command reference

## Export to docx

This will load yWriter 7 chapters and scenes into a new OpenDocument
text document (docx).

-   The document is placed in the same folder as the yWriter project.
-   Document's **filename**: `<yW project name>.docx`.
-   Text markup: Bold and italics are supported. Other highlighting such
    as underline and strikethrough are lost.
-   Only "normal" chapters and scenes are exported. Chapters and
    scenes marked "unused", "todo" or "notes" are not exported.
-   Only scenes that are intended for RTF export in yWriter will be
    exported.
-   Comments in the text bracketed with slashes and asterisks (like
    `/* this is a comment */`) are converted to author's comments.
-   Interspersed HTML, TEX, or RTF commands are taken over unchanged.
-   Gobal variables and project variables are not resolved.
-   Chapter titles appear as first level heading if the chapter is
    marked as beginning of a new section in yWriter. Such headings are
    considered as "part" headings.
-   Chapter titles appear as second level heading if the chapter is not
    marked as beginning of a new section. Such headings are considered
    as "chapter" headings.
-   Scene titles appear as navigable comments pinned to the beginning of
    the scene.
-   Usually, scenes are separated by blank lines. The first line is not
    indented.
-   Starting from the second paragraph, paragraphs begin with
    indentation of the first line.
-   Scenes marked "attach to previous scene" in yWriter appear like
    continuous paragraphs.



[Top of page](#top)

------------------------------------------------------------------------

## Proof reading

This will load yWriter 7 chapters and scenes into a new OpenDocument
text document (docx) with chapter and scene markers. File name suffix is
`_proof`.

-   The proof read document is placed in the same folder as the yWriter
    project.
-   Document's filename: `<yW project name>_proof.docx`.
-   Text markup: Bold and italics are supported. Other highlighting such
    as underline and strikethrough are lost.
-   All chapters and scenes will be exported, whether "used" or
    "unused".
-   The document contains chapter `[ChID:x]` and scene `[ScID:y]`
    markers according to yWriter 5 standard. **Do not touch lines
    containing the markers** if you want to be able to reimport the
    document into yWriter.
-   Back up your yWriter project and close yWriter before.



[Top of page](#top)

------------------------------------------------------------------------

## Brief synopsis

This will load a brief synopsis with chapter and scenes titles into a new
 OpenDocument teOptionally, you can append placed in the same folder as the yWriter project.
-   Document's **filename**: `<yW project name_brf_synopsis>.docx`.
-   Only "normal" chapters and scenes are exported. Chapters and
    scenes marked "unused", "todo" or "notes" are not exported.
-   Only scenes that are intended for RTF export in yWriter will be
    exported.
-   Chapter titles appear as first level heading if the chapter is
    marked as beginning of a new section in yWriter. Such headings are
    considered as "part" headings.
-   Chapter titles appear as second level heading if the chapter is not
    marked as beginning of a new section. Such headings are considered
    as "chapter" headings.
-   Scene titles appear as plain paragraphs.



[Top of page](#top)

------------------------------------------------------------------------

## Manuscript

This will load yWriter 7 chapters and scenes into a new OpenDocument
text document (docx) with invisible chapter and scene sections (to be
seen in the Navigator). File name suffix is `_manuscript`.



[Top of page](#top)

------------------------------------------------------------------------

## Scene descriptions

This will generate a new OpenDocument text document (docx) containing a
**full synopsis** with chapter titles and scene descriptions that can be
edited and written back to yWriter format. File name suffix is
`_scenes`.



[Top of page](#top)

------------------------------------------------------------------------

## Chapter descriptions

This will generate a new OpenDocument text document (docx) containing a
**brief synopsis** with chapter titles and chapter descriptions that can
be edited and written back to yWriter format. File name suffix is
`_chapters`.

**Note:** Doesn't apply to chapters marked
`This chapter begins a new section` in yWriter.



[Top of page](#top)

------------------------------------------------------------------------

## Part descriptions

This will generate a new OpenDocument text document (docx) containing a
**very brief synopsis** with part titles and part descriptions that can
be edited and written back to yWriter format. File name suffix is
`_parts`.

**Note:** Applies only to chapters marked
`This chapter  begins a new section` in yWriter.



[Top of page](#top)

------------------------------------------------------------------------

## Character list

This will generate a new OpenDocument spreadsheet (xlsx) containing a
character list that can be edited in Office Calc and written back to
yWriter format. File name suffix is `_charlist`.

You may change the sort order of the rows. You may also add or remove
rows. New entities must get a unique ID.



[Top of page](#top)

------------------------------------------------------------------------

## Location list

This will generate a new OpenDocument spreadsheet (xlsx) containing a
location list that can be edited in Office Calc and written back to
yWriter format. File name suffix is `_loclist`.

You may change the sort order of the rows. You may also add or remove
rows. New entities must get a unique ID.



[Top of page](#top)

------------------------------------------------------------------------

## Item list

This will generate a new OpenDocument spreadsheet (xlsx) containing an
item list that can be edited in Office Calc and written back to yWriter
format. File name suffix is `_itemlist`.

You may change the sort order of the rows. You may also add or remove
rows. New entities must get a unique ID.



[Top of page](#top)

------------------------------------------------------------------------

## Cross references

This will generate a new OpenDocument text document (docx) containing
navigable cross references. File name suffix is `_xref`. The cross
references are:

-   Scenes per character,
-   scenes per location,
-   scenes per item,
-   scenes per tag,
-   characters per tag,
-   locations per tag,
-   items per tag.



[Top of page](#top)

------------------------------------------------------------------------

## Character descriptions

This will generate a new OpenDocument text document (docx) containing
character descriptions, bio, goals, and notes that can be edited in Office
Writer and written back to yWriter format. File name suffix is
`_characters`.



[Top of page](#top)

------------------------------------------------------------------------

## Location descriptions

This will generate a new OpenDocument text document (docx) containing
location descriptions that can be edited in Office Writer and written
back to yWriter format. File name suffix is `_locations`.



[Top of page](#top)

------------------------------------------------------------------------

## Item descriptions

This will generate a new OpenDocument text document (docx) containing
item descriptions that can be edited in Office Writer and written back
to yWriter format. File name suffix is `_items`.



[Top of page](#top)

------------------------------------------------------------------------

## Scene list

This will generate a new OpenDocument spreadsheet (xlsx) listing scene
title, scene descriptions, and links to the manuscript's scene
sections. Further scene metadata (e.g. tags, goals, time), if any. File
name suffix is `_scenelist`.



[Top of page](#top)

------------------------------------------------------------------------

## Notes chapters

This will write yWriter 7 "Notes" chapters with child scenes into a new 
OpenDocument text document (docx) with invisible chapter and scene 
sections (to be seen in the Navigator). File name suffix is `_notes`.



[Top of page](#top)

------------------------------------------------------------------------


## Installation path

The **setup.py** installation script installs *yw2oo.pyw* in the user profile. This is the OptioOptioOptionally, you can appendter\yw2oo`
