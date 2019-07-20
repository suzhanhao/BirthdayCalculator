from datetime import datetime
from tkinter import *

today = datetime.today()


def birthday_count():
    user_input = entry.get()
    info = user_input.split('-')
    user_dob = datetime.strptime(user_input, '%Y-%m-%d')
    for d in info:
        bd_year = int(info[0])
        bd_month = int(info[1])
        bd_day = int(info[2])
    bd_cal = datetime(today.year, bd_month, bd_day)
    if not (bd_cal - today).days > 0:
        bd_cal = datetime(today.year + 1, bd_month, bd_day)
    user_age = Age(today, user_dob)
    user_count = BirthdayCount(today, bd_cal)
    label_age_year = Label(mywindow, text=user_age.age_years())
    label_age_year.grid(row=2, column=1)
    label_age_week = Label(mywindow, text=user_age.age_weeks())
    label_age_week.grid(row=3, column=1)
    label_age_day = Label(mywindow, text=user_age.age_days())
    label_age_day.grid(row=4, column=1)
    label_bdcount = Label(mywindow, text=user_count.get_birthdaycounts())
    label_bdcount.grid(row=5,column=1)


# 生日倒数
class BirthdayCount:
    def __init__(self, td, bd_cal):
        self.today = td
        self.bdcal = bd_cal
        self.del_days = self.bdcal - self.today

    def get_birthdaycounts(self):
        return 'You have %s days to your next birthday!'%self.del_days.days


# 年龄计算
class Age:
    def __init__(self, td, dob):
        self.today = td
        self.DOB = dob
        self.del_days = self.today - self.DOB

    # calculate age in days
    def age_days(self):
        return 'Your age in days: %s days'%self.del_days.days  # 只输出timedelta中days变量的值

    # calculate age in weeks
    def age_weeks(self):
        self.del_weeks = self.del_days.days//7
        self.del_weeks_days = self.del_days.days % 7
        return 'Your age in weeks: %s weeks %s days' % (self.del_weeks, self.del_weeks_days)

    # calculate age in years
    def age_years(self):
        self.del_years = self.del_days.days//365
        self.del_years_weeks = (self.del_days.days - self.del_years*365)//7
        self.del_years_days = (self.del_days.days - self.del_years*365) % 7
        return 'Your age in years: %s years %s weeks %s days' % (self.del_years, self.del_years_weeks, self.del_years_days)


mywindow = Tk()
label_today = Label(mywindow, text='Today is %s' % today.date())
label_input = Label(mywindow, text="Enter your date of birth in y-m-d format: ")
entry = Entry(mywindow)
button_cal = Button(mywindow, text="Click to calculate your result!", command=birthday_count)


label_today.grid(row=0, column=0)
label_input.grid(row=1, column=0)
entry.grid(row=1, column=1)
button_cal.grid(row=2, column=0)


mywindow.title('A Birthday Program')  # 设置窗口标题
mywindow.geometry("600x400")          # 初始窗口的大小
mywindow.mainloop()
