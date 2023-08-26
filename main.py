from tkinter import *


def encode_text(text, key):
    encoded = []
    for i, char in enumerate(text):
        key_char = key[i % len(key)]
        text_hex = ord(char)
        key_hex = ord(key_char)
        encoded_char_hex = text_hex ^ key_hex

        encoded.append(format(encoded_char_hex, '02X'))

    return ''.join(encoded)


def decode_text(text, key):
    decoded = []
    for i in range(0, len(text), 2):
        encoded_char_hex = text[i:i + 2]
        key_char = key[i // 2 % len(key)]  # Cycle through key characters

        encoded_char = int(encoded_char_hex, 16)
        key_hex = ord(key_char)
        decoded_char = encoded_char ^ key_hex

        decoded.append(chr(decoded_char))
    return ''.join(decoded)


def encrypt_button_pressed():
    if len(title_entry.get()) == 0:
        error_message.config(text="Please enter the title")
    elif len(secret_text.get("1.0", END).strip()) == 0:
        error_message.config(text="Please enter the text to be encrypted")
    elif len(master_key_entry.get()) == 0:
        error_message.config(text="Please enter the Master Key")
    else:
        text = secret_text.get("1.0", "end-1c")
        key = master_key_entry.get()
        secret_title = title_entry.get()
        encrypted_text = encode_text(text, key)

        with open("SecretNotes.txt", mode="a") as myNewFile:
            myNewFile.write(secret_title + '\n')
            myNewFile.write(encrypted_text + '\n')


def decrypt_button_pressed():

    if len(secret_text.get("1.0", END).strip()) == 0:
        error_message.config(text="Please enter the text to be decrypted")
    elif len(master_key_entry.get()) == 0:
        error_message.config(text="Please enter the Master Key")
    elif not is_hexadecimal(secret_text.get("1.0", "end-1c")):
        error_message.config(text="please enter the encrypted text correctly")
    else:
        text = secret_text.get("1.0", "end-1c").strip()
        key = master_key_entry.get()
        decrypted_text = decode_text(text, key)
        secret_text.delete("1.0", END)
        secret_text.insert(END, decrypted_text)


def is_hexadecimal(input_string):
    return all(char.isdigit() or char.lower() in 'abcdef' for char in input_string)


if __name__ == '__main__':
    # Window
    window = Tk()
    window.title("Secret Notes")
    window.minsize(300, 600)

    # Image
    image = PhotoImage(file="output.png")
    image_label = Label(window, image=image)
    image_label.pack()

    # Title
    title_label = Label(window, text="Enter note title", pady=5)
    title_label.pack()

    title_entry = Entry()
    title_entry.pack()
    note_title = title_entry.get()

    # Secret Text
    secret_label = Label(window, text="Enter secret", pady=5)
    secret_label.pack()

    secret_text = Text(window, width=40, height=10)
    secret_text.pack()

    # Master Key
    master_key_label = Label(window, text="Enter master key", pady=5)
    master_key_label.pack()

    master_key_entry = Entry(window)
    master_key_entry.pack()

    # Encryption
    encryption_button = Button(window, text="Save & Encrypt", pady=5, command=encrypt_button_pressed)
    encryption_button.pack()

    # Decryption
    decryption_button = Button(window, text="Decrypt", pady=5, command=decrypt_button_pressed)
    decryption_button.pack()

    # Error Message
    error_message = Label(window,)
    error_message.pack()

    window.mainloop()
