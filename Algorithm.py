# ----- Imports -----
from tkinter import messagebox
from tkinter import *
import tkinter as tk
import easygui
import os
import shutil

# ----- Globabl Variables -----
directory = None
total = 0
done = 0
left = 0
aud = 0
com = 0
doc = 0
exe = 0
img = 0
vid = 0
oth = 0
extensions = {
    "audio":["mp3", "m4a", "wav", "ogg"],
    "compressed":["rar", "zip", "7z"],
    "document":["txt", "rtt", "csv", "json", "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx"],
    "executable":["exe"],
    "image":["png", "jpg", "jpeg", "gif", "bmp"],
    "video":["mp4", "mov", "wmv", "mkv", "webm"]
}

# ----- Functions -----
def helper():
    """Shows The Helper Box For Instructions"""
    messagebox.showinfo(title = "Help Text", message = "Welcome To The File Sorting Algorithm. Please Select A Directory And Click On The Sort Button.")

def show():
    """Showing How Many Items A Directory Has"""
    global total
    global directory
    global aud
    global com
    global doc
    global exe
    global img
    global vid
    global oth
    total = 0
    directory = easygui.diropenbox()
    label3["text"] = " " + directory
    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)) == True:
            total += 1
    label13["text"] = total
    for key, value in extensions.items():
        for item in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, item)) == True:
                ext = item.split(".")[-1]
                if ext in value:
                    if key == "audio":
                        oth += 1
                        aud += 1
                        continue
                    elif key == "compressed":
                        oth += 1
                        com += 1
                        continue
                    elif key == "document":
                        oth += 1
                        doc += 1
                        continue
                    elif key == "executable":
                        oth += 1
                        exe += 1
                        continue
                    elif key == "image":
                        oth += 1
                        img += 1
                        continue
                    elif key == "video":
                        oth += 1
                        vid += 1
                        continue
                    
    label4["text"] = f"Audios\n{aud}"
    label5["text"] = f"Compressed\n{com}"
    label6["text"] = f"Documents\n{doc}"
    label7["text"] = f"Executables\n{exe}"
    label8["text"] = f"Images\n{img}"
    label9["text"] = f"Videos\n{vid}"
    label10["text"] = f"Others\n{total-oth}"

def sort():
    """Sort The Directory According To The File Extensions"""
    if messagebox.askyesno(title = "Sort Files", message = "Are You Sure You Want To Sort All The Files ?"):      
        if directory == None:
            messagebox.showerror(title = "Empty Directory", message = "Please Select A Directory")
        global done
        global left
        left = total
        if aud > 0:
            if not os.path.exists(os.path.join(directory, "Audios")):
                os.mkdir(os.path.join(directory, "Audios"))
        if com > 0:
            if not os.path.exists(os.path.join(directory, "Compressed")):
                os.mkdir(os.path.join(directory, "Compressed"))
        if doc > 0:
            if not os.path.exists(os.path.join(directory, "Documents")):
                os.mkdir(os.path.join(directory, "Documents"))
        if exe > 0:
            if not os.path.exists(os.path.join(directory, "Executables")):
                os.mkdir(os.path.join(directory, "Executables"))
        if img > 0:
            if not os.path.exists(os.path.join(directory, "Images")):
                os.mkdir(os.path.join(directory, "Images"))
        if vid > 0:
            if not os.path.exists(os.path.join(directory, "Videos")):
                os.mkdir(os.path.join(directory, "Videos"))
        if oth > 0:
            if not os.path.exists(os.path.join(directory, "Others")):
                os.mkdir(os.path.join(directory, "Others"))
            
        for item in os.listdir(directory):
            for key, value in extensions.items():
                if os.path.isfile(os.path.join(directory, item)) == True:
                    ext = item.split(".")[-1]
                    if ext in value:
                        if key == "audio":
                            shutil.move(os.path.join(directory, item), os.path.join(directory, "Audios"))
                            done += 1
                            left -= 1
                            label15["text"] = done 
                            label17["text"] = left
                            continue
                        elif key == "compressed":
                            shutil.move(os.path.join(directory, item), os.path.join(directory, "Compressed"))
                            done += 1
                            left -= 1
                            label15["text"] = done 
                            label17["text"] = left
                            continue
                        elif key == "document":
                            shutil.move(os.path.join(directory, item), os.path.join(directory, "Documents"))
                            done += 1
                            left -= 1
                            label15["text"] = done 
                            label17["text"] = left
                            continue
                        elif key == "executable":
                            shutil.move(os.path.join(directory, item), os.path.join(directory, "Executables"))
                            done += 1
                            left -= 1
                            label15["text"] = done 
                            label17["text"] = left
                            continue
                        elif key == "image":
                            shutil.move(os.path.join(directory, item), os.path.join(directory, "Images"))
                            done += 1
                            left -= 1
                            label15["text"] = done 
                            label17["text"] = left
                            continue
                        elif key == "video":
                            shutil.move(os.path.join(directory, item), os.path.join(directory, "Videos"))
                            done += 1
                            left -= 1
                            label15["text"] = done 
                            label17["text"] = left
                            continue
        if done < total:
            for item in os.listdir(directory):
                if os.path.isfile(os.path.join(directory, item)) == True:
                    shutil.move(os.path.join(directory, item), os.path.join(directory, "Others"))
                    done += 1
                    left -= 1
                    label15["text"] = done 
                    label17["text"] = left
    messagebox.showinfo(title = "Sorting Done", message = "The Sorting Is Done. Please Check Your Folder.")
    
