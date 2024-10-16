import tkinter as tk
from tkinter import scrolledtext
import subprocess

class TerminalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Terminal in Tkinter")
        self.geometry("600x400")

        # Create a scrolled text widget to act as terminal output
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, height=20, width=70)
        self.text_area.grid(row=0, column=0, padx=10, pady=10)

        # Create an entry widget for command input
        self.entry = tk.Entry(self, width=70)
        self.entry.grid(row=1, column=0, padx=10, pady=10)
        self.entry.bind("<Return>", self.run_command)

    def run_command(self, event):
        command = self.entry.get()  # Get command from the entry widget
        self.entry.delete(0, tk.END)  # Clear the entry widget after command is taken

        if command:
            try:
                # Run the command using subprocess and capture the output
                result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                # Display the command in the terminal
                self.text_area.insert(tk.END, f"\n$ {command}\n")
                
                # Insert the result of the command into the terminal
                if result.stdout:
                    self.text_area.insert(tk.END, result.stdout)
                if result.stderr:
                    self.text_area.insert(tk.END, result.stderr)
                    
                # Scroll to the end of the text box to show the latest output
                self.text_area.see(tk.END)
            except Exception as e:
                self.text_area.insert(tk.END, f"Error: {str(e)}\n")
                self.text_area.see(tk.END)

if __name__ == "__main__":
    app = TerminalApp()
    app.mainloop()
