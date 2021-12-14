import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

#from predict.predictTR import *
#from predict.predictTE import *
#from predict.predictT1 import *
#from predict.predictT2 import *
from predict.predictT import *
from reconstruct.reconstructImage import *
#from reconstruct.test import *
from utility.transforms import noise_and_kspace, to_k_space, to_Pil_image, preprocessImage

import sys
import math
import random

#GUI_reconstruct_mri_tk_HV.py



                
      #https://www.youtube.com/watch?v=Aim_7fC-inw
      #https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python
        
master = Tk()
master.title("MRI Reconstruction- Hoang Vo")
#app = MainWindow(master)
master.geometry("500x400")
#master.iconbitgmap("ML-reconstruction-Image/")

def open():
    global first_image
    global myImage
    global image1 # original image
    
    #first_image.grid_forget()
    btn_add_noise['state'] = DISABLED

    btn_reconstruct['state'] = DISABLED
   
    btn_parameters['state'] = DISABLED
    master.filename = filedialog.askopenfilename(initialdir="data/test/images", title="Select A File", filetypes=(("png files", "*.png"),("all files", "*.*")))
   # top = Toplevel()
    #top.title("Chosen Image")
    myLabel = Label(master, text = master.filename)#.pack()
    #print(myLabel)
    #processing image in here
   #https://stackoverflow.com/questions/52558118/how-to-display-multiple-images-inside-tkinter-window
    image1 = Image.open(master.filename)
    k_space = to_k_space(image1)
    k_space_image = to_Pil_image(k_space)
    k_space_image.save("k_space.png")
   # resized = myImage.resize((300,300),Image.ANTIALIAS)
    myImage = ImageTk.PhotoImage(Image.open(master.filename))#.resize((300,300),Image.ANTIALIAS))
    #tk_image = ImageTk.PhotoImage(myImage)

           
    first_image = Label(master, image= myImage)#.pack()


   # myLabel.grid(row=1, column=0, columnspan=12)
    #l1.grid(row=2, column=0, columnspan=2)
    first_image.grid(row=3, column=0, columnspan=2)
    #l2.grid(row=2,column=4, columnspan=2)

    #btn2 = Button(top, text="Add Noise").pack() #, command = top.destroy)
    #btn2.grid(row=1, column= 0)
    btn_add_noise['state'] = NORMAL
def call_k_space():
    img = Image.open("k_space.png")#.convert('RGB')
    print("get file")
    kImage = ImageTk.PhotoImage(img)
    k_first_image = Label(master, image= kImage)   
    k_first_image.grid(row=3, column=4, columnspan=2)
    
def noise_image():
    global second_image
    global noiseImage
    global image1
    global image2
    btn_add_noise['state'] = DISABLED

    btn_reconstruct['state'] = DISABLED
   
    btn_parameters['state'] = DISABLED
    #first_image.grid_forget()
    call_k_space()
    top = Toplevel()
    top.title("Noise Image")
    #do noise
    image2 = noise_and_kspace(image1)
    pil_image2 = to_Pil_image(image2)
    pil_image2.save("noise.png")
    
   # image = Image.open("testing/test.png")
    # do noise
   # resized = myImage.resize((300,300),Image.ANTIALIAS)
    noiseImage = ImageTk.PhotoImage(Image.open("noise.png"))#.resize((300,300),Image.ANTIALIAS))
    #tk_image = ImageTk.PhotoImage(myImage)
           
    second_image = Label(top, image= noiseImage)#.pack()
    second_image.grid(row=0, column=0, columnspan=2)
    btn_reconstruct['state'] = NORMAL