def clear():
    """Clear All The Values"""
    if messagebox.askyesno(title = "Clear Fields", message = "Are You Sure You Want To Clear All The Fields ?"):        
        label3["text"] = " Please Select A Folder"
        label4["text"] = "Audios"
        label5["text"] = "Compressed"
        label6["text"] = "Documents"
        label7["text"] = "Executables"
        label8["text"] = "Images"
        label9["text"] = "Videos"
        label10["text"] = "Others"
        label13["text"] = 0
        label15["text"] = 0
        label17["text"] = 0

def close():
    """Close The Application"""
    if messagebox.askyesno(title = "Exit Program", message = "Are You Sure You Want To Exit The App ?"):
        root.destroy()        

# ----- Main Code -----

# Initializing The Main Tkinter Window
root = tk.Tk()
root.resizable(False, False)
root.title("File Sorting Algorithm")
root.configure(bg="#cc99ff")
root.attributes("-fullscreen", True)

# Initializing The Images
picture1 = tk.PhotoImage(file="Files/Images/Audio.png")
picture2 = tk.PhotoImage(file="Files/Images/Compressed.png")
picture3 = tk.PhotoImage(file="Files/Images/Document.png")
picture4 = tk.PhotoImage(file="Files/Images/Executable.png")
picture5 = tk.PhotoImage(file="Files/Images/Image.png")
picture6 = tk.PhotoImage(file="Files/Images/Video.png")
picture7 = tk.PhotoImage(file="Files/Images/Other.png")

# Creating The Main Window
frame1 = tk.Frame(root, bg="#cc99ff", relief=RIDGE, bd=10)
frame1.place(relx=0.05, rely=0.075, relheight=0.85, relwidth=0.9)

label1 = tk.Label(frame1, text="File Sorting Algorithm", bg="#cc99ff" ,font=("Times New Roman", 40))
label1.place(relx=0.3, rely=0.05, relheight=0.1, relwidth=0.4)

button1 = tk.Button(frame1, text="i", font=("Times New Roman", 30, "bold"), relief=RIDGE, bd=10, command=helper, cursor="hand2")
button1.place(relx=0.8, rely=0.05, relheight=0.1, relwidth=0.07)

label2 = tk.Label(frame1, text="Select Folder To Sort", bg="#cc99ff", font=("Times New Roman", 20))
label2.place(relx=0.0175, rely=0.21, relheight=0.075, relwidth=0.2)

label3 = tk.Label(frame1, text=" Please Select A Folder", relief=RIDGE ,bd=6, font=("Times New Roman", 20), anchor="w")
label3.place(relx=0.24, rely=0.21, relheight=0.075, relwidth=0.55)

button2 = tk.Button(frame1, text="Select Folder", font=("Times New Roman", 20), relief=RIDGE ,bd=6 ,command=show, cursor="hand2")
button2.place(relx=0.815, rely=0.21, relheight=0.075, relwidth=0.15)

frame2 = tk.Frame(frame1, bg="white")
frame2.place(relx=0.02, rely=0.35, relheight=0.35, relwidth=0.12)

label4= tk.Label(frame2, text="Audios", image=picture1, font=("Times New Roman", 20) ,compound=TOP, bg="white")
label4.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

frame3 = tk.Frame(frame1, bg="white")
frame3.place(relx=0.16, rely=0.35, relheight=0.35, relwidth=0.12)

