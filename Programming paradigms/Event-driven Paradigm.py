import tkinter as tk

def greet():
    print("Hello, World!")

def main():
    root = tk.Tk()
    button = tk.Button(root, text="Click Me", command=greet)
    button.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
