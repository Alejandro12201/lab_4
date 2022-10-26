class menu():
    def __init__(self,laboratorio):
        self.laboratorio = laboratorio

    #-----------------------------------------------  
    def ver(self):
        print("BIENVENIDO AL CONTROL DE TEMPERATURA".center(50,"*"))
        print("Laboratorio 3: "+self.laboratorio)
        print("1. Captura de datos")
        print("2. Configuracion de parametros")
        print("3. Reportes")
        print("4. Salir")
        op=int(input(">>> "))

        return op
            
#------------------------------------------------------------------------------
class Captura_datos():
    def ver(self):
          print("MENU DE CAPTURA DE DATOS".center(50,"*"))
          print("1.Escoger cantidad de datos de captura ")
          print("2.Escoger momento de captura con grafica en tiempo real ")
          op=int(input(">>> "))
          
          return op 

#------------------------------------------------------------------------------
class ver_reporte():
    
    def ver(self):
      print("configuracion de parametros".center(20,"*"))
      print("1. Ver grafica de los datos capturados")
      print("2. Valor maximo")
      print("3. Valor minimo")
      print("4. Promedio de temperatura")
      op=int(input(">>> "))
      
      return op
