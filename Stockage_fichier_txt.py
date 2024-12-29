import os

class FileManager:
    def __init__(self):
        self.filename = "data.txt"
    
    def handle_txt_file(self):
        file_path = os.path.join(os.getcwd(), self.filename)
        while True:
            print("\nChoisissez une option:")
            print("1. Ajouter un élément")
            print("2. Ajouter une liste d'éléments")
            print("3. Lister les éléments")
            print("4. Quitter")
            
            choice = input("Entrez votre choix: ")
            
            if choice == '1':
                element = input("Entrez l'élément à ajouter: ")
                with open(file_path, 'a') as file:
                    file.write(element.strip() + "\n")
                print(f"Élément '{element}' ajouté.")
            
            elif choice == '2':
                elements = input("Entrez les éléments à ajouter (séparés par des virgules): ")
                element_list = elements.split(',')
                with open(file_path, 'a') as file:
                    for element in element_list:
                        file.write(element.strip() + "\n")
                print(f"{len(element_list)} éléments ajoutés.")
            
            elif choice == '3':
                try:
                    with open(file_path, 'r') as file:
                        lines = file.readlines()
                    print("\nÉléments dans le fichier:")
                    for line in lines:
                        print(line.strip())
                except FileNotFoundError:
                    print("Le fichier n'existe pas encore.")
            
            elif choice == '4':
                break
            
            else:
                print("Choix invalide. Essayez à nouveau.")
    

if __name__ == "__main__":
    file_manager = FileManager()
    file_manager.handle_txt_file()
