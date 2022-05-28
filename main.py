#creating the fibonacci series

#first make an input for the user
user = int(input("how many terms would you like to enter? : "))

# the first and second terms
n1,n2 = 0,1
counter = 0

#checking if the number of terms is valid
if user <= 0:
    print("enter a positive number")
elif  user == 1:
    print("the series is up to ", user,":")
    print(n1)
else:
    print("the series: ")
    while counter < user:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        counter += 1