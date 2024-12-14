import csv
import os
class Csv_manager():
    def create_csv_file(self,file_name, headers, **data_columns):
        """
        Crée un fichier CSV avec le nom, les en-têtes et les données fournis colonne par colonne.
        :param file_name: Nom du fichier à créer.
        :param headers: Liste des en-têtes pour les colonnes.
        :param data_columns: Données à insérer, chaque colonne étant passée comme un argument clé-valeur.
        """
        os.makedirs("test_data", exist_ok=True)
        file_path = os.path.join("test_data", file_name)

        # Transposer les données pour les écrire ligne par ligne
        rows = list(zip(*data_columns.values()))

        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')  # Utilisation du point-virgule comme délimiteur
            writer.writerow(headers)
            writer.writerows(rows)

        print(f"Fichier créé : {file_path}")

    # Générer des fichiers de test
    def generate_test_csv_files(self):
        """
        Génère plusieurs fichiers CSV contenant des données d'inventaire fictives.
        """
        self.create_csv_file(
            "electronique_inventory.csv",
            ["Nom du produit", "Quantite", "Prix unitaire (EUR)", "Categorie"],
            **{
                "Nom du produit": ["Produit-ELEC-1", "Produit-ELEC-2", "Produit-ELEC-3"],
                "Quantite": [20, 15, 50],
                "Prix unitaire (EUR)": [299.99, 399.99, 99.99],
                "Categorie": ["Electronique", "Electronique", "Electronique"]
            }
        )

        self.create_csv_file(
            "vetements_inventory.csv",
            ["Nom du produit", "Quantité", "Prix unitaire (EUR)", "Catégorie"],
            **{
                "Nom du produit": ["Produit-VET-1", "Produit-VET-2", "Produit-VET-3"],
                "Quantite": [10, 25, 30],
                "Prix unitaire (EUR)": [49.99, 79.99, 29.99],
                "Categorie": ["Vetements", "Vetements", "Vetements"]
            }
        )

    
if __name__ == "__main__":
    csv_manager = Csv_manager()
    csv_manager.generate_test_csv_files()
