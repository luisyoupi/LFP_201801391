ListaPelicualas=[] 
#clase pelicula
class Pelicula:
    def __init__(self, nombreP, actores, año, genero):
        self.nombreP = nombreP
        self.actores = actores
        self.año = año
        self.genero = genero
#esto es para mostrar a los actores de las peliculas
    def mostarinfo(self):
        print("\nNOMBRE PELICULA: ",self.nombreP, "\nACTORES: ", self.actores,"\nAÑO ESTRENO: ", self.año,"\nGENERO: ", self.genero)
     
    def mostrarpeli(self):
       
       print(self.nombreP)
    def mostraractores(self):
       
       print( self.actores) 
#aqui es el filtrado por actor
def filtrarporactor(ListaPelicualas):
    actor = input("Introduzca el nombre del actor: ")
    print("Peliculas en las que ha actuado", actor, ":")
    for peli in ListaPelicualas:
        if actor in peli.actores:
            print(peli.nombreP)

#aqui es el filtrado por año
def filtrarporeanio(ListaPelicualas):
    anio = int(input("Introduzca el año de estreno: "))
    print("Peliculas estrenadas en el año", anio, ":")
    for peli in ListaPelicualas:
        if peli.año == str(anio):
            print(peli.nombreP)

#aqui es el filtrado por género
def filtrarporgenero(ListaPelicualas):
    genero = input("Introduzca el género de la pelicula: ")
    print("Peliculas del genero", genero, ":")
    for peli in ListaPelicualas:
        if peli.genero == genero:
            print(peli.nombreP)    



          
#aqui es para que lea el archivo y lo guarde
def leerArchivoEntrada(lista):
    ruta = input("Escriba la ruta del archivo a leer: ")
    archivo = open(ruta, 'r')
    lineas = archivo.readlines()
    
    for i in lineas:
        i = i.split(";" )
        
        count = 1
        tmp_nombre = None
        tmp_autores = None
        tmp_anio = None
        tmp_genero = None
        for j in i:
            if count == 1:
                tmp_nombre = j
            elif count == 2:
                j = j.split("," )
                tmp_autores = j
            elif count == 3:
                tmp_anio = j
            elif count == 4:
                tmp_genero = j
            count += 1

        peli = Pelicula(tmp_nombre, tmp_autores, tmp_anio, tmp_genero)
        lista.append(peli)
def menu2():
 print("------------menu de gestiones-----------------------")
 print("elija opcion del 1 al 3 ")
 print("1 opcion mostrar peliculas")
 print("2 opcion mostrar actores")
 print("3 regresar")

def menu3():
 print("------------menu de FILTRO-----------------------")
 print("elija opcion del 1 al 3 ")
 print("1 Filtrar por actores")
 print("2 filtrar por año")
 print("3 filtrar por genero")
 print("4 regresar")
        
            
print("-----------------------")
print("BINVENIDOS a practica 1 Luis Fernando Gomez Rendon 201801391 seccion B-")
print("-----------------------")
input()
#este es el menu principal
menu = 0
while menu != 5:
    print("\n-----------------------")
    print("MENU PRINCIPAL")
    print("1 Carga")
    print("2 Gestion")
    print("3 Filtro")
    print("4 Grafico")
    print("5 Salir")
    print("-----------------------")
    print("elija una opcion de 1 a 5:")
    menu = int(input())
    if menu == 1:
       try:
        print("------CARGA DE ARCHIVo----------")
        leerArchivoEntrada(ListaPelicualas)
        print("CARGO EXITOSAMENTE\n")
        for i in ListaPelicualas:
            i.mostarinfo()
       except FileNotFoundError:
        print("por favor ingresar archivo de entrada")
        input()
       

        pass


     #este es el menu de mostra la info
    elif menu == 2:


        menuG = 0
        while menuG != 3:
         menu2()
         menuG =int(input())
        
         if menuG == 1:
             print("---------------------Listado de peliculas ----------------")
             for k in ListaPelicualas:
              k.mostrarpeli()
        
              pass
             
         elif menuG==2:
          print("---------------------Listado de actores ----------------")
          for ñ in ListaPelicualas:
           
           ñ.mostraractores()
          
          pass
         elif menuG==3:
           
         
           pass

      #el menu del filtrado
    elif menu == 3:
        menuFI = 0
        while menuFI != 4:
            menu3()
            menuFI =int(input())
            
            if menuFI == 1:
                print("---------------------Filtrado por actor----------------")
                filtrarporactor(ListaPelicualas)
                
            elif menuFI == 2:
                print("---------------------Filtrado por año----------------")
                filtrarporeanio(ListaPelicualas)
            elif menuFI == 3:
                print("---------------------Filtrado por genero----------------")
                filtrarporgenero(ListaPelicualas)
            elif menuFI == 4:
                pass

    elif menu == 4:
        
        print("GRAFICO")
        pass
    elif menu == 5:
      
        print("gracias por usar el programa practica 1 ")
        break
