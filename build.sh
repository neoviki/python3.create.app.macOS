rm -rf build
rm -rf dist
/Users/viki/Library/Python/3.10/bin/pyinstaller --noconsole --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' --windowed myapp.py

if [ $? -ne 0 ]; then
    echo "error: pyinstaller failed"
    exit 1
fi

cd dist/myapp.app/Contents/MacOS
if [ $? -ne 0 ]; then
    echo "error: dist directoru missing!"
    exit 1
fi

codesign --remove-signature Python
codesign --remove-signature myapp
#sudo codesign --remove-signature Python
#codesign --remove-signature main


echo
echo
echo "Generated application is @ dist/myapp.app"
echo
echo
