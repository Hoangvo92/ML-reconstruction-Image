import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

import sys
import math
import random





'''
    The Qt MainWindow class
    A vtk widget and the ui controls will be added to this main window
'''
class MainWindow(tk.Frame):

    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
         ''' Step 1: Initialize the Qt window '''
        self.master.title("MRI Reconstruction- Hoang Vo")
        #https://www.geeksforgeeks.org/open-a-new-window-with-a-button-in-python-tkinter/        
        self.master.geometry("1000x500")
        
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        ''' Step 1: Initialize the Qt window '''
 
        

        
        ''' Step 3: Add the control panel to the right hand side of the central widget '''
        # Note: To add a widget, we first need to create a widget, then set the layout for it
        self.right_panel_widget = Qt.QWidget() # create a widget
        self.right_panel_layout = Qt.QVBoxLayout() # set layout - lines up the controls vertically
        self.right_panel_widget.setLayout(self.right_panel_layout) #assign the layout to the widget
        self.mainLayout.addWidget(self.right_panel_widget) # now, add it to the central frame
        
        # The controls will be added here
        self.add_controls()
                
        
        
master = tk.Tk()
master.title("MRI Reconstruction- Hoang Vo")
#app = MainWindow(master)
master.geometry("1000x500")
master.iconbigmap("ML-reconstruction-Image/")

def open():
    global myImage
    
    master.filename = filedialog.askopenfilename(initialdir="/OASIS1", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
                  
    myLabel = Label(master, text = master.filename).pack()
    #processing image in here
    myImage = ImageTk.photoImage(Image.open(master.filename))
                  
    myImageLabel = Label(image=MyImage).pack()
    

                  
btn =  Button(master, text= "Open File" , command = open).pack()
    
master.maibloop()                 
#app.mainloop()