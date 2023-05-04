# mtg-liga-parser

Since MTG leagues do not support exporting of files in an easy format (only PDF and text copy),
this tool is designed to parse the .pdf files that can be downloaded and write a sorted .csv file.  

# Example usage

`python -m app`

The output file is always overwritten by processing all input .pdf files.

# Config options

```
{
  "pdf_folder": "relative/path/to/pdf/folder, e.g. pdfs",
  ip"aggregated_file": "relative/path/to/ligadata.csv, file to be created",
  "csv_delimiter": "; -> this is the .csv delimiter to be used"
}
```

# Packaging

```
pyinstaller __main__.py 
pyinstaller -F __main__.py
```
