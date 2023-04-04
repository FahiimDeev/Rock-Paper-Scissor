import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox
from PIL import Image, ImageTk  

class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        load = Image.open("img1.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0,y=0)
        
        border = tk.LabelFrame(self, text='Login', bg='ivory', bd = 10, font=("Arial", 20))
        border.pack(fill="both", expand="yes", padx = 150, pady=150)
        
        L1 = tk.Label(border, text="Username", font=("Arial Bold", 15), bg='ivory')
        L1.place(x=50, y=20)
        T1 = tk.Entry(border, width = 30, bd = 5)
        T1.place(x=180, y=20)
        
        L2 = tk.Label(border, text="Password", font=("Arial Bold", 15), bg='ivory')
        L2.place(x=50, y=80)
        T2 = tk.Entry(border, width = 30, show='*', bd = 5)
        T2.place(x=180, y=80)
        
        def verify():
            try:
                with open("credential.txt", "r") as f:
                    info = f.readlines()
                    i  = 0
                    for e in info:
                        u, p =e.split(",")
                        if u.strip() == T1.get() and p.strip() == T2.get():
                            controller.show_frame(SecondPage)
                            
                            
                            import random

                            root = Tk()
                            root.geometry("800x500")
                            root.title("Rock Paper Scissor Game")

                            computer_value = {
                                "0":"Rock",
                                "1":"Paper",
                                "2":"Scissor"
                            }

                            def reset_game():
                                b1["state"] = "active"
                                b2["state"] = "active"
                                b3["state"] = "active"
                                l1.config(text = "Player			 ")
                                l3.config(text = "Computer")
                                l4.config(text = "")

                            # Disable the Button
                            def button_disable():
                                b1["state"] = "disable"
                                b2["state"] = "disable"
                                b3["state"] = "disable"

                            # If I select rock
                            def isrock():
                                c_v = computer_value[str(random.randint(0,2))]
                                if c_v == "Rock":
                                    match_result = "Match Draw"
                                elif c_v=="Scissor":
                                    match_result = "You Win"
                                else:
                                    match_result = "Computer Win"
                                l4.config(text = match_result)
                                l1.config(text = "Your choice: Rock		 ")
                                l3.config(text = c_v)
                                button_disable()

                            # If I select paper
                            def ispaper():
                                c_v = computer_value[str(random.randint(0, 2))]
                                if c_v == "Paper":
                                    match_result = "Match Draw"
                                elif c_v=="Scissor":
                                    match_result = "Computer Win"
                                else:
                                    match_result = "You Win"
                                l4.config(text = match_result)
                                l1.config(text = "Your choice: Paper		 ")
                                l3.config(text = c_v)
                                button_disable()

                            # If I select scissor
                            def isscissor():
                                c_v = computer_value[str(random.randint(0,2))]
                                if c_v == "Rock":
                                    match_result = "Computer Win"
                                elif c_v == "Scissor":
                                    match_result = "Match Draw"
                                else:
                                    match_result = "You Win"
                                l4.config(text = match_result)
                                l1.config(text = "Your choice: Scissor		 ")
                                l3.config(text = c_v)
                                button_disable()

                            Label(root,
                                text = "Rock Paper Scissor",
                                font = "normal 20 bold",
                                fg = "blue").pack(pady = 20)

                            frame = Frame(root)
                            frame.pack()

                            l1 = Label(frame,
                                    text = "You			 ",
                                    font = 10)

                            l2 = Label(frame,
                                    text = "VS			 ",
                                    font = "normal 9 bold")

                            l3 = Label(frame, text = "Computer", font = 10)

                            l1.pack(side = LEFT)
                            l2.pack(side = LEFT)
                            l3.pack()

                            l4 = Label(root,
                                    text = "",
                                    font = "normal 20 bold",
                                    bg = "white",
                                    width = 15 ,
                                    borderwidth = 2,
                                    relief = "solid")
                            l4.pack(pady = 20)

                            frame1 = Frame(root)
                            frame1.pack()

                            b1 = Button(frame1, text = "Rock",
                                        font = 10, width = 7,
                                        command = isrock)

                            b2 = Button(frame1, text = "Paper ",
                                        font = 10, width = 7,
                                        command = ispaper)

                            b3 = Button(frame1, text = "Scissor",
                                        font = 10, width = 7,
                                        command = isscissor)

                            b1.pack(side = LEFT, padx = 10)
                            b2.pack(side = LEFT,padx = 10)
                            b3.pack(padx = 10)

                            Button(root, text = "Reset Game",
                                font = 10, fg = "red",
                                bg = "black", command = reset_game).pack(pady = 20)

                            root.mainloop()

                            i = 1
                            break
                    if i==0:
                        messagebox.showinfo("Error", "Please provide correct username and password!!")
            except:
                messagebox.showinfo("Error", "Please provide correct username and password!!")
         
        B1 = tk.Button(border, text="Submit", font=("Arial", 15), command=verify)
        B1.place(x=320, y=115)
        
        def register():
            window = tk.Tk()
            window.resizable(0,0)
            window.configure(bg="deep sky blue")
            window.title("Register")
            l1 = tk.Label(window, text="Username:", font=("Arial",15), bg="deep sky blue")
            l1.place(x=10, y=10)
            t1 = tk.Entry(window, width=30, bd=5)
            t1.place(x = 200, y=10)
            
            l2 = tk.Label(window, text="Password:", font=("Arial",15), bg="deep sky blue")
            l2.place(x=10, y=60)
            t2 = tk.Entry(window, width=30, show="*", bd=5)
            t2.place(x = 200, y=60)
            
            l3 = tk.Label(window, text="Confirm Password:", font=("Arial",15), bg="deep sky blue")
            l3.place(x=10, y=110)
            t3 = tk.Entry(window, width=30, show="*", bd=5)
            t3.place(x = 200, y=110)
            
            def check():
                if t1.get()!="" or t2.get()!="" or t3.get()!="":
                    if t2.get()==t3.get():
                        with open("credential.txt", "a") as f:
                            f.write(t1.get()+","+t2.get()+"\n")
                            messagebox.showinfo("Welcome","You are registered successfully!!")
                    else:
                        messagebox.showinfo("Error","Your password didn't get match!!")
                else:
                    messagebox.showinfo("Error", "Please fill the complete field!!")
                    
            b1 = tk.Button(window, text="Sign in", font=("Arial",15), bg="#ffc22a", command=check)
            b1.place(x=170, y=150)
            
            window.geometry("470x220")
            window.mainloop()
            
        B2 = tk.Button(self, text="Register", bg = "dark orange", font=("Arial",15), command=register)
        B2.place(x=650, y=20)
        
class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        load = Image.open("img3.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0,y=0)
        
        
        Button = tk.Button(self, text="Next", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=650, y=450)
        
        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=100, y=450)
        
class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg='Tomato')
        
        Label = tk.Label(self, text="Thanks for playing. Have a good day!", bg = "orange", font=("Arial Bold", 25))
        Label.place(x=40, y=150)
        
        Button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=650, y=450)
        
        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(SecondPage))
        Button.place(x=100, y=450)
        
        
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #creating a window
        window = tk.Frame(self)
        window.pack()
        
        window.grid_rowconfigure(0, minsize = 500)
        window.grid_columnconfigure(0, minsize = 800)
        
        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(FirstPage)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")
            
app = Application()
app.maxsize(800,700)
app.mainloop()