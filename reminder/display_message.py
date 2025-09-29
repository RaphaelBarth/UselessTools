import tkinter as tk
import nonsensical_phrase as nsp

def close_window() -> None:
    root.destroy()

phrase = nsp.get_random_phrase()
root = tk.Tk()

# get screen attributes
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# set properties
root.title("")
root.overrideredirect(1)
root.configure(bg=phrase.get(nsp.COLOR))
root.attributes("-topmost", True)
root.geometry(f"{screen_width}x{screen_height}+0+0")

# Define font sizes
font_size_phrase = int(screen_height / 20)
font_size_author = int(screen_height / 22)

# Create and pack phrase label
label_phrase = tk.Label(
    root,
    text=phrase.get(nsp.TEXT),
    bg=phrase.get(nsp.COLOR),
    font=("Arial", font_size_phrase, "bold"),
    anchor="center",
)
label_phrase.pack(side="top", pady=(screen_height / 10))

# Create and pack author label
label_author = tk.Label(
    root,
    text=phrase.get(nsp.AUTHOR),
    bg=phrase.get(nsp.COLOR),
    font=("Arial", font_size_author, "italic"),
    anchor="center",
)
label_author.pack(side="top")

# Create and pack OK button
ok_button = tk.Button(
    root,
    text="OK",
    command=close_window,
    font=("Arial", font_size_phrase, "bold"),
    bg=phrase.get(nsp.COLOR),
    activebackground=phrase.get(nsp.COLOR),
    borderwidth=0,
    padx=20,
    pady=10,
)
ok_button.pack(side="bottom", fill="x", padx=20, pady=(20, 0))

# Start the Tkinter main loop
root.mainloop()
