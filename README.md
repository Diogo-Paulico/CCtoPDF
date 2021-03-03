# CCtoPDF
Turns two pictures of the CC (Cartão de Cidadão) and turns it into a PDF containing both centered and in a real-life size inserting an optional watermark if supplied, usefull when you need to send a copy of your CC when accepting contracts from service companies.<br>
The supplied card imaged should have decent quality and should be as trimmed as possible.<br>
Tested image formats: .jpg, .jpeg, .png

## Getting it up and Running

### Prerequisites

A standalone version for 64 bit Linux and Windows is made available in the Releases section of the repository, if you do not want to install python3 and the required library on your machine.

You will need Python3 and the reportlab library installed to use this <br/>
To install reportlab on Python3 open a terminal and type:
```
pip3 install reportlab
```

## Using the software
It has both a CLI (Command Line Interface) and GUI (Graphical User Interface) , the standalone version mentioned previously only contains the GUI.
The CLI is only made available for the non-standalone version.

### GUI 
![](/docs/GUI_LINUX.png) <br>
The GUI was built using *Tkinter* Python module, it looks very similiar in the 2 supported OSs (Windows and Linux).<br>
The first two buttons will open context menus to open the image files of both faces of the card (Front and Back respectively), you may leave the text field blank if you do not want to have a watermark, press <kbd>Gerar</kbd> and a new context menu will open for you to choose where you want to save and the name you want to give the PDF file.
#### Launching the GUI
In the standalone version in Windows all you have to do is double click the downloaded .exe file, for the standalone Linux version you will have to use a console to navigate the directory where the file was saved and then ./programName
In the non-standalone version, you will need to clone the repository, open a console, navigate to the program's folder and type:
```
python3 ./gui.py
```

### CLI
After cloning the repository to your machine, opening a console window and navigating to the program's folder.<br>
The program takes the following arguments: Full path to the front face image file of the card, Full path to the back face image file of the card, Full path including the .pdf extension to save the generated PDF and optionally a sentence to be used as a watermark<br>
Example use:
```
python3 cc_to_pdf.py /home/user/Front.png /home/user/Back.png /home/user/out.pdf Example Sentence for Watermark
```

## Authors

* **Diogo Paulico** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
