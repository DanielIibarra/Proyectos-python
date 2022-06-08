def time_calculator(inicio,final,dia=""):
    
    min = 0
    hrs = 0
    count=0
    count2=0
    count3=0
    msg="" 
    dias=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",]
    hinicial = inicio.split(" ")
    hinicial1 = hinicial[0].split(":")
    hfinal = final.split(":")
    min=int(hinicial1[1])+int(hfinal[1])
    hrs=int(hinicial1[0])+int(hfinal[0])
    horario=hinicial[1]
    while min > 59:
        min=min-60
        hrs=hrs+1 
    while hrs >= 12:
        hrs=hrs-12
        count=count+1
        if horario=="PM" and count==1:
            horarior="AM"
        elif horario=="AM" and count==1:
            horarior="PM"
        elif horario=="PM" and count==count%2:
            horarior="PM"
        elif horario=="AM" and count==count%2:
            horarior="AM"
        elif horario=="PM" and count==count%1:
            horarior="AM"
        elif horario=="AM" and count==count%1:
            horarior="PM"
        
        if count >= 1:
            if count==2 or count==1 and horario!=horarior:
                msg="next day"
            else:
                msg= int(count/2),"days later"
    if dia!= "":
        count2=count
        while count2 >= 2:
            count2=count2-2
            count3=count3+1
            while count2>=14:
                count2=count2-14
                
    if dia!="":
        print(hrs,":",min,horarior,dias[dias.index(dia)+count3],msg)
    else:
        print(hrs,":",min,horarior,msg)

    
time_calculator("6:30 PM", "205:12")