label5 = tk.Label(frame3, text="Compressed", image=picture2, font=("Times New Roman", 20) ,compound=TOP, bg="white")
label5.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

frame4 = tk.Frame(frame1, bg="white")
frame4.place(relx=0.3, rely=0.35, relheight=0.35, relwidth=0.12)

label6 = tk.Label(frame4, text="Documents", image=picture3, font=("Times New Roman", 20) ,compound=TOP, bg="white")
label6.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

frame5 = tk.Frame(frame1, bg="white")
frame5.place(relx=0.44, rely=0.35, relheight=0.35, relwidth=0.12)

label7 = tk.Label(frame5, text="Executables", image=picture4, font=("Times New Roman", 20) ,compound=TOP, bg="white")
label7.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

frame6 = tk.Frame(frame1, bg="white")
frame6.place(relx=0.58, rely=0.35, relheight=0.35, relwidth=0.12)

label8= tk.Label(frame6, text="Images", image=picture5, font=("Times New Roman", 20) ,compound=TOP, bg="white")
label8.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

frame7 = tk.Frame(frame1, bg="white")
frame7.place(relx=0.72, rely=0.35, relheight=0.35, relwidth=0.12)

label9= tk.Label(frame7, text="Videos", image=picture6, font=("Times New Roman", 20) ,compound=TOP, bg="white")
label9.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

frame8 = tk.Frame(frame1, bg="white")
frame8.place(relx=0.86, rely=0.35, relheight=0.35, relwidth=0.12)

label10 = tk.Label(frame8, text="Others", image=picture7, font=("Times New Roman", 20) ,compound=TOP, bg="white")
label10.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

label11 = tk.Label(frame1, text="STATUS", bg="#cc99ff", font=("Times New Roman", 20))
label11.place(relx=0.15, rely=0.8, relheight=0.05, relwidth=0.1)

frame9 = tk.Frame(frame1, bg="#cc99ff", relief=RIDGE, bd=5)
frame9.place(relx=0.25, rely=0.79, relheight=0.07, relwidth=0.6)

frame10 = tk.Frame(frame9, bg="#cc99ff")
frame10.place(relx=0.01, rely=0, relheight=1, relwidth=0.3)

label12 = tk.Label(frame10, text="TOTAL", bg="#cc99ff", font=("Times New Roman", 20))
label12.place(relx=0, rely=0, relheight=1, relwidth=0.75)

label13 = tk.Label(frame10, text=total, font=("Times New Roman", 20))
label13.place(relx=0.76, rely=0, relheight=1, relwidth=0.25)

frame11 = tk.Frame(frame9, bg="#cc99ff")
frame11.place(relx=0.31, rely=0, relheight=1, relwidth=0.3)

label14 = tk.Label(frame11, text="DONE", bg="#cc99ff", font=("Times New Roman", 20))
label14.place(relx=0, rely=0, relheight=1, relwidth=0.75)

label15 = tk.Label(frame11, text=done, font=("Times New Roman", 20))
label15.place(relx=0.76, rely=0, relheight=1, relwidth=0.25)

frame12 = tk.Frame(frame9, bg="#cc99ff")
frame12.place(relx=0.61, rely=0, relheight=1, relwidth=0.3)

label16 = tk.Label(frame12, text="LEFT", bg="#cc99ff", font=("Times New Roman", 20))
label16.place(relx=0, rely=0, relheight=1, relwidth=0.75)

label17 = tk.Label(frame12, text=left, font=("Times New Roman", 20))
label17.place(relx=0.76, rely=0, relheight=1, relwidth=0.25)

button3 = tk.Button(frame1, text="Sort", font=("Times New Roman", 20), relief=RIDGE, bd=6, command=sort, cursor="hand2")
button3.place(relx=0.34, rely=0.9, relheight=0.07, relwidth=0.1)

button4 = tk.Button(frame1, text="Clear", font=("Times New Roman", 20), relief=RIDGE, bd=6, command=clear, cursor="hand2")
button4.place(relx=0.45, rely=0.9, relheight=0.07, relwidth=0.1)

button5 = tk.Button(frame1, text="Exit", font=("Times New Roman", 20), relief=RIDGE, bd=6, command=close, cursor="hand2")
button5.place(relx=0.56, rely=0.9, relheight=0.07, relwidth=0.1)

# ----- Driver Code -----
if __name__ == "__main__":
    root.mainloop()
