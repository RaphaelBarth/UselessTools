import tkinter as tk
import nonsensical_phrase as nsp


def close_window() -> None:
    root.destroy()


phrase = nsp.get_random_phrase()
root = tk.Tk()

# get screen attributes
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# screen_width = 200
# screen_height = 100

# set properties
root.title("")
root.overrideredirect(1)
root.configure(bg=phrase.get(nsp.COLOR))
root.attributes("-topmost", True)
root.geometry(f"{screen_width}x{screen_height}+0+0")


label_phrase = tk.Label(
    root,
    text=phrase.get(nsp.TEXT),
    bg=phrase.get(nsp.COLOR),
    font=("Arial", int(screen_height / 20), "bold"),
    anchor="center",
)

label_phrase.pack(side="top", pady=(screen_height / 10))

label_author = tk.Label(
    root,
    text=phrase.get(nsp.AUTHOR),
    bg=phrase.get(nsp.COLOR),
    font=("Arial", int(screen_height / 22), "italic"),
    anchor="center",
)
label_author.pack(side="top")


ok_button = tk.Button(
    root,
    text="OK",
    command=close_window,
    font=("Arial", int(screen_height / 20), "bold"),
    bg=phrase.get(nsp.COLOR),
    activebackground=phrase.get(nsp.COLOR),
    borderwidth=0,
    padx=20,
    pady=10,
)

ok_button.pack(side="bottom", fill="x", padx=20, pady=(20, 0))

root.mainloop()
