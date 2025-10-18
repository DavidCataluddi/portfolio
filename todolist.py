#dictionnary
dictionnaire = {"tâches à faire": [] ,"tâches faites": []}

while True:
    try:
        number = int(input("##### Gestionnaire de tâches #####\n1. Ajouter une tâche\n2. Lister les tâches\n3. Marquer une tâche comme faite\n4. Supprimer une tâche\n5. Sauvegarder et quitter\nnombre: "))
        if number == 1:
            tache = input("insérez une tâche à faire: ")
            dictionnaire["tâches à faire"].append(tache)
        elif number == 2:
            print(f"[]{dictionnaire["tâches à faire"]}")
            print(f"[X]{dictionnaire['tâches faites']}")            
    except ValueError:
        print("error, veuillez choisir un nombre intégral")
        continue