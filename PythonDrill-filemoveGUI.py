#
# PYTHON:   version 3.6.0
# AUTHOR:   Annie M Bowman
# PURPOSE:  Tech Academy Python Course DRILL Item #65
#           Develop a GUI for users to run file-transfer
#           script easily & with more versatility. User must
#           be able to browse to source and destination folders
#           and manually initiate 'file check & transfer'
# OS TEST:  Written and tested on MacOS Sierra v10.12.3

import os
import shutil
from datetime import datetime
import time
from tkinter import *
import tkinter as tk
from tkinter import messagebox, filedialog


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs) #base class constructor
        #master frame config:
        self.master = master
        self.master.minsize(640, 480)
        self.master.maxsize(640, 480)
        self.master.configure(bg='#000066')
        self.master.rowconfigure(3, minsize=70)
        self.master.rowconfigure(4, minsize=70)
        self.master.title('Daily File Transfer')
        
        center_window(self,640,480) #centers the gui on user's screen

        #LABELS!
        self.lbl_slist = tk.Label(self.master, text='Src Contents:') #source contents label
        self.lbl_slist.grid(row=2, column=0, padx=(15,0), pady=(20,0), sticky='sw')
        self.lbl_slist.config(background='#000066', foreground='white',
                          font=('Helvetica', 16, 'bold'))

        self.lbl_dlist = tk.Label(self.master, text='Dest Contents:') #destination contents label
        self.lbl_dlist.grid(row=2, column=4, padx=(15,0), pady=(20,0), sticky='sw')
        self.lbl_dlist.config(background='#000066', foreground='white',
                          font=('Helvetica', 16, 'bold'))

        #ENTRY FIELDS!
        self.ent_source = tk.Entry(self.master, text='') #source path entry field
        self.ent_source.grid(row=0, column=0, columnspan=5, padx=(30,10), pady=(15,5), sticky='we')
        
        self.ent_dest = tk.Entry(self.master, text='') #destination path entry field
        self.ent_dest.grid(row=1, column=0, columnspan=5, padx=(30,10), pady=(5,0), sticky='we')

        #LISTBOXES/SCROLLBARS!
            #source folder contents:
        self.scroll_s = Scrollbar(self.master, orient=VERTICAL)
        self.list_s = Listbox(self.master, height=10, exportselection=0,
                              yscrollcommand=self.scroll_s.set)
        self.scroll_s.config(command=self.list_s.yview)
        self.scroll_s.grid(row=3, column=2, rowspan=3, pady=(5,0), sticky='nsw')
        self.list_s.grid(row=3, column=0, rowspan=3, padx=(35,0), pady=(5,0), columnspan=2,
                         sticky='nse')
            #destination folder contents:
        self.scroll_d = Scrollbar(self.master, orient=VERTICAL)
        self.list_d = Listbox(self.master, height=10, exportselection=0,
                              yscrollcommand=self.scroll_d.set)
        self.scroll_d.config(command=self.list_d.yview)
        self.scroll_d.grid(row=3, column=6, rowspan=3, padx=(0,30), pady=(5,0), sticky='nsw')
        self.list_d.grid(row=3, column=4, rowspan=3, padx=(35,0), pady=(5,0), columnspan=2,
                         sticky='nse')
        

        #BUTTONS!
            #SOURCE:
        self.btn_source = tk.Button(self.master, width=10, height=2, text='SOURCE',
                                    font=('Helvetica', 14, 'bold'), foreground='#000066',
                                    highlightbackground='#888888', command=lambda: get_source(self))
        self.btn_source.grid(row=0, column=5, columnspan=2, pady=(15,5), sticky='e')

            #DESTINATION:
        self.btn_dest = tk.Button(self.master, width=10, height=2, text='DEST.',
                                  font=('Helvetica', 14, 'bold'), foreground='#000066',
                                  highlightbackground='#888888', command=lambda: get_dest(self))
        self.btn_dest.grid(row=1, column=5, columnspan=2, pady=(5,0), sticky='e')

            #TRANSFER:
        arrow = PhotoImage(file='stock_folder-move.gif').subsample(4,4)
        self.btn_transfer = tk.Button(self.master, text='TRANSFER', image=arrow, compound=TOP,
                                    highlightbackground='#888888', foreground='#000066',
                                    font=('Helvetica',14,'bold'),command=lambda:file_transfer(self))
        self.btn_transfer.image = arrow
        self.btn_transfer.grid(row=5, column=3, padx=(30,0),pady=(0,30),ipadx=5,ipady=2, sticky='ew')

            #QUIT:
        self.btn_quit = tk.Button(self.master, width=8, height=2, text='QUIT',
                                  font=('Helvetica', 14, 'bold'), foreground='#000066',
                                  highlightbackground='#888888', command=lambda: ask_quit(self))
        self.btn_quit.grid(row=6, column=5, columnspan=2, pady=25, sticky='e')

