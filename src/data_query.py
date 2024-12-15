import csv
import os

class CsvManager():
    def __init__(self, input_folder, output_file):
        """
        Initialise la classe CsvManager avec un dossier d'entrée et un fichier de sortie.
        :param input_folder: Dossier contenant les fichiers CSV à fusionner.
        :param output_file: Nom du fichier de sortie contenant les données fusionnées.
        """
        self.input_folder = input_folder
        self.output_file = output_file

    def merge_csv_files(self):
        """
        Regroupe toutes les données des fichiers CSV dans un dossier en un seul fichier CSV.
        """
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)

        # Liste pour conserver les noms des fichiers et traiter l'en-tête
        first_file = True

        with open(self.output_file, mode='w', newline='', encoding='utf-8') as output_csv:
            writer = csv.writer(output_csv)

            for file_name in os.listdir(self.input_folder):
                if file_name.endswith('.csv'):
                    file_path = os.path.join(self.input_folder, file_name)
                    with open(file_path, mode='r', encoding='utf-8') as input_csv:
                        reader = csv.reader(input_csv)
                        headers = next(reader)  # Lire les en-têtes

                        # Écrire les en-têtes uniquement pour le premier fichier
                        if first_file:
                            writer.writerow(headers)
                            first_file = False

                        # Écrire les données du fichier
                        writer.writerows(reader)

        print(f"Données fusionnées dans : {self.output_file}")

    def search_by_category(self, category):
        """
        Recherche les lignes appartenant à une catégorie donnée.
        :param category: Nom de la catégorie à rechercher.
        :return: Liste des lignes correspondantes.
        """
        results = []
        with open(self.output_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if category.lower() in row['Categorie'].lower():
                    results.append(row)
        return results

    def search_by_price_range(self, min_price, max_price):
        """
        Recherche les produits dont le prix est dans une plage donnée.
        :param min_price: Prix minimum.
        :param max_price: Prix maximum.
        :return: Liste des lignes correspondantes.
        """
        results = []
        with open(self.output_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    price = float(row['Prix unitaire'])
                    if min_price <= price <= max_price:
                        results.append(row)
                except ValueError:
                    continue  # Ignorer les lignes avec des valeurs non numériques
        return results

    def sort_by_column(self, column_name, ascending=True):
        """
        Trie les données dans le fichier fusionné par une colonne spécifiée.
        :param column_name: Nom de la colonne à trier.
        :param ascending: Booléen indiquant si le tri est ascendant (True) ou descendant (False).
        :return: Liste des lignes triées.
        """
        with open(self.output_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        try:
            sorted_rows = sorted(rows, key=lambda x: float(x[column_name]), reverse=not ascending)
        except KeyError:
            print(f"Erreur : La colonne '{column_name}' n'existe pas dans le fichier CSV.")
            return []
        except ValueError:
            print(f"Erreur : Certaines valeurs dans la colonne '{column_name}' ne sont pas numériques.")
            return []

        return sorted_rows

if __name__ == "__main__":
    input_folder = "csv"  # Remplacez par le dossier contenant les fichiers CSV
    output_file = "csv_merge/merged_inventory.csv"  # Nom du fichier fusionné

    manager = CsvManager(input_folder, output_file)
    manager.merge_csv_files()

    # Exemple d'utilisation des fonctions
    print("\nRecherche par catégorie :")
    print(manager.search_by_category("Electronique"))

    print("\nRecherche par plage de prix :")
    print(manager.search_by_price_range(50, 300))

    print("\nTri par prix unitaire (ascendant) :")
    sorted_data = manager.sort_by_column("Prix unitaire", ascending=True)
    for row in sorted_data:
        print(row)

    print("\nTri par prix unitaire (descendant) :")
    sorted_data = manager.sort_by_column("Prix unitaire", ascending=False)
    for row in sorted_data:
        print(row)
