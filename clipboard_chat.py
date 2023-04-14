# Import the required libraries
import openai
import logging
import pyperclip
import keyboard
import pyautogui # for simulating key presses

# Set up logging
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(levelname)s] - %(message)s")
logging.info("Starting the program")

# Set your OpenAI API key
openai.api_key = "OPENAI_KEY"

# Define a function to send text to OpenAI and get a response
def chat(text):
  # Log the input text
  logging.debug(f"Sending text to OpenAI: {text}")
  # Try to create a chat completion object with the text as the user message
  try:
    chat_completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "user",
          "content": text
        }
      ],
      max_tokens=100 # set up max tokens to 100
    )
    # Get the assistant message from the chat completion object
    response = chat_completion.choices[0].message.content
    # Log the response
    logging.debug(f"Received response from OpenAI: {response}")
    # Return the response
    return response
  except Exception as e:
    # Log the exception
    logging.error(f"An error occurred while sending text to OpenAI: {e}")
    # Return an empty string or a default response
    return ""

# Define a function to handle the keyboard shortcut
def shortcut():
  # Try to get the selected text from the clipboard
  try:
    text = pyperclip.paste()
    # Log the clipboard content
    logging.info(f"Clipboard content: {text}")
  except Exception as e:
    # Log the exception
    logging.error(f"An error occurred while getting clipboard content: {e}")
    # Set text to an empty string or a default value
    text = ""
  # Try to send the text to OpenAI and get a response
  try:
    response = chat(text)
  except Exception as e:
    # Log the exception
    logging.error(f"An error occurred while chatting with OpenAI: {e}")
    # Set response to an empty string or a default value
    response = ""
  # Try to copy the response to the clipboard
  try:
    pyperclip.copy(response)
    # Log the clipboard update
    logging.info(f"Clipboard updated with response: {response}")
  except Exception as e:
    # Log the exception
    logging.error(f"An error occurred while updating clipboard with response: {e}")
  # Try to press the numlock key
  try:
    pyautogui.press("numlock")
    # Log the key press
    logging.info("Pressed numlock key")
  except Exception as e:
    # Log the exception
    logging.error(f"An error occurred while pressing numlock key: {e}")

# Register the keyboard shortcut Ctrl + Alt + X to call the shortcut function
keyboard.add_hotkey("ctrl+alt+x", shortcut)
logging.info("Registered keyboard shortcut: Ctrl + Alt + X")

# Wait for the user to press Esc to exit the program
logging.info("Waiting for user input...")
keyboard.wait("esc")
logging.info("Exiting the program")
