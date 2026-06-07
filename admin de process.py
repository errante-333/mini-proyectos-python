
import webbrowser
import os
import shutil

def sub_menu():
    print("1-Crear un directorio")
    print("2-Borrar un directorio")
    print("salir")

def menusito():
   print("1-Youtube")
   print("2-Github")
   print("3-Chat gpt")
   print("4-Python wiki")
   print("5-salir")

def menu_system():
   print("1-crear carpeta")
   print("2-borrar carpeta")
   print("3-cerrar el programa")

  


decisión = input("quieres usar el menu web o el menu de sistema,respondecon w o s ").lower().strip()


if decisión == "w":

 menusito()
 while True:
          
     rp = input("Abrir?, digite el numero ")
    

     if rp == "1":
          
          webbrowser.open("https://www.youtube.com")
          print("Un poco de entretenimiento, diviertete, pero no demasiado, programa")

     elif rp == "2":
          
          webbrowser.open("https://www.github.com")

          print("Disfruta tus repos y proyectos")

     elif rp == "3":
          
          webbrowser.open("https://chatgpt.com")

          print("inspirate pero no copies")    

     elif rp == "4":
          
          webbrowser.open("https://www.python.org/")

          print("Volviendo a las bases eh?, haces bien")  

     elif rp == "5":
          
          print("Nos vemos en  una proxima instancia con suerte habra mejores funciones")  
          break

          
     else:
        
      print("opcion no valida")
      continue


 sub_menu()



elif decisión == "s":

     sub_menu()

     while True:

      respuesta = (input("que haras?"))
     
      if respuesta == "1":
        
       dir_ectory = input("cual es el nombre que vas a poner, digitalo a continuación. ")
       os.mkdir(dir_ectory)

      elif respuesta == "2":
         dead_dir = input("Pon el nombre de la carpeta a eliminar")
         shutil.rmtree(dead_dir)
         print("borrado con exito")

      elif respuesta == "3":
       
       break
      
      else:
         print("respuesta no valida")
         continue

