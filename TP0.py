def menu():
    Choix: int
    choixValide: bool = False


    print("bienvenue au jeu du nombre mystère !")
    print("facile(1): nombre entre 1 et 19, 10 essais")
    print("normal(2): nombre entre 1 et 49, 5 essais")
    print("difficile(3): nombre entre 1 et 99, 5 essais")
    print("impossible(4): nombre entre 1 et 999, 1 essais")

    choix = int(input("veuillez entrer votre choix(1, 2, 3, ou 4): "))
    match choix:
        case 1:
         print("1")
        case 2:
         print("2")
        case 3:
         print("3")
        case 4:
         print("4")