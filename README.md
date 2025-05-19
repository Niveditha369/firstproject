Project Summary: Basic Python Keylogger

This Python script functions as a basic keylogger, designed to capture keystrokes entered on the system. It utilizes the pynput library to monitor keyboard events. The captured keystrokes are recorded and appended to a text file named keylogger.txt. Subsequently, the script uses the smtplib and ssl libraries to send the contents of this log file to a specified email address.

Key Features:

Keystroke Capture: Records all keys pressed.
Local Logging: Saves captured keystrokes to keylogger.txt.
Email Reporting: Sends the content of the log file to a configured email address.
Basic Implementation: Represents a foundational keylogger with potential for future enhancements like periodic email sending.
Non-Executable: Requires explicit execution via the command line using python keylogger.py.
Exit Mechanism: The keylogger can be terminated by pressing the Esc key.
Requirements:

Python 3.x
pynput library (install via pip install pynput)
smtplib and ssl (typically included with Python)
A configured email account and password for sending logs.
Note: This is a basic implementation and lacks advanced features found in more sophisticated keyloggers. Use responsibly and ethically, only on systems you own or with explicit permission.
