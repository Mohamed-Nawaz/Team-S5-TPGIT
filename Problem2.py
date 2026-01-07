Total_class=float(input("Enter Total no. Classes:"))
if Total_class<=0:
    print("Invalid Input!")
    exit()
attended_class=float(input("Enter Total no. Classes attended:"))
min_class = Total_class*0.75
if attended_class>=min_class:
    print("You are eligible to attend semester examination")
else:
    print("You are not eligible to attend semester examination")
    class_needed = min_class - attended_class
    print("No. of additional classes required:",class_needed)
