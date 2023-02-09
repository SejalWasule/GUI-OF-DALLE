from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile

root = Tk()
root.title("Welcome to open AI")
root.geometry("1000x600+300+200")
root.configure(bg="#fff")
root.resizable(False,False)
##############################################################################################################
def newwindow():
    root.destroy()
    screen=Tk()
    screen.title("OPEN.AI-EXPLORE YOUR IMAGINATION!")
    screen.geometry("925x500+300+200")
    screen.config(bg="white")
    
#################################################################################################################   
# Main Menu
    mainmenu = Menu(screen)
    
# Menubar
    filemenu = Menu(mainmenu, tearoff = 0)
    filemenu.add_command(label = "Open", command = filedialog.askopenfilename )
    filemenu.add_command(label = "save", command = filedialog.asksaveasfilename)
    filemenu.add_separator()
    filemenu.add_command(label = "Exit", command = screen.destroy)
    mainmenu.add_cascade(label="File", menu=filemenu)
 
    option = Menu(mainmenu, tearoff = 0)
    option.add_command(label = "Favourites" )
    option.add_command(label = "History")
    option.add_command(label = "Collections")
    option.add_command(label = "Settings")
    mainmenu.add_cascade(label="Tools", menu=option)
    
    More = Menu(mainmenu, tearoff = 0)
    More.add_command(label = "Documentation")
    More.add_command(label = "Show credits")
    More.add_command(label = "Buy credits")
    More.add_command(label = "Join discord")
    More.add_command(label = "Visit API")
    More.add_command(label = "Announcements")
    mainmenu.add_cascade(label = "Help", menu = More)
 
    screen.config(menu = mainmenu)
#########################################################################################################################
    def generating():
        messagebox.showinfo("Generating ......")
#Widgets
    download = Button(screen,width=13,text="Save Image",border = 1,bg="white",fg ="Teal",font=("Calibri",14,"bold"),command = filedialog.asksaveasfilename)
    download.pack(expand=True)
    download.place(x=10,y=00)
    
    vartn = Button(screen,width=17,text="Create Variations",border = 1,bg="white",fg ="Teal",font=("Calibri",14,"bold"))
    vartn.pack(expand=True)
    vartn.place(x=130,y=00)
    
    edit = Button(screen,width=13,text="Edit Image",border = 1,bg="white",fg ="Teal",font=("Calibri",14,"bold"))
    edit.pack(expand=True)
    edit.place(x=300,y=00)
    
    share= Button(screen,width=8,text="Share",border = 1,bg="white",fg ="Teal",font=("Calibri",14,"bold"))
    share.pack(expand=True)
    share.place(x=435,y=00)
    
    Add  = Button(screen,width=17,text="Add to collection",border = 1,bg="white",fg ="Teal",font=("Calibri",14,"bold"))
    Add.pack(expand=True)
    Add.place(x=520,y=00)
    
