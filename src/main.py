import csv
from data_query import *
from report_generator import *
from data_loader import *
import os

def main():
    input_folder = "csv"  # Chemin vers le dossier contenant les fichiers CSV
    output_file = "csv_merge/merged_inventory.csv"  # Chemin du fichier fusionné

    manager = CsvManager(input_folder, output_file)
    # Fusionner les fichiers CSV dès le démarrage
    manager.merge_csv_files()
    print(f"Les fichiers du dossier '{input_folder}' ont été fusionnés dans '{output_file}'.")

    while True:
        print("\n===== Menu Principal =====")
        print("1. Rechercher des données")
        print("2. Trier les données")
        print("3. Générer un rapport global")
        print("4. Quitter")

        choix = input("Choisissez une option : ").strip()

        if choix == "1":
            print("\n===== Sous-menu Recherche =====")
            print("1. Rechercher par catégorie")
            print("2. Rechercher par plage de prix")
            sub_choix = input("Choisissez une option : ").strip()

            results = []
            if sub_choix == "1":
                category = input("Entrez le nom de la catégorie à rechercher : ").strip()
                results = manager.search_by_category(category)
                if results:
                    print("\nRésultats :")
                    for row in results:
                        print(row)
                else:
                    print("Aucun produit trouvé pour cette catégorie.")

            elif sub_choix == "2":
                try:
                    min_price = float(input("Entrez le prix minimum : ").strip())
                    max_price = float(input("Entrez le prix maximum : ").strip())
                    results = manager.search_by_price_range(min_price, max_price)
                    if results:
                        print("\nRésultats :")
                        for row in results:
                            print(row)
                    else:
                        print("Aucun produit trouvé dans cette plage de prix.")
                except ValueError:
                    print("Veuillez entrer des valeurs numériques valides pour le prix.")

            else:
                print("Choix invalide dans le sous-menu Recherche. Veuillez réessayer.")

            if results:
                generate = input("Souhaitez-vous générer un rapport pour ces résultats ? (oui/non) : ").strip().lower()
                if generate == "oui":
                    report_name = input("Entrez le nom du fichier de rapport (avec extension, ex: rapport.txt ou rapport.csv) : ").strip()
                    generate_report(manager, filter_type="search_results", filter_value=results, report_name=report_name)

        elif choix == "2":
            print("\n===== Tri des données =====")
            column_name = input("Entrez le nom de la colonne à trier (ex: Prix unitaire, Quantite) : ").strip()
            order = input("Ordre de tri (ascendant/descendant) : ").strip().lower()
            ascending = order == "ascendant"

            sorted_data = manager.sort_by_column(column_name, ascending=ascending)
            if sorted_data:
                print("\nDonnées triées :")
                for row in sorted_data:
                    print(row)

                save_sorted = input("Souhaitez-vous sauvegarder ces données triées dans un fichier CSV ? (oui/non) : ").strip().lower()
                if save_sorted == "oui":
                    csv_sort_folder = "csv_sort"
                    os.makedirs(csv_sort_folder, exist_ok=True)
                    sorted_file_name = input("Entrez le nom du fichier trié (avec extension, ex: sorted_data.csv) : ").strip()
                    sorted_file_path = os.path.join(csv_sort_folder, sorted_file_name)

                    with open(sorted_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
                        writer = csv.DictWriter(csv_file, fieldnames=sorted_data[0].keys())
                        writer.writeheader()
                        writer.writerows(sorted_data)

                    print(f"Fichier trié enregistré dans : {sorted_file_path}")
            else:
                print("Aucune donnée triée disponible.")

        elif choix == "3":
            print("\n===== Génération de rapport global =====")
            report_name = input("Entrez le nom du fichier de rapport global (avec extension, ex: rapport_global.txt ou rapport_global.csv) : ").strip()
            generate_report(manager, report_name=report_name)

        elif choix == "4":
            print("Programme terminé.")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
import csv
from data_query import CsvManager
import os

def main():
    input_folder = "csv"  # Chemin vers le dossier contenant les fichiers CSV
    output_file = "csv_merge/merged_inventory.csv"  # Chemin du fichier fusionné

    manager = CsvManager(input_folder, output_file)
    # Fusionner les fichiers CSV dès le démarrage
    manager.merge_csv_files()
    print(f"Les fichiers du dossier '{input_folder}' ont été fusionnés dans '{output_file}'.")

    while True:
        print("\n===== Menu Principal =====")
        print("1. Rechercher des données")
        print("2. Trier les données")
        print("3. Générer un rapport global")
        print("4. Quitter")

        choix = input("Choisissez une option : ").strip()

        if choix == "1":
            print("\n===== Sous-menu Recherche =====")
            print("1. Rechercher par catégorie")
            print("2. Rechercher par plage de prix")
            sub_choix = input("Choisissez une option : ").strip()

            results = []
            if sub_choix == "1":
                category = input("Entrez le nom de la catégorie à rechercher : ").strip()
                results = manager.search_by_category(category)
                if results:
                    print("\nRésultats :")
                    for row in results:
                        print(row)
                else:
                    print("Aucun produit trouvé pour cette catégorie.")

            elif sub_choix == "2":
                try:
                    min_price = float(input("Entrez le prix minimum : ").strip())
                    max_price = float(input("Entrez le prix maximum : ").strip())
                    results = manager.search_by_price_range(min_price, max_price)
                    if results:
                        print("\nRésultats :")
                        for row in results:
                            print(row)
                    else:
                        print("Aucun produit trouvé dans cette plage de prix.")
                except ValueError:
                    print("Veuillez entrer des valeurs numériques valides pour le prix.")

            else:
                print("Choix invalide dans le sous-menu Recherche. Veuillez réessayer.")

            if results:
                generate = input("Souhaitez-vous générer un rapport pour ces résultats ? (oui/non) : ").strip().lower()
                if generate == "oui":
                    report_name = input("Entrez le nom du fichier de rapport (avec extension, ex: rapport.txt ou rapport.csv) : ").strip()
                    generate_report(manager, filter_type="search_results", filter_value=results, report_name=report_name)

        elif choix == "2":
            print("\n===== Tri des données =====")
            column_name = input("Entrez le nom de la colonne à trier (ex: Prix unitaire, Quantite) : ").strip()
            order = input("Ordre de tri (ascendant/descendant) : ").strip().lower()
            ascending = order == "ascendant"

            sorted_data = manager.sort_by_column(column_name, ascending=ascending)
            if sorted_data:
                print("\nDonnées triées :")
                for row in sorted_data:
                    print(row)

                save_sorted = input("Souhaitez-vous sauvegarder ces données triées dans un fichier CSV ? (oui/non) : ").strip().lower()
                if save_sorted == "oui":
                    csv_sort_folder = "csv_sort"
                    os.makedirs(csv_sort_folder, exist_ok=True)
                    sorted_file_name = input("Entrez le nom du fichier trié (avec extension, ex: sorted_data.csv) : ").strip()
                    sorted_file_path = os.path.join(csv_sort_folder, sorted_file_name)

                    with open(sorted_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
                        writer = csv.DictWriter(csv_file, fieldnames=sorted_data[0].keys())
                        writer.writeheader()
                        writer.writerows(sorted_data)

                    print(f"Fichier trié enregistré dans : {sorted_file_path}")
            else:
                print("Aucune donnée triée disponible.")

        elif choix == "3":
            print("\n===== Génération de rapport global =====")
            report_name = input("Entrez le nom du fichier de rapport global (avec extension, ex: rapport_global.txt ou rapport_global.csv) : ").strip()
            generate_report(manager, report_name=report_name)

        elif choix == "4":
            print("Programme terminé.")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
