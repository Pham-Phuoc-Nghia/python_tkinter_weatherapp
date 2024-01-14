from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather Application")
root.geometry("900x500+300+200")
root.resizable(False,False)


#search boxes

search_box = StringVar()
search_box.set("")
search_box_label = Label(root,text="Enter City Name",font=("times new roman",15))
search_box_label.grid(row=0,column=0)
search_box_entry = Entry(root,textvariable=search_box) 

root.mainloop()