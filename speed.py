from tkinter import *
import speedtest

def bytes_to_mb(bytes):
    KB = 1024  # One Kilobyte is 1024 bytes
    MB = KB * 1024  # One MB is 1024 KB
    return str(round(bytes / MB, 2))

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_best_server()

    try:
        downloading = bytes_to_mb(sp.download()) + " Mbps"
        uploading = bytes_to_mb(sp.upload()) + " Mbps"
        lab_down.config(text=downloading)
        lab_up.config(text=uploading)
    except Exception as e:
        lab_down.config(text="Error")
        lab_up.config(text="Error")
        print(f"Speed test failed: {e}")

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x550")
sp.config(bg="black")

lab = Label(sp, text="Internet Speed Test", font=("Times New Roman", 30, "bold"), bg="black", fg="white")
lab.place(x=70, y=40, height=50, width=360)

lab = Label(sp, text="Downloading speed", font=("Times New Roman", 30, "bold"))
lab.place(x=70, y=130, height=50, width=360)

lab_down = Label(sp, text="00 Mbps", font=("Times New Roman", 30, "bold"))
lab_down.place(x=70, y=200, height=50, width=360)

lab = Label(sp, text="Uploading speed", font=("Times New Roman", 30, "bold"))
lab.place(x=70, y=290, height=50, width=360)

lab_up = Label(sp, text="00 Mbps", font=("Times New Roman", 30, "bold"))
lab_up.place(x=70, y=360, height=50, width=360)

button = Button(sp, text="Check speed", font=("Times New Roman", 30, "bold"), relief=RAISED, bg="green", command=speedcheck)
button.place(x=70, y=460, height=50, width=360)

sp.mainloop()






