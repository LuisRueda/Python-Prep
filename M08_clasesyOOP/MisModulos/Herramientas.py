class HerramientasImp:

    def __init__(self, lista):
        assert type(lista) == list, f'{lista} no es una lista, se espera una lista de números enteros'
        #self.lista = lista
        if (len(lista) == 0):
            self.lista = []
            raise ValueError('Se ha creado una lista vacía. Se esperaba una lista de números enteros')  
        else:
            self.lista = lista
        
        

    def __verificar_primo(self,numero):
        primo=True
        for i in range(2,numero):
            if numero%i==0:
                primo=False
                break
        if primo==True:
            return True
        else:
            return False
        
    def __valor_modal(self,lista):
        Cuenta=0
        Numero=None
        for i in lista:
            cuenta_Temp=lista.count(i)
            if cuenta_Temp>Cuenta:
                Cuenta=cuenta_Temp
                Numero=i
        return Numero, Cuenta
    
    __celsius2farenheit = lambda self, x: (x*(9/5)) + 32
    __celsius2kelvin = lambda self, x: x + 273.15
    __farenheit2celsius = lambda self, x: (x-32)*(5/9)
    __kelvin2celsius = lambda self, x: x-273.15
    
    def __convert_temperaturas (self,medida,escala_orig,escala_des):
        if escala_orig=='C' and escala_des=='F':
            return self.__celsius2farenheit(medida)
        elif escala_orig=='C' and escala_des=='K':
            return self.__celsius2kelvin(medida)
        elif escala_orig=='F' and escala_des=='C':
            return self.__farenheit2celsius(medida)
        elif escala_orig=='K' and escala_des=='C':
            return self.__kelvin2celsius(medida)
        elif escala_orig=='K' and escala_des=='F':
            return self.__celsius2farenheit(self.__kelvin2celsius(medida))
        elif escala_orig=='F' and escala_des=='K':
            return self.__kelvin2celsius(self.__celsius2farenheit(medida))
        elif escala_orig==escala_des:
            return medida
        else:
            return 'Escoja una opción valida'
    def __factorial (self,numero):
        if numero>1:
            resultado=numero*self.__factorial(numero-1)
            return resultado
        else:
            return 1
    #primos
    def validar_primos (self):
        primos = []
        for i in self.lista:
            if self.__verificar_primo(i)==True:
                primos.append(i)
                #print('El numero',i,'es primo')
            else:
                #print('El numero',i,'no es primo')
                pass
        return primos
    #modal
    def validar_modal (self):
        numero, cuenta = self.__valor_modal(self.lista)
        #print ('El número', numero, 'es el que mas se repite con un total de', cuenta,'veces')
        return numero, cuenta
    
    #grados
    def __escoger_nombre_temperatura(self,opcion):
        nombres = ('Celsius', 'Farenheit', 'Kelvin')
        if opcion=='C':
            return 'Celsius'
        elif opcion=='F':
            return 'Farenheit'
        elif opcion=='K':
            return 'Kelvin'
        else:
            return None

    def validar_conversion(self,origen,destino):
        nombre_origen=self.__escoger_nombre_temperatura(origen)
        nombre_destino=self.__escoger_nombre_temperatura(destino)
        convertidas=[]
        if nombre_origen==None or nombre_destino==None:
            print('Los párametros esperados son C F ó K')
        else:
            for i in self.lista:
                convertidas.append(self.__convert_temperaturas(i,origen,destino))
                #print('El valor para una temperatura de {0} {1} a {2} es: {3:.2f} {2}'.format(i,nombre_origen,nombre_destino,self.__convert_temperaturas(i,origen,destino)))
        return convertidas

    #factorial
    def validar_factorial(self):
        factoriales=[]
        for i in self.lista:
            factoriales.append(self.__factorial(i))
            #print('El factorial de',i,'es:',self.__factorial(i))
        return factoriales