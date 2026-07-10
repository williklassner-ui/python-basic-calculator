import tkinter as tk
from tkinter import font

class ModernCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("K-Rechner")
        self.root.geometry("380x620")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")
        
        # Custom font
        self.display_font = font.Font(family="Segoe UI", size=42, weight="bold")
        self.button_font = font.Font(family="Segoe UI", size=18, weight="normal")
        
        self.expression = ""
        
        # Display (big like in the image)
        self.display_frame = tk.Frame(self.root, bg="#1e1e1e")
        self.display_frame.pack(fill="x", padx=20, pady=(40, 15))
        
        self.display = tk.Entry(
            self.display_frame, 
            font=self.display_font,
            bg="#1e1e1e",
            fg="#ffffff",
            justify="right",
            bd=0,
            relief="flat",
            readonlybackground="#1e1e1e",
            highlightthickness=0
        )
        self.display.pack(fill="x", ipady=20)
        self.display.config(state="readonly")
        
        # Button frame
        button_frame = tk.Frame(self.root, bg="#1e1e1e")
        button_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Button layout matching the image (orange operators)
        buttons = [
            ('C', '#a6a6a6'), ('±', '#a6a6a6'), ('%', '#a6a6a6'), ('÷', '#ff9f0a'),
            ('7', '#333333'), ('8', '#333333'), ('9', '#333333'), ('×', '#ff9f0a'),
            ('4', '#333333'), ('5', '#333333'), ('6', '#333333'), ('−', '#ff9f0a'),
            ('1', '#333333'), ('2', '#333333'), ('3', '#333333'), ('+', '#ff9f0a'),
            ('0', '#333333'), ('.', '#333333'), ('=', '#ff9f0a')
        ]
        
        row = 0
        col = 0
        for (text, color) in buttons:
            fg_color = "#000000" if color == "#a6a6a6" else "#ffffff"
            
            if text == '0':
                btn = tk.Button(
                    button_frame, 
                    text=text, 
                    font=self.button_font,
                    bg=color,
                    fg=fg_color,
                    bd=0,
                    relief="flat",
                    activebackground="#555555",
                    highlightthickness=0,
                    command=lambda t=text: self.on_button_click(t)
                )
                btn.grid(row=row, column=col, columnspan=2, padx=6, pady=6, ipadx=10, ipady=28, sticky="nsew")
                col += 1
            else:
                btn = tk.Button(
                    button_frame, 
                    text=text, 
                    font=self.button_font,
                    bg=color,
                    fg=fg_color,
                    bd=0,
                    relief="flat",
                    activebackground="#555555",
                    highlightthickness=0,
                    command=lambda t=text: self.on_button_click(t)
                )
                btn.grid(row=row, column=col, padx=6, pady=6, ipadx=10, ipady=28, sticky="nsew")
            
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Configure grid weights
        for i in range(5):
            button_frame.rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.columnconfigure(i, weight=1)
        
        self.root.mainloop()
    
    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '±':
            if self.expression and self.expression[0] == '-':
                self.expression = self.expression[1:]
            elif self.expression:
                self.expression = '-' + self.expression
        elif char == '%':
            try:
                self.expression = str(float(self.expression) / 100)
            except:
                self.expression = "Error"
        elif char == '=':
            try:
                # Replace symbols for eval
                expr = self.expression.replace('×', '*').replace('−', '-').replace('÷', '/')
                result = eval(expr)
                self.expression = str(result)
            except:
                self.expression = "Error"
        else:
            if char in '÷×−+':
                self.expression += char
            else:
                self.expression += char
        
        # Update display
        self.display.config(state="normal")
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)
        self.display.config(state="readonly")

if __name__ == "__main__":
    ModernCalculator()
