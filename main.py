import tkinter
import tkinter.messagebox
import customtkinter
import subprocess

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CodeSlam Compiler")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CodeSlam", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        # create sidebar buttons
        self.sideBtnLexical = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_lexical)
        self.sideBtnLexical.grid(row=1, column=0, padx=20, pady=10)
        self.sideBtnSyntax = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_syntax)
        self.sideBtnSyntax.grid(row=2, column=0, padx=20, pady=10)
        self.sideBtnSemantic = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_semantic)
        self.sideBtnSemantic.grid(row=3, column=0, padx=20, pady=10)
        
        # create sidebar widgets
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create textbox for code editor
        self.codebox = customtkinter.CTkTextbox(self, width=250)
        self.codebox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        # Placeholder text
        self.codebox_placeholder = "Enter your code here..."
        self.codebox.insert("0.0", self.codebox_placeholder)
        self.codebox.bind("<FocusIn>", self.clear_placeholder)
        self.codebox.bind("<FocusOut>", self.add_placeholder)

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Lexical Analyzer", width=300)
        self.scrollable_frame.grid(row=0, column=2, rowspan=2, padx=(20, 10), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        # Terminal (text widget) to display output
        self.terminal_output = customtkinter.CTkTextbox(self, width=250, height=150)
        self.terminal_output.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.terminal_output.insert("0.0", "Terminal Output:\n\n")
        self.terminal_output.configure(state="disabled")  # Make terminal output read-only

        # Command input field (entry widget)
        self.command_input = customtkinter.CTkEntry(self)
        self.command_input.grid(row=2, column=1, padx=(20, 0), pady=(10, 20), sticky="ew")
        self.command_input.bind("<Return>", self.execute_command)  # Bind Enter key to run the command

        # set default values
        self.sideBtnLexical.configure(text="Lexical")
        self.sideBtnSyntax.configure(text="Syntax")
        self.sideBtnSemantic.configure(text="Semantic")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

    def clear_placeholder(self, event):
        if self.codebox.get("1.0", "end-1c") == self.codebox_placeholder:
            self.codebox.delete("1.0", "end")

    def add_placeholder(self, event):
        if not self.codebox.get("1.0", "end-1c"):
            self.codebox.insert("1.0", self.codebox_placeholder)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_lexical(self):
        self.append_terminal_output("Lexical Button Clicked!")
    
    def sidebar_button_syntax(self):
        self.append_terminal_output("Syntax Button Clicked!")
    
    def sidebar_button_semantic(self):
        self.append_terminal_output("Semantic Button Clicked!")

    def append_terminal_output(self, text):
        """Append text to the terminal output."""
        self.terminal_output.configure(state="normal")  # Make it editable temporarily
        self.terminal_output.insert("end", f"{text}\n")  # Add the text to the terminal
        self.terminal_output.see("end")  # Scroll to the end to show the latest output
        self.terminal_output.configure(state="disabled")  # Set it back to read-only

    def execute_command(self, event):
        """Execute the command entered in the command input field."""
        command = self.command_input.get()  # Get the command from the input field
        if command:
            try:
                # Run the command using subprocess
                result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                
                # Show the command in the terminal
                self.append_terminal_output(f"$ {command}")
                
                # Show the result of the command
                if result.stdout:
                    self.append_terminal_output(result.stdout)
                if result.stderr:
                    self.append_terminal_output(result.stderr)

            except Exception as e:
                self.append_terminal_output(f"Error: {e}")
        
        # Clear the input field
        self.command_input.delete(0, 'end')


if __name__ == "__main__":
    app = App()
    app.mainloop()