# PyKeylogger
For Education Purposes ONLY

This program was intentionally made difficult to install. The idea behind this is to keep anyone who just wants to use my code to
inflict harm upon another computer.

If you would like to use this code, here's the directions for installation:

BEFORE INSTALLING: install the PyHook module, and win32 modules for your current system. Also, if you don't have it already, install 
python 2.7.11+ for your system.

1. Install the 3 files: the py file, the batch file, and the vbs file. 
2. Put the python file somewhere, and keep it there. The program needs to modified every time you move it.
3. Find the path, and put it in the batch file where indicated.
4. Put the batch file, and remember where it is.
5. Find that path, and put it in the vbs file where indicated.
6. Put the vbs file in the startup menu. To find it, you can do windows key + r, and type in "shell:startup" (without quotes)
7. Make sure python starts on the command line at startup. To do this, when you start the computer, type in "python" (without quotes)
on the command line. If the screen changes into an idle interface, then you're fine. If it says something along the lines of
"can't do that", then you need to put python on the environment PATH. This should help if you need it:
http://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7

9. Inside the python file, put in an email that you want it to log in to, and the email it should send to. Also, feel free to edit the
amount of time it takes for each log to come in.
10. Restart/log off/something else, and test the program
