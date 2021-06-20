""" Programa calculadora artimética amigable#
    Realiza las 4 operaciones (+,-,* /)
    incorpora al modulo calculadora_aritmetica.py
    Oscar Franco-Bedoya
    Mayo 3-2021 """

#---------------- Zona librerias------------
import functions as f

#=====================================================================


#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
def menu_operaciones():
  print("CALCULADORA AMIGABLE!!!")
  print("==================================================")
  print("| Menú")
  print("==================================================")
  print("| Ingresa un número para realizar la operación.")
  print("==================================================")
  print("| 1. Calcular suma: (1)")
  print("==================================================")
  print("| 2. Calcular la resta: (2)")
  print("==================================================")
  print("| 3. Calcular multiplicación: (3)")
  print("==================================================")
  print("| 4. Calcular división: (3)")
  print("==================================================")
  print('Fixed By: <Nestor A-Dev/>\n')
   
  opcion = int(input())
  return opcion

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
operacion=menu_operaciones()

#Condicionales de eleccion de opciones
#Condicional Suma
if operacion == 1 :
  print('Seleccionaste la opcion' , operacion,'\n\nVAMOS A SUMAR!!\n')
  num1 = float(input('Ingresa el primer sumando: '))
  num2 = float(input('Ingresa el segundo sumando: '))
  print('\nEl resultado es: ',f.sumar_numeros(num1 , num2))

#C ondicional Resta
elif operacion == 2 :
  print('Seleccionaste la opcion' , operacion,'\n\nVAMOS A RESTAR!!\n')
  num1 = float(input('Ingresa el minuendo: '))
  num2 = float(input('Ingresa el sustraendo: '))
  print( '\nEl resultado es: ' ,f.restar_numeros(num1 , num2))
 
#Condicional Multiplicación
elif operacion == 3 :
  print('Seleccionaste la opcion' , operacion,'\n\nVAMOS A MULTIPLICAR!!\n')
  num1 = float(input('Ingresa el multiplicando: '))
  num2 = float(input('Ingresa el multiplicador: '))
  print( '\nEl resultado es: ' ,f.multiplicar_numeros(num1 , num2))

#Condicional División
elif operacion == 4 :
  print('Seleccionaste la opcion' , operacion,'\n\nVAMOS A DIVIDIR!!\n')
  num1 = float(input('Ingresa el dividendo: '))
  num2 = float(input('Ingresa el divisor: '))
  f.dividir_numeros(num1 , num2)

#Avisa al usuario una opcion invalida
else:
  print('\nLa opción es invalida!!, verifica las opciones nuevamente.')


#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
