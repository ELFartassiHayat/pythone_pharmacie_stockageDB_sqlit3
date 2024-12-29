import sqlite3

class Medicament:
    def __init__(self, db_name="pharmacy.db"):
        self.conn = sqlite3.connect(db_name)
        
        self.conn.execute("PRAGMA foreign_keys = ON;")

    def AjouterMedicament(self, nom, prix, quantite, fournisseur_id):
     cursor = self.conn.execute("SELECT * FROM Fournisseur WHERE ID_Fournisseur=?", (fournisseur_id,))
     fournisseur = cursor.fetchone()

     if fournisseur:
       
        self.conn.execute('''INSERT INTO Medicament (Nom_Medicament, Prix, Quantite_Stock, ID_Fournisseur) 
                             VALUES (?, ?, ?, ?)''', (nom, prix, quantite, fournisseur_id))
        self.conn.commit()
        print(f"Médicament '{nom}' ajouté avec succès.")
     else:
       
        print(f"Aucun fournisseur avec l'ID {fournisseur_id} trouvé.")


    def DeleteMedicament(self, medicament_id):
        cursor = self.conn.execute("SELECT * FROM Medicament WHERE ID_Medicament=?", (medicament_id,))
        
        medicament = cursor.fetchone()
        
        if medicament:
            self.conn.execute("DELETE FROM Medicament WHERE ID_Medicament=?", (medicament_id,))
            self.conn.commit()
            print(f"Médicament ID {medicament_id} supprimé.")
        else:
            print(f"Aucun médicament avec l'ID {medicament_id} trouvé.")



    def ModifierPrix(self, medicament_id, nouveau_prix):
        cursor = self.conn.execute("SELECT * FROM Medicament WHERE ID_Medicament=?", (medicament_id,))
        medicament = cursor.fetchone()
        if medicament:
            self.conn.execute("UPDATE Medicament SET Prix=? WHERE ID_Medicament=?", (nouveau_prix, medicament_id))
            self.conn.commit()
            print(f"Le prix du médicament ID {medicament_id} a été modifié.")
        else:
            print(f"Aucun médicament avec l'ID {medicament_id} trouvé.")

    def AfficherMedicaments(self):
        cursor = self.conn.execute("SELECT * FROM Medicament")
        medicaments = cursor.fetchall()
        if medicaments:
            for med in medicaments:
                print(f"ID: {med[0]}, Nom: {med[1]}, Prix: {med[2]}, Quantité: {med[3]}, Fournisseur ID: {med[4]}")
        else:
            print("Aucun médicament trouvé.")


class Fournisseur:
    def __init__(self, db_name="pharmacy.db"):
        self.conn = sqlite3.connect(db_name)
        
        self.conn.execute("PRAGMA foreign_keys = ON;")

    def AjouterFournisseur(self, nom, telefone):
        self.conn.execute('''INSERT INTO Fournisseur (Nom_Fournisseur, Téléphone) 
                             VALUES (?, ?)''', (nom, telefone))
        self.conn.commit()
        print(f"Fournisseur '{nom}' ajouté avec succès.")

    def DeleteFournisseur(self, ID_Fournisseur):
        cursor = self.conn.execute("SELECT * FROM Fournisseur WHERE ID_Fournisseur=?", (ID_Fournisseur,))
        fournisseur = cursor.fetchone()
        if fournisseur:
            self.conn.execute("DELETE FROM Fournisseur WHERE ID_Fournisseur=?", (ID_Fournisseur,))
            self.conn.commit()
            print(f"Fournisseur ID {ID_Fournisseur} supprimé.")
        else:
            print(f"Aucun fournisseur avec l'ID {ID_Fournisseur} trouvé.")

    def ModifierFournisseur(self, ID_Fournisseur, nouveau_num):
        cursor = self.conn.execute("SELECT * FROM Fournisseur WHERE ID_Fournisseur=?", (ID_Fournisseur,))
        fournisseur = cursor.fetchone()
        if fournisseur:
            self.conn.execute("UPDATE Fournisseur SET Téléphone = ? WHERE ID_Fournisseur = ?", (nouveau_num, ID_Fournisseur))
            self.conn.commit()
            print(f"Le téléphone du fournisseur ID {ID_Fournisseur} a été modifié.")
        else:
            print(f"Aucun fournisseur avec l'ID {ID_Fournisseur} trouvé.")

    def AfficherFournisseur(self):
        cursor = self.conn.execute("SELECT * FROM Fournisseur")
        fournisseurs = cursor.fetchall()
        if fournisseurs:
            for row in fournisseurs:
                print(row)
        else:
            print("Aucun fournisseur trouvé.")


