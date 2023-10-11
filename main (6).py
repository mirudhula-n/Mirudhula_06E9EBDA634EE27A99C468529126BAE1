#Write a program that determines whether a year entered by the user is a leap year or not using if-elif-else statements. 
 def checkLeap(Year): 
   if((Year % 400 == 0) or 
      (Year % 100 != 0) and 
      (Year % 4 == 0)): 
     print("Given Year is a leap Year"); 
   else: 
     print ("Given Year is not a leap year") 
 Year = int(input("Enter the number:")) 
 checkLeap(Year)