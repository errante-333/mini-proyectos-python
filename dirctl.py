import os
import shutil


while True:
    respuesta = (input("quieres crear un directorio ")).lower().strip()


    if respuesta == "si":
     
         dir_name = (input("que nombre quieres poner a tu carpeta "))

         os.mkdir(dir_name)
         
         continue


    elif respuesta == "no":
     
         rp2 = input("quieres salir o borrar un directorio, 1 salir, 2 borrar un directorio ").strip()



         if rp2 == "1":
              
             break
        
          
         elif rp2 == "2":
               
             dead_dir = (input("como se llama la carpeta que deseas borrar? ")).strip.lower()

             shutil.rmtree(dead_dir)

   

              