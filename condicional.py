animal = input("Escribe un animal: ")

animal = animal.lower()
def determinar(animal):
    if animal == "perro":
        print (f"El {animal} hace waw waw")

    elif animal == "gato":
        print (f"El {animal} hace miaw miaw")
    else: 
        print(f"El animal debe ser igual a perro o gato")
determinar(animal)
