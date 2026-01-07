iteration=int(input("Enter of entries to be added:"))
i=0
sname=[]
sdept=[]
while iteration>0:

        name=input("\nEnter your name:")
        sname.append(name)
        dept=input("\nEnter your department name:")
        sdept.append(dept)
        iteration-=1
for j in range(len(sname)):  
    print("\nSeat ",j+1,'-',sname[j],'(',sdept[j],')')
