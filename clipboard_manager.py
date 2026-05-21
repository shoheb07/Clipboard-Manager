import pyperclip
import time

# Clipboard History List
clipboard_history = []

print("Clipboard Manager Started...")
print("Press CTRL + C to Stop\n")

last_text = ""

try:

    while True:

        # Read Clipboard Content
        current_text = pyperclip.paste()

        # Save New Clipboard Content
        if current_text != last_text:

            clipboard_history.append(current_text)

            last_text = current_text

            print(f"Copied: {current_text}")

        time.sleep(1)

except KeyboardInterrupt:

    print("\nClipboard Manager Stopped")

    print("\nClipboard History:\n")

    for i, text in enumerate(
        clipboard_history,
        start=1
    ):

        print(f"{i}. {text}")
