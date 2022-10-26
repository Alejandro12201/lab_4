import serial
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
pause=False

try:
    global puerto
    puerto = serial.Serial("COM12",9600)
    puerto.close()
    puerto.open()
    print("Port is open")
except:
    print("Problemas abriendo puerto :( ")
    
def onclick(event):
    global pause
    print("pausa")
    pause=True


fig, ax=plt.subplots()
fig.canvas.mpl_connect("button_press_event", onclick)
y_data=[]

def update_data(i):#parametro i para que tome referencia de que punto debe ir mostrando 
    if not pause:
        punto=puerto.readline().decode().strip()
        print(punto)
        y_data.append(punto)
        ax.clear()
        ax.plot(y_data)

ani= animation.FuncAnimation(fig,update_data)
plt.show()

'''
class obtener_2(puerto):
    def __init__(self):
        self.min= min
    def onclick(self,event):
        global pause
        print("pausa")
        pause=True
    def update_data(self,puerto):#parametro i para que tome referencia de que punto debe ir mostrando 
        if not pause:
            print(self.puerto)
            #punto = int(self.puerto.readline()).decode().strip()
            #print(punto)
            #y_data.append(punto)
            #ax.clear()
            #ax.plot(y_data)


'''