------------------------------------------
## Step 1

brew install python
brew install pyinstaller 

Version : python@3.9 -> 3.9.10
Host System: MacOS Catalina

------------------------------------------

## Step 2

Interpreter Location:

    /Library/Frameworks/Python.framework/Versions/3.10/bin/python3
    /Library/Frameworks/Python.framework/Versions/3.10/bin/pip3

--------------------------------------------------

## Step 3

Confirm the installation path path

which pip3

Expected Output : /Library/Frameworks/Python.framework/Versions/3.10/bin/pip3
    
which python3

Expected Output : /Library/Frameworks/Python.framework/Versions/3.10/bin/python3


-----------------------------------------
## Step 4

brew install pyinstaller

Make sure the installation is successful
--------------------------------------------------

## Step 5

cd source_code

## Check the following binary exist

ls /System/Library/Frameworks/Tk.framework/Tk
ls /System/Library/Frameworks/Tcl.framework/Tcl

## Build Application

pyinstaller  --noconsole --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' --windowed myapp.py


--------------------------------------------------
## Step 9 

Remove Signature

cd dist/myapp.app/Contents/MacOS

codesign --remove-signature Python
codesign --remove-signature myapp

--------------------------------------------------

## Step 7

If build is successful, the executables will be stored at


open dist/myapp.app


The application should launch and run

--------------------------------------------------

