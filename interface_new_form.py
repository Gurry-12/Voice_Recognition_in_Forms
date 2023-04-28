import tkinter as tk
import speech_recognition as sr
import re

# Regular expression pattern for matching domain names
domain_pattern = r'\b[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# Create the main window
root = tk.Tk()
root.title("Form Interface")
root.geometry("400x300")

# Create the form labels
name_label = tk.Label(root, text="Name:")
email_label = tk.Label(root, text="Email:")
phone_label = tk.Label(root, text="Phone Number:")

# Create the form entry fields
name_entry = tk.Entry(root)
email_entry = tk.Entry(root)
phone_entry = tk.Entry(root)

# Position the form labels and entry fields
name_label.grid(row=0, column=0, padx=10, pady=10)
email_label.grid(row=1, column=0, padx=10, pady=10)
phone_label.grid(row=2, column=0, padx=10, pady=10)
name_entry.grid(row=0, column=2, padx=10, pady=10)
email_entry.grid(row=1, column=2, padx=10, pady=10)
phone_entry.grid(row=2, column=2, padx=10, pady=10)

def recognize_speech(entry_field):
    # Create a recognizer instance
    recognizer = sr.Recognizer()

    # Define the microphone as the audio source
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            # Transcribe human voice from microphone input
            transcript = recognizer.recognize_google(audio)
            print("Transcript:", transcript)
            entry_field.delete(0, tk.END)
            entry_field.insert(0, transcript)
            f1 = open("text.txt",mode="a")
            f1.write(transcript + "\n")
            f1.close()

            # If email field is updated, clarify and add "@" symbol
            if entry_field == email_entry:
                email = add_at_symbol(transcript)
                email = re.sub(r'(\S+)@', lambda m: m.group(1).lower() + '@', email)
                entry_field.delete(0, tk.END)
                entry_field.insert(0, email)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Error: ", str(e))

def add_at_symbol(email_text):
    # Split the email into username and domain
    email_parts = email_text.split(" ")
    username = email_parts[0]
    domain = email_parts[-1]

    # Remove spaces and add "@" symbol before the domain
    domain = domain.replace(" ", "")
    email = username + "@" + domain
    return email

# Create a submit button
submit_button = tk.Button(root, text="Submit", bg="blue", fg="white")
submit_button.grid(row=3, column=1, padx=10, pady=10)

name_entry.bind("<FocusIn>", lambda event: recognize_speech(name_entry))
email_entry.bind("<FocusIn>", lambda event: recognize_speech(email_entry))
phone_entry.bind("<FocusIn>", lambda event: recognize_speech(phone_entry))

# Run the main loop
root.mainloop()
