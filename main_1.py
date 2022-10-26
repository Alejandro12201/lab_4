from Clases.menu import *
from Clases.rangos import *
from Clases.obtencion import *
from Clases.reporte import *
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import sys

#------------------------------------------------------------------------------
global pause
pause = False
global y_data
y_data = []

#------------------------------------------------------------------------------
def onclick(event):
    global pause
    print("pausa")
    pause=True
    
#------------------------------------------------------------------------------
fig, ax=plt.subplots()
fig.canvas.mpl_connect("button_press_event", onclick)
            
#------------------------------------------------------------------------------
def update_data(i): 
    if not pause:
        #dato=Puerto.leer(op_pu)
        dato=int(puerto.readline().decode().strip())
        print(dato)
        y_data.append(dato)
        ax.clear()
        ax.plot(y_data)
        time.sleep(1)
        
#------------------------------------------------------------------------------
def main():
    Menu=menu("Escuela colmbiana de ingeniería julio garavito")
    op=Menu.ver()

    #----------------------------------------------- 
    if op==1:
        menu2= Captura_datos()
        op2=menu2.ver()
        if op2==1:
            obtener_1()
            main()
        elif op2== 2:
            print("RECUERDE CERRAR LA VENTANA DE LA GRÁFICA DE TIEMPO REAL PARA CONTINUAR")
            ani= animation.FuncAnimation(fig,update_data)
            plt.show()
            #print(y_data)
            save_dato(y_data)
            main()
        else:
            print("opcion incorrecta")
            main()

    #----------------------------------------------- 
    elif op==2:
        eq=definir_rangos()
        eq.save_parametros()
        main()

    #----------------------------------------------- 
    elif op==3:
        menu2=ver_reporte()
        op2=menu2.ver()
        if op2==1:
            grafiquita()
            main()
        elif op2==2:
            valor_max()
            main()
        elif op2==3:
            valor_min()
            main()
        elif op2==4:
            prom_temp()
            main()
        else:
            print("Opcion incorrecta, por favor intente de nuevo")
            main()

    #----------------------------------------------- 
    elif op == 4:
        print(sys.exit("Hasta lueguito bye bye"))

    #----------------------------------------------- 
    else:
        print("opcion incorrecta, por favor intente de nuevo")
        main()

#------------------------------------------------------------------------------
if __name__=='__main__':
    main()
    