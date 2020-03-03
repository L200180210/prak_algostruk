lower = 2
upper = 1000
if lower>=1 and upper>1:
    for x in range(lower,upper):
        prima=True
        for i in range(2,x):
            if(x%i==0):
                prima=False
        if prima==True:
            print(x)
else:
    print("Bukan Bilangan Prima")
                    