class Client:
    def __init__(self, db_name="pharmacy.db"):
        self.conn = sqlite3.connect(db_name)
        
        self.conn.execute("PRAGMA foreign_keys = ON;")

    def AjouterClient(self, Nom_Client, Téléphone):
        self.conn.execute('''INSERT INTO Client (Nom_Client, Téléphone) 
                             VALUES (?, ?)''', (Nom_Client, Téléphone))
        self.conn.commit()
        print(f"Client '{Nom_Client}' ajouté avec succès.")

    def DeleteClient(self, ID_Client):
        cursor = self.conn.execute("SELECT * FROM Client WHERE ID_Client=?", (ID_Client,))
        client = cursor.fetchone()
        if client:
            self.conn.execute("DELETE FROM Client WHERE ID_Client=?", (ID_Client,))
            self.conn.commit()
            print(f"Client d'ID {ID_Client} supprimé.")
        else:
            print(f"Aucun client avec l'ID {ID_Client} trouvé.")

    def Modifier_num_Client(self, ID_Client, nouveau_numero):
        cursor = self.conn.execute("SELECT * FROM Client WHERE ID_Client=?", (ID_Client,))
        client = cursor.fetchone()
        if client:
            self.conn.execute("UPDATE Client SET Téléphone=? WHERE ID_Client=?", (nouveau_numero, ID_Client))
            self.conn.commit()
            print(f"Le numéro du client d'ID {ID_Client} a été modifié.")
        else:
            print(f"Aucun client avec l'ID {ID_Client} trouvé.")

    def AfficherClient(self):
        clients = self.conn.execute("SELECT * FROM Client").fetchall()
        if clients:
            for client in clients:
                print(f"ID_Client: {client[0]}, Nom_Client: {client[1]}, Téléphone: {client[2]}")
        else:
            print("Aucun CLIENT trouvé.")


class Commande:
    def __init__(self, db_name="pharmacy.db"):
        self.conn = sqlite3.connect(db_name)
        
        self.conn.execute("PRAGMA foreign_keys = ON;")

    def AjouterCommande(self, Date_Commande, id_client, medicament_id):
     cursor = self.conn.execute("SELECT * FROM Client WHERE ID_Client=?", (id_client,))
     client = cursor.fetchone()

    
     cursor = self.conn.execute("SELECT * FROM Medicament WHERE ID_Medicament=?", (medicament_id,))
     medicament = cursor.fetchone()

     if client and medicament:
        
        self.conn.execute('''INSERT INTO Commande (Date_Commande, Id_Client, Id_Medicament) 
                             VALUES (?, ?, ?)''', (Date_Commande, id_client, medicament_id))
        self.conn.commit()
        print("Commande ajoutée avec succès.")
     else:
        if not client:
            print(f"Aucun client avec l'ID {id_client} trouvé.")
        if not medicament:
            print(f"Aucun médicament avec l'ID {medicament_id} trouvé.")


    def DeleteCommande(self, Commande_id):
        cursor = self.conn.execute("SELECT * FROM Commande WHERE ID_Commande=?", (Commande_id,))
        commande = cursor.fetchone()
        if commande:
            self.conn.execute("DELETE FROM Commande WHERE ID_Commande=?", (Commande_id,))
            self.conn.commit()
            print(f"Commande ID {Commande_id} supprimée.")
        else:
            print(f"Aucune commande avec l'ID {Commande_id} trouvée.")

    def ModifierCommande(self, Commande_id, medicament_id):
     cursor = self.conn.execute("SELECT * FROM Commande WHERE ID_Commande=?", (Commande_id,))
     commande = cursor.fetchone()

     cursor = self.conn.execute("SELECT * FROM Medicament WHERE ID_Medicament=?", (medicament_id,))
     medicament = cursor.fetchone()

     if commande:
        if medicament:
            
            self.conn.execute("UPDATE Commande SET Id_Medicament=? WHERE ID_Commande=?", 
                              (medicament_id, Commande_id))
            self.conn.commit()
            print(f"Les infos de la commande ID {Commande_id} ont été modifiées.")
        else:
            print(f"Aucun médicament avec l'ID {medicament_id} trouvé.")
     else:
        print(f"Aucune commande avec l'ID {Commande_id} trouvée.")


    def AfficherCommandes(self):
        cursor = self.conn.execute("SELECT * FROM Commande")
        commandes = cursor.fetchall()
        if commandes:
            for cmd in commandes:
                print(f"ID: {cmd[0]}, Date: {cmd[1]}, Client ID: {cmd[2]}, Médicament ID: {cmd[3]}")
        else:
            print("Aucune commande trouvée.")


  
