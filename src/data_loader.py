import csv
import os


class CsvCreator():

    def create_csv_file(self, file_path, name, quantity, price, category):
        """
        Ajoute un produit dans un fichier CSV spécifié par ses paramètres. Si
        le fichier n'existe pas, il est créé avec les en-têtes.

        :param file_path: Chemin du fichier à créer ou modifier.
        :param name: Nom du produit.
        :param quantity: Quantité du produit.
        :param price: Prix unitaire du produit.
        :param category: Catégorie du produit.
        """
        headers = ["Nom du produit", "Quantite", "Prix unitaire", "Categorie"]
        data = {
            "Nom du produit": name,
            "Quantite": quantity,
            "Prix unitaire": price,
            "Categorie": category
        }

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Vérifie si le fichier existe déjà
        file_exists = os.path.exists(file_path)

        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)

        print(f"Produit ajouté : {name} dans {file_path}")

    def generate_test_csv_files(self):
        """
        Génère plusieurs fichiers CSV contenant
        des données d'inventaire fictives.
        """
        # Electronique
        self.create_csv_file("csv/electronique_inventory.csv",
                             "Smartphone", 50, 799.99, "Electronique")
        self.create_csv_file("csv/electronique_inventory.csv",
                             "Laptop", 30, 999.99, "Electronique")
        self.create_csv_file("csv/electronique_inventory.csv",
                             "Tablet", 40, 499.99, "Electronique")
        self.create_csv_file("csv/electronique_inventory.csv",
                             "Smartwatch", 25, 199.99, "Electronique")
        self.create_csv_file("csv/electronique_inventory.csv",
                             "Camera", 15, 599.99, "Electronique")

        # Vetements
        self.create_csv_file("csv/vetements_inventory.csv",
                             "T-shirt", 100, 19.99, "Vetements")
        self.create_csv_file("csv/vetements_inventory.csv",
                             "Jeans", 60, 49.99, "Vetements")
        self.create_csv_file("csv/vetements_inventory.csv",
                             "Jacket", 25, 89.99, "Vetements")
        self.create_csv_file("csv/vetements_inventory.csv",
                             "Sweater", 40, 29.99, "Vetements")
        self.create_csv_file("csv/vetements_inventory.csv",
                             "Shoes", 80, 79.99, "Vetements")

        # Voiture
        self.create_csv_file("csv/voiture_inventory.csv",
                             "Toyota Corolla", 10, 20000, "Voiture")
        self.create_csv_file("csv/voiture_inventory.csv",
                             "Tesla Model 3", 5, 35000, "Voiture")
        self.create_csv_file("csv/voiture_inventory.csv",
                             "Honda Civic", 12, 22000, "Voiture")
        self.create_csv_file("csv/voiture_inventory.csv",
                             "Ford Mustang", 8, 45000, "Voiture")
        self.create_csv_file("csv/voiture_inventory.csv",
                             "BMW 3 Series", 7, 41000, "Voiture")

        # Avion
        self.create_csv_file("csv/avion_inventory.csv",
                             "Cessna 172", 2, 300000, "Avion")
        self.create_csv_file("csv/avion_inventory.csv",
                             "Boeing 737", 1, 100000000, "Avion")
        self.create_csv_file("csv/avion_inventory.csv",
                             "Airbus A320", 1, 98000000, "Avion")
        self.create_csv_file("csv/avion_inventory.csv",
                             "Piper PA-28", 3, 350000, "Avion")
        self.create_csv_file("csv/avion_inventory.csv",
                             "Gulfstream G550", 1, 62000000, "Avion")


if __name__ == "__main__":
    # Exemple d'utilisation
    creator = CsvCreator()
    creator.generate_test_csv_files()
