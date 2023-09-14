import tkinter as tk

# Function
def close_app():
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("Tkinter Window")
window.geometry("400x300")

# Create a label widget
label = tk.Label(window, text="This is Parking App")
label.pack()


# Create a button that calls the close_app function when clicked
close_button = tk.Button(window, text="Close App", command=close_app)
close_button.pack()

# Start the Tkinter event loop
window.mainloop()