if __name__ == "__main__":
    manager_medicament = Medicament()
    manager_fournisseur = Fournisseur()
    manager_client = Client()
    manager_commande = Commande()

    while True:
       
        print("\n--- Menu Principal ---")
        print("1. Gérer les Médicaments")
        print("2. Gérer les Fournisseurs")
        print("3. Gérer les Clients")
        print("4. Gérer les Commandes")
        print("5. Quitter")

        choix = input("Entrez votre choix: ")
        
        
        if choix == '1':
            
            while True:
                print("\n--- Menu Médicament ---")
                print("1. Ajouter un médicament")
                print("2. Supprimer un médicament")
                print("3. Modifier le prix d'un médicament")
                print("4. Afficher les médicaments")
                print("5. Retour au menu principal")

                choix_medicament = input("Entrez votre choix: ")
                if choix_medicament == '1':
                    
                    nom = input("Nom du médicament: ")
                    prix = float(input("Prix: "))
                    quantite = int(input("Quantité en stock: "))
                    fournisseur_id = int(input("ID du fournisseur: "))
                    manager_medicament.AjouterMedicament(nom, prix, quantite, fournisseur_id)
                    
                    
                    
                elif choix_medicament == '2':
                    medicament_id = int(input("ID du médicament à supprimer: "))
                    manager_medicament.DeleteMedicament(medicament_id)
                    
                    
                elif choix_medicament == '3':
                    
                    medicament_id = int(input("ID du médicament: "))
                    nouveau_prix = float(input("Nouveau prix: "))
                    manager_medicament.ModifierPrix(medicament_id, nouveau_prix)
                    
                    
                elif choix_medicament == '4':
                    manager_medicament.AfficherMedicaments()
                elif choix_medicament == '5':
                    break
                else:
                    print("Choix invalide. Veuillez réessayer.")
        
        
        elif choix == '2':
            
            while True:
                print("\n--- Menu Fournisseur ---")
                print("1. Ajouter un fournisseur")
                print("2. Supprimer un fournisseur")
                print("3. Modifier le téléphone d'un fournisseur")
                print("4. Afficher les fournisseurs")
                print("5. Retour au menu principal")

                choix_fournisseur = input("Entrez votre choix: ")
                if choix_fournisseur == '1':
                    nom = input("Nom du fournisseur: ")
                    telephone = input("Téléphone: ")
                    manager_fournisseur.AjouterFournisseur(nom, telephone)
                    
                    
                elif choix_fournisseur == '2':
                    
                    fournisseur_id = int(input("ID du fournisseur à supprimer: "))
                    manager_fournisseur.DeleteFournisseur(fournisseur_id)
                    
                elif choix_fournisseur == '3':
                    
                    fournisseur_id = int(input("ID du fournisseur: "))
                    nouveau_num = input("Nouveau numéro de téléphone: ")
                    manager_fournisseur.ModifierFournisseur(fournisseur_id, nouveau_num)
                    
                    
                elif choix_fournisseur == '4':
                    manager_fournisseur.AfficherFournisseur()
                elif choix_fournisseur == '5':
                    break
                else:
                    print("Choix invalide. Veuillez réessayer.")
        
       
        elif choix == '3':
            
            while True:
                print("\n--- Menu Client ---")
                print("1. Ajouter un client")
                print("2. Supprimer un client")
                print("3. Modifier le téléphone d'un client")
                print("4. Afficher les clients")
                print("5. Retour au menu principal")

                choix_client = input("Entrez votre choix: ")
                if choix_client == '1':
                    
                    nom = input("Nom du client: ")
                    telephone = input("Téléphone: ")
                    manager_client.AjouterClient(nom, telephone)
                    
                elif choix_client == '2':
                    
                    client_id = int(input("ID du client à supprimer: "))
                    manager_client.DeleteClient(client_id)
                    
                elif choix_client == '3':
                    
                    client_id = int(input("ID du client: "))
                    nouveau_numero = input("Nouveau numéro de téléphone: ")
                    manager_client.Modifier_num_Client(client_id, nouveau_numero)
                    
                    
                elif choix_client == '4':
                    manager_client.AfficherClient()
                    
                elif choix_client == '5':
                    break
                else:
                    print("Choix invalide. Veuillez réessayer.")
        
       
        elif choix == '4':
            
            while True:
                print("\n--- Menu Commande ---")
                print("1. Ajouter une commande")
                print("2. Supprimer une commande")
                print("3. Modifier une commande")
                print("4. Afficher les commandes")
                print("5. Retour au menu principal")

                choix_commande = input("Entrez votre choix: ")
                if choix_commande == '1':
                    
                    date = input("Date de la commande: ")
                    client_id = int(input("ID du client: "))
                    medicament_id = int(input("ID du médicament: "))
                    manager_commande.AjouterCommande(date, client_id, medicament_id)
                    
                elif choix_commande == '2':
                    
                    commande_id = int(input("ID de la commande à supprimer: "))
                    manager_commande.DeleteCommande(commande_id)
                    
                    
                elif choix_commande == '3':
                    
                    commande_id = int(input("ID de la commande: "))
                    medicament_id = int(input("Nouveau médicament ID: "))
                    manager_commande.ModifierCommande(commande_id, medicament_id)
                    
                    
                    
                elif choix_commande == '4':
                    manager_commande.AfficherCommandes()
                elif choix_commande == '5':
                    break
                else:
                    print("Choix invalide. Veuillez réessayer.")
        
        elif choix == '5':
            print("Au revoir!")
            break
        
        else:
            print("Choix invalide. Veuillez réessayer.")