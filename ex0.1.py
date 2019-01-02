hour=(input('enter hours='))
pay=50 #per hour
try:
     hour=int(hour)
     if hour>=45:
          hour=float(hour)
          to_pay=hour*pay*1.5
          print(to_pay)
     else:
          to_pay=hour*pay
          print(to_pay)
     print("Thank you  !!")
except:
     print('try again nonsense...!!!')
