from tkinter import *


window = Tk()
window.title("Secret Notes")
window.minsize(300, 600)

image = PhotoImage(file="output.png")
image_label = Label(window, image=image)
image_label.pack()

# Title
title_label = Label(text="Enter note title", pady=5)
title_label.pack()

title_entry = Entry()
title_entry.pack()
note_title = title_entry.get()

# Secret Text
secret_label = Label(text="Enter secret", pady=5)
secret_label.pack()

secret_text = Text(height=10, width=30)
secret_text.pack()
text = secret_text.get(0, END)

# Master Key
master_key_label = Label(text="Enter master key", pady=5)
master_key_label.pack()

master_key_entry = Entry()
master_key_entry.pack()
master_key = master_key_entry.get()

# Encryption
encryption_button = Button(text="Save & Encrypt", pady=5)
encryption_button.pack()

# Decryption
decryption_button = Button(text="Decrypt", pady=5)
decryption_button.pack()

'''
ui

    image+
    title label+
    title+
    the text+
    master key label+
    master key+
    save&encrypt+
    decrypt+
   

image insertion+

encryption through master key
insertion of text into file
decryption
error messages for when:
    *the title is not entered
    *there is no text to be encrypted/decrypted
    *the text to be decrypted is incorrect
    *there is no master key
     
'''


window.mainloop()