#####################################################################################

    a=Label(screen, text="Start with a detailed description",bg="white",font=("Cambria",15,"bold"))
    a.pack(expand=True)
    a.place(x=100,y=100)
    
    surprise = Button(screen,width=10,text="Surprise me",border = 1,bg="white",fg ="Teal",font=("Calibri",16,"bold"),command= generating)
    surprise.pack(expand=True)
    surprise.place(x=450,y=90)
    
    frm = Frame(screen,width=1000,height=100,bg="Light Blue")
    frm.pack()
    frm.place(x=100,y=170)

    def on_enter(e):
        Input.delete("0","end")
    
    def on_leave(e):
        D = Input.get()
        if D=="":
            Input.insert(0,"Username")
    
    Input = Entry(frm,width =100,fg = "black", border =0, bg="Light Blue",font =("Comic Sans",12))
    Input.pack()
    Input.place(x=70,y=30)
    Input.insert(0,"Enter Detailed Discription(Eg:An Avocado shaped Chair)")
    Input.bind("<FocusIn>",on_enter)
    Input.bind("<FocusOut>",on_leave)

    generate = Button(frm,width=10,text="Generate",border = 1,bg="Black",fg ="white",font=("Calibri",16,"bold"),command=generating)
    generate.pack(expand=True)
    generate.place(x=860,y=40)

    frame1 = Frame(screen,width=400,height=800,bg="Teal")
    frame1.place(x=1200,y=0)
    
    upload = Button(screen,width=30,text="Upload an Image you want to edit",border = 0,bg="white",fg ="Teal",font=("Calibri",16,"bold"),command = filedialog.askopenfilename)
    upload.pack(expand=True)
    upload.place(x=450,y=270)

    recent = Button(frame1,width=8,text="Recent",border = 0,bg="black",fg ="white",font=("Calibri",16))
    recent.pack(expand=True)
    recent.place(x=50,y=20)
    
    clr = Button(frame1,width=8,text="Clear all",border = 0,bg="black",fg ="white",font=("Calibri",16))
    clr.pack(expand=True)
    clr.place(x=200,y=20)
    
    logout = Button(frame1,width=8,text="Logout",border = 0,bg="black",fg ="white",font=("Calibri",16),command=screen.destroy)
    logout.pack(expand=True)
    logout.place(x=150,y=700)
    
    b=Label(screen, text="Share your generations\n Get featured in the example gallery",bg="white",font=("Cambria",15,"bold"))
    b.pack(expand=True)
    b.place(x=800,y=20)
    
    subgen = Button(screen,width=30,text="Submit Generations",border = 0,bg="Light Blue",fg ="black",font=("Calibri",16,"bold"),command = filedialog.askopenfilename)
    subgen.pack(expand=True)
    subgen.place(x=800,y=90)
    
    #############################################################################################################3
    gal=Label(screen, text="Gallery: Try these examples",bg="white",font=("Cambria",15,"bold"))
    gal.pack(expand=True)
    gal.place(x=500,y=350)
    
    Img_btn1 = PhotoImage(file = "furry monster.png")
    img1 = Button(screen,image = Img_btn1,borderwidth = 1 )
    img1.pack()
    img1.place(x = 10 ,y=400)
    img11=Label(screen, text="A photo of a white\n fur monster standing\n in a purple room\nClick to try",bg="white",font=("Cambria",15,"bold"))
    img11.pack(expand=True)
    img11.place(x=10,y=600)
    
    Img_btn2 = PhotoImage(file = "roboNeon .png")
    img2 = Button(screen,image = Img_btn2,borderwidth = 1 )
    img2.pack()
    img2.place(x = 300 ,y=400)
    img22=Label(screen, text="A cyberpunk monster\n in a control room\n Click to try",bg="white",font=("Cambria",15,"bold"))
    img22.pack(expand=True)
    img22.place(x=300,y=600)
    
    Img_btn3 = PhotoImage(file = "Supernova.png")
    img3 = Button(screen,image = Img_btn3,borderwidth = 1 )
    img3.pack()
    img3.place(x = 600 ,y=400)
    img33=Label(screen, text="An expressive oil \npainting of a basketball\nplayer dunking, depicted\nas an explosion of a nebula\n Click to try",bg="white",font=("Cambria",15,"bold"))
    img33.pack(expand=True)
    img33.place(x=600,y=600)
    
    Img_btn4 = PhotoImage(file = "neonlights.png")
    img4 = Button(screen,image = Img_btn4,borderwidth = 1 )
    img4.pack()
    img4.place(x =900 ,y=400)
    img44=Label(screen, text="A futuristic neon lit \n cyborg face \nClick to try",bg="white",font=("Cambria",15,"bold"))
    img44.pack(expand=True)
    img44.place(x=900,y=600)
    
   
    screen.mainloop()
   
############################################################################################################

def signin():
    username = user.get()
    password= passw.get()
    
    if username == "Sejal" and password =="2002":
        newwindow()
        
    elif username!="Sejal" or password !="2002":
        messagebox.showerror("Invalid","Invalid username or password")
        
##################################################################################################################
def signup():
    window = Toplevel(root)
    window.title("Sign Up!")
    window.geometry('600x600+300+200')
    window.configure(background = "white")
    window.resizable(False,False)
    
    labl_0 = Label(window, text="Create Account",width=20,font=("bold", 20))  
    labl_0.place(x=90,y=53)  
  
    name = Label(window, text="Name",width=20,font=("bold", 10))  
    name.place(x=80,y=150)  
    ent_name = Entry(window,width =30,fg = "black", border =1, bg="Light gray",font =("Comic Sans",14,"bold"))  
    ent_name.place(x=240,y=150)
    ent_name.insert(0,"Enter name")  
  
    mail = Label(window, text="Email",width=20,font=("bold", 10))  
    mail.place(x=68,y=200)  
    ent_mail = Entry(window,width =30,fg = "black", border =1, bg="Light gray",font =("Comic Sans",14,"bold"))  
    ent_mail.place(x=240,y=200)
    ent_mail.insert(0,"Enter mail") 
    
    newpas = Label(window, text="Create Password",width=20,font=("bold", 10))  
    newpas.place(x=68,y=250)  
    ent_newpas = Entry(window,width =30,fg = "black", border =1, bg="Light gray",font =("Comic Sans",14,"bold"))  
    ent_newpas.place(x=240,y=250)
    ent_newpas.insert(0,"Enter password") 

    Button(window, text='Submit',width=20,bg='Light Blue',fg='black',command=newwindow ).place(x=180,y=380)  

    window.mainloop()
