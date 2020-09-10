#Assignment No. 1...............................................

altitude=int(input("Enter the altitude of the plane ="))
if altitude<=1000:
    print("Safe for landing")
elif altitude>1000 and altitude<5000:
    print("Bring down to 1000")
elif altitude>5000:
    print("Turn around")


#Assignment No. 2.......................................

for i in range(1,200): 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i) 