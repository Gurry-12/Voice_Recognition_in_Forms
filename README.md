# Voice_Recognition_in_Forms

# Form Interface with Speech Recognition

## Overview

This project implements a simple form interface using Python's tkinter library, allowing users to input their name, email, and phone number. The special feature of this interface is speech recognition, which enables users to populate the form fields by speaking into the microphone.

## Dependencies

- Python 3
- tkinter
- speech_recognition

  ## Install the required Python packages

      pip install tkinter
      pip install SpeechRecognition

# How to Use
Run the application:

      python form_interface.py

  1. The application window will open, displaying three form fields: Name, Email, and Phone Number.
   2. Click inside any form field to activate the microphone.
  3. Start speaking to fill in the respective form field. The speech will be transcribed and displayed in the form field.
  4. For the Email field, the application will automatically add an "@" symbol after transcribing the domain name.
  5. Once all the form fields are populated, click the "Submit" button.

# Note

    Make sure your microphone is properly connected and working before using the speech recognition feature.

# Acknowledgements

   The speech recognition feature uses the speech_recognition library by Anthony Zhang (Uberi). [SpeechRecognition on GitHub](SpeechRecognitiononGitHub)
  The tkinter-based form interface is built using Python's built-in tkinter library.

# Contact

For any questions or inquiries about the project, you can contact me at singhsarpreet234@gmail.com.
