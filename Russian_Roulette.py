#russian roulet tool basic

import random

rp = input("empezar la ruleta rusa? ").lower().strip()





if  rp == "si":
       
       user = (input("choose you name."))
       gun = random.randint(1,6)
       proyectil = random.randint(1,6)

       print ("Tambor del revolver", gun,) 

       if gun == proyectil:
        

             print("you die", user,)
                   
       if gun != proyectil:
        
             print("you lives, good intent", user,)

             



elif rp == "no": 

    print ("coward")



else:
    print("respuesta no valida")    




      

