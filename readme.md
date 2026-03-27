# Generador de Contraseñas (Python)
La idea es generar contraseñas seguras pidiéndole al usuario la longitud y validando que cumpla ciertos mínimos.


Proyecto simple escrito con Python y utilizando paradigma imperativo.  

## ¿Qué hace?

El programa pide un número y genera una contraseña que tenga:

- 3 mayúsculas  
- 3 minúsculas  
- 3 números  
- 3 caracteres especiales  
- Longitud mínima: 12  
- No acepta 0 ni valores inválidos  

Si la longitud es mayor a 12, completa el resto con caracteres aleatorios.

## ¿Por qué es imperativo?

Porque está hecho paso a paso, modificando variables y usando bucles y condicionales.  
Nada raro: se construye la contraseña agregando elementos a una lista, se mezcla y se devuelve.  
Todo explícito, todo secuencial.

## Cómo usarlo

1. Ejecutás el script.  
2. Ingresás la longitud.  
3. Te devuelve una contraseña que cumple todas las reglas.  


## Requisitos

Solo Python.  
Nada extra, este script no usa librerías externas.
