import customtkinter as a

win = a.CTk()
win.geometry("500x550")
a.set_appearance_mode("dark")

nav_frame = a.CTkFrame(win, height=60, width=500, fg_color="gold")
nav_frame.place(relx = 0.0 , rely=0.0)

bg_frame = a.CTkFrame(win, fg_color="white")
bg_frame.place(relx=0.1,rely = 0.2,  relwidth=0.8, relheight=0.7)

title = a.CTkLabel(bg_frame, text = ("Ebookreader"), font=("Arial", 20), text_color= "white")
title.place(relx=0.3, rely=0.05)

ebook_entry = a.CTkEntry(bg_frame, placeholder_text="EbookReader", font=("Arial", 15), text_color="white" )
ebook_entry.place(relx=0.3, rely=0.2)

button = a.CTkButton(bg_frame, text = "Load", font=("Arial", 15), text_color="white")
button.place(relx=0.1, rely=0.4)

button2 = a.CTkButton(bg_frame, text = 'Play', font = ('Arial',15),text_color = 'white')
button2.place(relx = 0.5, rely = 0.4)

win.mainloop()