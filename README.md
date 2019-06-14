# url2pdf GUI

A simple Python GUI for the url2pdf command-line tool.

Tested with this [fork](https://github.com/rwelz/URL2PDF) fork of the original [url2pdf](https://github.com/scottgarner/URL2PDF) tool.

Run the GUI: 
```
cd <path_to_url2pdf_gui>
./url2pdf.py
```

Check the Python code:
```
cd <path_to_url2pdf_gui>
flake8 url2pdf.py
flake8 url2pdf_gui.py
```

Built with wxPython 3.0, wxGlade 0.9.3, and url2pdf 6.2.6.

## Dependencies
 - wxPython
 - wxGlade
 - xerox
 - url2pdf
 
## Things to do
 - build an app, e.g. using py2app
 