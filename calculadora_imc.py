


print("Bienvenido a la calculadora de imc de el sistema")

peso = float(input("¿Cual es tu peso en kilogramos?"))

altura = float(input("¿ y Cual es tu altura en metros ?"))

preimc = (altura * altura)   # 👈 ahora sí es altura al cuadrado

imc = (peso / preimc)        # 👈 ahora sí fórmula correcta

print(f"este es tu imc {imc}")


