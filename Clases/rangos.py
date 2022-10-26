class conf_parametros():
    file="database/Parametros.csv"
    def __init__(self,min_hip,max_hip,min_nor,max_nor,min_fie,max_fie):
        self.min_hip= min_hip
        self.max_hip= max_hip
        self.min_nor= min_nor
        self.max_nor= max_nor
        self.min_fie= min_fie
        self.max_fie= max_fie

    #-----------------------------------------------     
    def save_parametros(self):
        f=open(self.file,"w")
        linea=";".join([str(self.min_hip),str(self.max_hip),str(self.min_nor),str(self.max_nor),str(self.min_fie),str(self.max_fie)])
        f.write(linea+"\n")
        f.close()

#------------------------------------------------------------------------------
def definir_rangos():
    print("Por favor ingrese valores de Hipotermia")
    min_hip=int(input("valor mínimo"))
    max_hip=int(input("valor maximo"))
    print("")

    print("Por favor ingrese valores de Temperatura normal")
    min_nor=int(input("alor mínimo"))
    max_nor=int(input("valor maximo"))
    print("")

    print("Por favor ingrese valores de Fiebre")
    min_fie=int(input("alor mínimo"))
    max_fie=int(input("valor maximo"))
    print("")
    eq=conf_parametros(min_hip,max_hip,min_nor,max_nor,min_fie,max_fie)
    
    return eq
