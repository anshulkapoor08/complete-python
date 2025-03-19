h = int(input())
m = int(input())
s = int(input())
while(h<24):
    while(m<60):
        while(s<60):
            if(h<12):
                print("Time is: ",h,":",m,":",s," AM")
                print("Good Morning") 
                break
            else:
                print("Time is: ",h,":",m,":",s," PM")
                print("Good Evening")
                break            
# above code executes infinite times, so we need to break the loop but it is not breaking the loop 