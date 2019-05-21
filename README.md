# AgPAS-Exporter
A script to aggregate data from AgPAS webform submissions to Excel format. It parses data from the Notice of Intent and Questionnaire (Funded) webform submissions and refactors them into a format suitable for copy-pasting into the AgPAS database.


# Required Files
* `questionnaire_funded.csv` - Downloaded from the Drupal admin interface ([link](https://agnr.umd.edu/admin/structure/webform/manage/questionnaire_funded/results/download))
* `notice_of_intent_to_submit.csv` - Downloaded from the Drupal admin interface ([link](https://agnr.umd.edu/admin/structure/webform/manage/notice_of_intent_to_submit/results/download))
* `AgPAS-Exporter` - this program

# Usage

Double-click the `AgPAS-Exporter` executable. It will look in its surrounding folder for the required files (listed above) and read the information from them.

After successfully parsing the information, it will output the data in the format of the AgPAS database to a file named `database_out.xlsx`


# Development

## About this repository

This repository contains the code used to create the AgPAS Exporter program. It is written in Python. 

Library requirements are listed in `requirements.txt` and can be install via pip:

`$ pip install -r requirements.txt`

## Building from source

I used `pyinstaller` to build the script to an EXE executable. It will automatically include all necessary libraries, resulting in a portable .exe file.

`$ pyinstaller -F AgPAS-Exporter.py`

## Testing

Just run `$ python AgPAS-Exporter.py` with all necessary files in the same directory as the executable/script.

## License
MIT License

Copyright (c) 2019 Mike Bailey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
