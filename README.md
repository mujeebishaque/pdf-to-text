# pdf-to-text
Really easy to use and simple python source code to convert pdf into text interactively. 

The above script is missing a dependency file. You can use the following code to get a filedialogue

```
from tkinter.filedialog import askopenfilename

def open_file_dialogue():
    _filename = askopenfilename(initialdir=CURRENT_DIR, filetypes =[("PDF File", "*.pdf")], title = "Choose a file.")
    if not _filename:
        SHOW_MESSAGE("No File Selected. Try Again.")
        return
    return _filename

```

The script works perfectly fine and fast. You'd just need to modify a couple of things or remove them. 
