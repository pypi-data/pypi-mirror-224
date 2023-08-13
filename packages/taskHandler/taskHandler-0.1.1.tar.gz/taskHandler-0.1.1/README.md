# About

This taskHandker package will distribute all file present in give directory in the newly create foldes according to there file extension


# how to use

```md = ManageDownloads()```

for windos `C:\Users\<userName>\Downloads\` is the default path
and for Linux `'home/<userName>/Downloads'` is the default path

or we can chagne path like this:-

```
download_path = r"C:\Users\<userName>\Downloads\Images"
md.set_download_path(download_path)

```
then call organize_downloads

```md.organize_downloads()```

file distributed according to key valse define in whitlist varable

```
newWhitlist={
                'Media': {'mp3', 'mp4'},
                'Images': {'jpg', 'jpeg', 'gif', 'png'},
                'Web': {'html', 'css'},
                'MS-Office': {'docx', 'xlsx', 'ppt'},
                'Scripts': {'py', 'pyc', 'c++', 'cpp', 'c', 'java', 'js'},
                "Pdf&csv": {'pdf', 'csv'},
                'Application': {'exe', 'bat'}
                }

```
this whitlist can be modified

```
newWhitlist={
                'Media': {'mp3'},
                'Images': {'jpg','gif', 'png'},
                'Web': {'html', 'css'},
                'MS-Office': {'docx', 'xlsx', 'ppt'},
                'Scripts': {'py', 'pyc', 'c', 'java', 'js'},
                "PdfCsv": {'pdf', 'csv'}
                }

md.set_whitelist(newWhitlist)
```

## also importing pwd is necessary for Linux