##############################################################################################################
def blog():
    messagebox.showinfo("Blog","DALL·E 2 can create original,\n realistic images and art from atext description.\n It can combine concepts, attributes, and styles.")
def api():
    messagebox.showinfo("API","Visit for Information:\n https://openai.com/api/")
def about():
    messagebox.showinfo("Abouts","Visit for Information:\n https://openai.com/about/")
def resrch():
    messagebox.showinfo("Research","OpenAI conducts fundamental, long-term research toward the creation of safe AGI.\n Visit for Information:\n https://openai.com/research/")
    
    
img = PhotoImage(file="aiart.png")
Label(root,image=img,bg = "white").place(x=10,y=100)

blg = Button(root,width=13,text="BLOG",border = 0,bg="white",fg ="Teal",font=("Calibri",14,"bold"),command = blog )
blg.place(x=10,y=00)

follw = Button(root,width=20,text="FOLLOW ON INSTAGRAM",border = 0,bg="white",fg ="Teal",font=("Calibri",14,"bold"))
follw.place(x=150,y=00)

view = Button(root,width=15,text="VIEW API DOCS",border = 0,bg="white",fg ="Teal",font=("Calibri",14,"bold"),command= api)
view.place(x=390,y=00)
    
abt= Button(root,width=10,text="ABOUT",border = 0,bg="white",fg ="Teal",font=("Calibri",14,"bold"),command=about)
abt.place(x=560,y=00)

Add  = Button(root,width=17,text="VIEW RESEARCH",border = 0,bg="white",fg ="Teal",font=("Calibri",14,"bold"),command = resrch)
Add.place(x=680,y=00)


####################################################################################################

frame = Frame(root,width=500,height=500,bg="black")
frame.place(x=480,y=70)

heading = Label(frame,text="OPEN.AI",fg="#fff",bg="black", font=("Cambria",70,"bold"))
heading.place(x=50,y=5)

subheading = Label(frame,text="OPEN.AI is a new system that \ncan create realistic images\n and art from a description \n in natural language.",fg="#fff",bg="black", font=("Cambria",25,"bold"))
subheading.place(x=30,y=120)

########################################################################################

login = Label(frame,text="Log in",fg="Light blue",bg="black", font=("STENCIL",18,"bold"))
login.place(x=220,y=280)

def on_enter(e):
    user.delete("0","end")

def on_leave(e):
    name = user.get()
    if name=="":
        user.insert(0,"Username")
    
user = Entry(frame,width =30,fg = "black", border =1, bg="Light gray",font =("Comic Sans",14,"bold"))
user.place(x=100,y=320)
user.insert(0,"Enter Username")
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

def on_enter(e):
    passw.delete("0","end")

def on_leave(e):
    code = passw.get()
    if code=="":
        passw.insert(0,"Password")
    
    
passw = Entry(frame, width =30,fg = "black", border =1, bg="Light gray",font =("Comic Sans",14,"bold"))
passw.place(x=100,y=370)
passw.insert(0,"Enter Password")
passw.bind("<FocusIn>",on_enter)
passw.bind("<FocusOut>",on_leave)

Enter= Button(frame,width=30,pady=7,text="Explore Your Imagination!",fg ="Teal",border = 0,font=("Britannic Bold",18,"bold"),command=signin)
Enter.place(x=50,y=420)

Noacc = Label(root,text="Don't Have an Account?",fg="Black",bg="white", font =("Calibri",14 ))
Noacc.place(x=80,y=500)

sign_up = Button(root,width=8,text="Sign Up!",border = 0,bg="white",fg ="Teal",font=("Calibri",16,"bold"),command=signup)
sign_up.place(x=270,y=492)

root.mainloop()