# ----------------------------- FUNCTIONS! ------------------------------------

def center_window(self, w, h):
    #get user's screen width & height:
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    #calculate x & y coords for placing app:
    x = int((screen_width/2)-(w/2)) 
    y = int((screen_height/2)-(h/2))
    #use geometry method to place app on the user's screen:
    center = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return center

def get_source(self):
    try:
        self.ent_source.delete(0,'end') #delete anything currently in the path field
        source = filedialog.askdirectory() #allow user to browse to find source folder
        self.ent_source.insert(0,source) #insert the filepath for source folder into path field
        clear_listS(self) #calls function to clear source listbox of contents
        for files in os.listdir(source): #then iterates through source folder contents
            self.list_s.insert('end', files+'\n') #and inserts each file on new row in listbox
    except:
        pass #so it won't throw an error if user cancels

def get_dest(self):
    try:
        self.ent_dest.delete(0,'end') #delete anything currently in the path field
        dest = filedialog.askdirectory() #allow user to browse to find dest folder
        self.ent_dest.insert(0,dest) #insert the filepath for dest folder into path field
        clear_listD(self) #calls function to clear dest listbox of contents
        for files in os.listdir(dest): #then iterates through dest folder contents
            self.list_d.insert('end', files+'\n') #and inserts each file on new row in listbox
    except:
        pass #so it won't throw an error if user cancels

def file_transfer(self):
    source = self.ent_source.get().strip() #gets path from source entry field
    dest = self.ent_dest.get().strip() #gets path from dest entry field
    if (len(source) > 0) and (len(dest) > 0): 
        for files in os.listdir(source): #iterates through contents of Source folder
            fileA = os.path.join(source, files) #adds files filename to end of Source folder path
            fileB = os.path.join(dest, files) #adds files filename to end of Dest folder path
            tstamp = os.path.getmtime(fileA) #gets time of most recent modification as a timestamp
            now = time.time() #gets unix time for current time
            last_modified = datetime.fromtimestamp(os.path.getmtime(fileA)).strftime('%I:%M %p on %m-%d-%y')
            if tstamp > (now - 86400): #if file was modified within the last 24hours:
                shutil.move(fileA, fileB) #change directory of each file from Source to Destination
    else: #if one or more of the paths is empty
        messagebox.showerror('Missing Path', 'Please make sure to choose paths for both'
                                 ' source and destination folders!')
                       
    clear_listS(self) #calls function to clear source listbox
    for files in os.listdir(source): #then iterates through source folder's updated contents
        self.list_s.insert('end', files+'\n') #and inserts new files in listbox
    clear_listD(self) #calls function to clear dest listbox
    for files in os.listdir(dest): #then iterates through dest folder's updated contents
        self.list_d.insert('end', files+'\n') #and inserts new files in listbox


def clear_listS(self):
    self.list_s.delete(0, 'end') #deletes any contents in the source listbox

def clear_listD(self):
    self.list_d.delete(0, 'end') #deletes any contents in the dest listbox

def ask_quit(self):
    #display a message box asking user if they want to exit, and if TRUE (ok):
    if messagebox.askokcancel('Exit program', 'Are you sure you want to exit?'):
        #close the app:
        self.master.destroy()
        os._exit(0) #this fully deletes any reference to our widgets from the
                    #user's computer (to free up their memory & prevent bugs

    

if __name__ == '__main__':
    root = tk.Tk()
    gui = ParentWindow(root)
    root.mainloop()
    
