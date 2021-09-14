from tkinter import *
from tkinter import ttk
import time
from gpiozero import CPUTemperature
import psutil


root = Tk()
root.title("Raspberry Pi Diagnostic")
root.geometry("600x200")

cpu=CPUTemperature()
use=psutil.cpu_percent()
ram=psutil.virtual_memory()

def diagnose():
    total=0
    total2=0
    total3=0
    for n in range(1,101):
        total+=cpu.temperature
        total2+=use
        total3+=ram.used
        progress['value']+=1
        root.update_idletasks()
        time.sleep(3)
    progress['value']=0
    avg=total/100
    avg2=total2/100
    avg3=((total3/100)/ram.total)*100
    final=round(avg,1)
    final2=round(avg2,1)
    final3=round(avg3,1)
    temp.config(text=f"Average CPU Temp:{final} C")
    usage.config(text=f"Average CPU Usage:{final2} %")
    ram_use.config(text=f"Average Ram Used:{final3} %")

temp=Label(root,text="")
usage=Label(root,text="")
ram_use=Label(root,text="")
button=Button(root, text="Begin Diagnostic", command=diagnose)
progress=ttk.Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')

button.pack(pady=10)
progress.pack()
temp.pack(pady=10)
usage.pack()
ram_use.pack(pady=10)

root.mainloop()