# Modern minimalist calculator based on K-Rechner

import tkinter as tk
from tkinter import font

class ModernCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("K-Rechner")
        self.root.geometry("360x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")
        
        self.display_font = font.Font(family="Segoe UI", size=28, weight="bold")
        self.button_font = font.Font(family="Segoe UI", size=16)
        
        self.expression = ""
        
        self.display = tk.Entry(
            self.root, 
            font=self.display_font,
            bg="#2d2d2d",
            fg="#ffffff",
            justify="right",
            bd=0,
            relief="flat",
            readonlybackground="#2d2d2d"
        )
        self.display.pack(fill="x", padx=20, pady=(40, 20), ipady=30)
        self.display.config(state="readonly")
        
        button_frame = tk.Frame(self.root, bg="#1e1e1e")
        button_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        buttons = [
            ('C', '#ff5c5c'), ('±', '#666666'), ('%', '#666666'), ('÷', '#ff9500'),
            ('7', '#333333'), ('8', '#333333'), ('9', '#333333'), ('×', '#ff9500'),
            ('4', '#333333'), ('5', '#333333'), ('6', '#333333'), ('−', '#ff9500'),
            ('1', '#333333'), ('2', '#333333'), ('3', '#333333'), ('+', '#ff9500'),
            ('0', '#333333'), ('.', '#333333'), ('=', '#ff9500')
        ]
        
        row = col = 0
        for text, color in buttons:
            if text == '0':
                btn = tk.Button(
                    button_frame, text=text, font=self.button_font,
                    bg=color, fg="#ffffff", bd=0, relief="flat",
                    activebackground="#555555",
                    command=lambda t=text: self.on_button_click(t)
                )
                btn.grid(row=row, column=col, columnspan=2, padx=4, pady=4, ipadx=10, ipady=25, sticky="nsew")
                col += 1
            else:
                btn = tk.Button(
                    button_frame, text=text, font=self.button_font,
                    bg=color, fg="#ffffff", bd=0, relief="flat",
                    activebackground="#555555",
                    command=lambda t=text: self.on_button_click(t)
                )
                btn.grid(row=row, column=col, padx=4, pady=4, ipadx=10, ipady=25, sticky="nsew")
            
            col += 1
            if col > 3:
                col = 0
                row += 1
        
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
                expr = self.expression.replace('×', '*').replace('−', '-').replace('÷', '/')
                result = eval(expr)
                self.expression = str(result)
            except:
                self.expression = "Error"
        else:
            self.expression += char
        
        self.display.config(state="normal")
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)
        self.display.config(state="readonly")

if __name__ == "__main__":
    ModernCalculator()
