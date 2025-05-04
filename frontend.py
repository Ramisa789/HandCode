import tkinter as tk
import camera

root = tk.Tk()
root.title("Simple App")

label = tk.Label(root, text="Click to start camera")
label.pack()

start_button = tk.Button(root, text="Start Camera", command= camera.camera)
start_button.pack()

root.mainloop()