import os
import shutil
from tkinter import Tk, Canvas, Button

loopPoint = 0

folder_path = 'output'
image_paths = []

for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        image_path = os.path.join(folder_path, filename)
        image_paths.append(image_path)

def move_file(key):
    global loopPoint
    if loopPoint < len(image_paths):
        source_path = image_paths[loopPoint]
        folder_path_1 = "folder1"
        folder_path_2 = "folder2"
        if key == "1":
            destination = folder_path_1
        elif key == "2":
            destination = folder_path_2
        else:
            return
        shutil.move(source_path, destination)
        loopPoint += 1
        update_ui()

def update_ui():
    if loopPoint < len(image_paths):
        image_path = image_paths[loopPoint]
        img = Image.open(image_path)
        img = ImageTk.PhotoImage(img)
        canvas.itemconfig(image_item, image=img)
        canvas.image = img
    else:
        root.destroy()

def on_key(event):
    move_file(event.char)

def quit_application():
    root.destroy()

root = Tk()
root.title("Image Mover")

image_path = image_paths[loopPoint]
img = Image.open(image_path)
img = ImageTk.PhotoImage(img)
canvas = Canvas(root, width=img.width(), height=img.height())
image_item = canvas.create_image(0, 0, anchor='nw', image=img)
canvas.pack()

quit_button = Button(root, text="Quit", command=quit_application)
quit_button.pack()

root.bind("<Key>", on_key)

root.mainloop()
