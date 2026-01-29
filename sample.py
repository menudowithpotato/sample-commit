


import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#2C3E50")
        
        # Variable to store the expression
        self.expression = ""
        
        # Create the display
        self.create_display()
        
        # Create buttons
        self.create_buttons()
    
    def create_display(self):
        """Create the calculator display"""
        # Display frame
        display_frame = tk.Frame(self.root, bg="#2C3E50")
        display_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Display entry
        self.display = tk.Entry(
            display_frame,
            font=("Arial", 24, "bold"),
            justify="right",
            bg="#ECF0F1",
            fg="#2C3E50",
            bd=10,
            relief="flat"
        )
        self.display.pack(expand=True, fill="both", ipady=20)
    
    def create_buttons(self):
        """Create calculator buttons"""
        # Button frame
        button_frame = tk.Frame(self.root, bg="#2C3E50")
        button_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Button layout
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]
        
        # Colors
        number_color = "#3498DB"
        operator_color = "#E74C3C"
        equal_color = "#27AE60"
        clear_color = "#E67E22"
        
        # Create buttons
        for i, row in enumerate(buttons):
            for j, button_text in enumerate(row):
                # Determine button color
                if button_text == '=':
                    bg_color = equal_color
                elif button_text == 'C':
                    bg_color = clear_color
                elif button_text in ['+', '-', '*', '/']:
                    bg_color = operator_color
                else:
                    bg_color = number_color
                
                # Create button
                button = tk.Button(
                    button_frame,
                    text=button_text,
                    font=("Arial", 18, "bold"),
                    bg=bg_color,
                    fg="white",
                    bd=0,
                    relief="flat",
                    activebackground=bg_color,
                    activeforeground="white",
                    cursor="hand2",
                    command=lambda x=button_text: self.on_button_click(x)
                )
                button.grid(row=i, column=j, sticky="nsew", padx=5, pady=5)
        
        # Configure grid weights for responsive layout
        for i in range(4):
            button_frame.grid_rowconfigure(i, weight=1)
            button_frame.grid_columnconfigure(i, weight=1)
    
    def on_button_click(self, char):
        """Handle button clicks"""
        if char == 'C':
            # Clear the display
            self.expression = ""
            self.display.delete(0, tk.END)
        
        elif char == '=':
            # Calculate the result
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
                self.expression = result
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero!")
                self.expression = ""
                self.display.delete(0, tk.END)
            except:
                messagebox.showerror("Error", "Invalid expression!")
                self.expression = ""
                self.display.delete(0, tk.END)
        
        else:
            # Add character to expression
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)


def main():
    """Main function to run the calculator"""
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()