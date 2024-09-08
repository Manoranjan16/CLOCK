import tkinter as tk
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime("%I")
    mi = time.strftime("%M")
    sec = time.strftime("%S")
    ap = time.strftime("%p")
    
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")
    
    lab_hour.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    
    lab_date.config(text=date)
    lab_month.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)
    
    lab_hour.after(200, date_time)

clock = tk.Tk()
clock.title("Digital Clock")
clock.geometry("1000x500")
clock.iconbitmap("bell.ico")
clock.config(bg="#173B45")

digital_time = tk.Label(clock, text="Manoranjan Digital Clock", font=("Time New Roman",20,"bold"),bg="green",fg="#EE4E4E")
digital_time.place(x=220,y=10, height=30, width=400)
lab_hour = tk.Label(clock, text="00", font=("Time New Roman",50,"bold"),bg="green",fg="#EE4E4E")
lab_hour.place(x=100,y=60, height=100, width=100)
lab_min = tk.Label(clock, text="00", font=("Time New Roman",50,"bold"),bg="green",fg="#EE4E4E")
lab_min.place(x=280,y=60, height=100, width=100)
lab_sec = tk.Label(clock, text="00", font=("Time New Roman",50,"bold"),bg="green",fg="#EE4E4E")
lab_sec.place(x=460,y=60, height=100, width=100)
lab_AM_PM = tk.Label(clock, text="AM", font=("Time New Roman",38,"bold"),bg="green",fg="#EE4E4E")
lab_AM_PM.place(x=640,y=60, height=100, width=100)

lab_hour_name = tk.Label(clock, text="Hour", font=("Time New Roman",25,"bold"),bg="green",fg="#EE4E4E")
lab_hour_name.place(x=100,y=180, height=60, width=100)
lab_min_name = tk.Label(clock, text="Min.", font=("Time New Roman",25,"bold"),bg="green",fg="#EE4E4E")
lab_min_name.place(x=280,y=180, height=60, width=100)
lab_sec_name = tk.Label(clock, text="Sec.", font=("Time New Roman",25,"bold"),bg="green",fg="#EE4E4E")
lab_sec_name.place(x=460,y=180, height=60, width=100)
lab_AM_PM_name = tk.Label(clock, text="AM/PM", font=("Time New Roman",22,"bold"),bg="green",fg="#EE4E4E")
lab_AM_PM_name.place(x=640,y=180, height=60, width=100)

lab_date = tk.Label(clock, text="09", font=("Time New Roman",50,"bold"),bg="green",fg="#EE4E4E")
lab_date.place(x=100,y=260, height=100, width=100)
lab_month = tk.Label(clock, text="08", font=("Time New Roman",50,"bold"),bg="green",fg="#EE4E4E")
lab_month.place(x=280,y=260, height=100, width=100)
lab_year = tk.Label(clock, text="24", font=("Time New Roman",50,"bold"),bg="green",fg="#EE4E4E")
lab_year.place(x=460,y=260, height=100, width=100)
lab_day = tk.Label(clock, text="Fri", font=("Time New Roman",36,"bold"),bg="green",fg="#EE4E4E")
lab_day.place(x=640,y=260, height=100, width=100)

lab_date_name = tk.Label(clock, text="Date", font=("Time New Roman",22,"bold"),bg="green",fg="#EE4E4E")
lab_date_name.place(x=100,y=380, height=60, width=100)
lab_month_name = tk.Label(clock, text="Month", font=("Time New Roman",22,"bold"),bg="green",fg="#EE4E4E")
lab_month_name.place(x=280,y=380, height=60, width=100)
lab_year_name = tk.Label(clock, text="Year", font=("Time New Roman",22,"bold"),bg="green",fg="#EE4E4E")
lab_year_name.place(x=460,y=380, height=60, width=100)
lab_day_name = tk.Label(clock, text="Day", font=("Time New Roman",22,"bold"),bg="green",fg="#EE4E4E")
lab_day_name.place(x=640,y=380, height=60, width=100)

date_time()
clock.mainloop()