def reconstruct_image():
    global third_image
    global reconstruct
    global image1
    global image2
    global image3
    btn_add_noise['state'] = DISABLED

    btn_reconstruct['state'] = DISABLED
   
    btn_parameters['state'] = DISABLED
    #first_image.grid_forget()
    top = Toplevel()
    top.title("Reconstruct Image")
    img_gt, img_und = preprocessImage( image1, image2)
    image3 = reconstructImage(img_gt, img_und, 'machine_learning/restnet-model4.pt')
    
   # image = Image.open("pred1.png")
    # do noise
   # resized = myImage.resize((300,300),Image.ANTIALIAS)
    reconstruct= ImageTk.PhotoImage(Image.open("pred1.png"))#.resize((300,300),Image.ANTIALIAS))
    #tk_image = ImageTk.PhotoImage(myImage)
           
    third_image = Label(top, image= reconstruct)#.pack()
    third_image.grid(row=0, column=0, columnspan=2)
    #btn_parameters.grid(row=0, column=3)
    btn_parameters['state'] = NORMAL

def predictValue():

    btn_add_noise['state'] = DISABLED

    btn_reconstruct['state'] = DISABLED
   
    btn_parameters['state'] = DISABLED
    #first_image.grid_forget()
    top3 = Toplevel()
    top3.geometry("100x100")
    top3.title("Values of T1, T2, and T2*")
    

    #################
    #generate parameters in prediction
    
   # TR = predictTR('machine_learning/model_tr.h5', 'labels/TR_labels.txt')#"5"
    #TE = predictTE('machine_learning/model_tr.h5', 'labels/TE_labels.txt') #"2"
    T1 = predictT('machine_learning/model_t1.h5', 'labels/T1_labels.txt') #"2"
    T2 = predictT('machine_learning/model_t2.h5', 'labels/T2_labels.txt') #"2"
    T2dot = predictT('machine_learning/model_t2dot.h5', 'labels/T2dot_labels.txt') #"2"
      # Create text widget and specify size.
    p1 = Label(top3, text= f"T1  = {T1}", foreground="black")
    p2 = Label(top3, text= f"T2  = {T2}", foreground="black")
    p3 = Label(top3, text= f"T2* = {T2dot}", foreground="black")
     
    p1.grid(row=0, column= 0, columnspan=3)
    p2.grid(row=1, column= 0, columnspan=3)
    p3.grid(row=2, column= 0, columnspan=3)

   # btn_parameters.grid_forget()
  

  
   

#image1 = ImageTk.PhotoImage(Image.open("testing/test.png").resize((300,300),Image.ANTIALIAS))
#first_image = Label(image = image1 )
#first_image.grid(row=0, column=0, columnspan=2)
#second_image = Label(image = image1)
#second_image.grid(row=0, column=2, columnspan=2)
#third_image = Label(image = image1)
#third_image.grid(row=0, column=4, columnspan=2)
                
                  
btn_open =  Button(master, text= "Open File" , command = open) #.pack()

btn_add_noise = Button(master, text ="Add Noise", command= noise_image)
btn_reconstruct = Button(master, text="Reconstruct Image", command=reconstruct_image)
btn_parameters = Button(master, text="Predict Values", command=predictValue)



btn_open.grid(row = 0, column= 0)
btn_add_noise.grid(row=0, column= 2)
btn_add_noise['state'] = DISABLED
btn_reconstruct.grid(row=0, column=4)
btn_reconstruct['state'] = DISABLED
btn_parameters.grid(row=0, column = 6)
btn_parameters['state'] = DISABLED

l1 = Label(master, text= f"Original Image", foreground="black")
l2 = Label(master, text= f"K-space of Original Image", foreground="black")
l1.grid(row=2, column=0, columnspan=2)
l2.grid(row=2,column=4, columnspan=2)


master.mainloop()
#app.mainloop()


#for noise pop up image
#top = Toplevel()
#top.title("Noise Image")
#noise_image = ImageTk.PhotoImage("noise image.png")
#noise_label = Label(top, image= noise_image).pack()
#btn2 = Button(top, text="Destroy", command = top.destroy)





#https://www.youtube.com/watch?v=YXPyB4XeYLA
#https://stackoverflow.com/questions/23584325/cannot-use-geometry-manager-pack-inside