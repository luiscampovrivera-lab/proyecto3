nombre1 = input("Escriba primer nombre:")
nombre2 = input("Escriba segundo nombre:")
apellido = input("Escriba apellido:")
dominio = "@istlatroncal.edu.ec"
correo = nombre1[0] + nombre2[0] + apellido + dominio
print(f"{nombre1 [0]}{nombre2 [0]}{ apellido}{dominio}")
print(correo)


estudiante1 = [{nombre1} , {nombre2} , {apellido} , {correo} ]
print(estudiante1)
estudiantes_istlt = []
estudiantes_istlt.append(estudiante1)
print(estudiantes_istlt)


palabra = input("Palabra: ")
palabra_reversa = palabra [::-1]
print(f"¿es palindrome? {palabra == palabra_reversa}")
palindrome = [palabra]
print(palindrome)
