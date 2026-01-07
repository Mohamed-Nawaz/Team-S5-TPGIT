iteration=int(input("Enter no. of Products to be added in bill:"))
i=1
l_product=[]
l_quantity=[]
l_price=[]
sum=0
while iteration>0:
        print("Product:",i)
        product=input("Enter your Product name:")
        l_product.append(product)
        quantity=int(input("Enter quantity:"))
        l_quantity.append(quantity)
        price=int(input("Enter  price:"))
        l_price.append(price)
        iteration-=1

print("----------------------------------------")   
for j in range(len(l_product)):  
    print(l_product[j],' ',l_quantity[j],' x ',l_price[j],' = ',l_quantity[j]*l_price[j])
    sum=sum+(l_quantity[j]*l_price[j])

print("----------------------------------------")
print("Total amount:",sum)
if sum>=500 and sum<1000:
      print("5% Discount!!!")
      print("Final amount:",sum-(sum*(5/100)))
elif sum>=1000 and sum<2000:
    print("10% Discount!!!")
    print("Final amount:",sum-(sum*(10/100)))
elif sum>=2000:
      print("15% Discount!!!")
      print("Final amount:",sum-(sum*(15/100)))
elif sum <500:
      print("No discount avaliable.Purchase above 500 to get offer!")
else:
      pass
