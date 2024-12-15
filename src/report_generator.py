import csv
import os

def generate_report(manager, filter_type=None, filter_value=None, report_name=None):
    """
    Génère un rapport récapitulatif des données consolidées ou filtrées.
    :param manager: Instance de CsvManager pour accéder aux données.
    :param filter_type: Type de filtre ('category', 'price_range', None pour tous les résultats).
    :param filter_value: Valeur pour le filtre (ex : nom de catégorie ou plage de prix).
    :param report_name: Nom du fichier de sortie. Si None, le programme demande un nom.
    """
    # Obtenir les données en fonction du filtre
    if filter_type == 'category':
        data = manager.search_by_category(filter_value)
    elif filter_type == 'price_range':
        min_price, max_price = filter_value
        data = manager.search_by_price_range(min_price, max_price)
    elif filter_type == 'search_results':
        data = filter_value
    elif filter_type == 'sorted_data':
        data = filter_value
    else:
        with open(manager.output_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=',')
            data = [row for row in reader]

    if not data:
        print("Aucune donnée correspondante trouvée pour le filtre spécifié.")
        return

    # Calcul des métriques
    total_products = len(data)
    total_quantity = sum(int(row['Quantite']) for row in data)
    total_value = sum(float(row['Prix unitaire']) * int(row['Quantite']) for row in data)

    # Générer le contenu du rapport
    report_content = (
        f"Rapport Récapitulatif:\n"
        f"====================\n"
        f"Total des produits : {total_products}\n"
        f"Quantité totale : {total_quantity}\n"
        f"Valeur totale des stocks : {total_value:.2f} EUR\n"
    )

    # Demander le dossier de sortie
    report_folder = "rapports"
    os.makedirs(report_folder, exist_ok=True)

    # Demander le nom du fichier si non fourni
    if not report_name:
        report_name = input("Entrez le nom du fichier de rapport (avec extension, ex: rapport.txt ou rapport.csv) : ").strip()
    report_path = os.path.join(report_folder, report_name)

    # Demander le format de sortie
    output_format = os.path.splitext(report_name)[-1].lower()[1:]

    if output_format == 'txt':
        with open(report_path, mode='w', encoding='utf-8') as txt_file:
            txt_file.write(report_content)
        print(f"Rapport généré dans le fichier : {report_path}")

    elif output_format == 'csv':
        with open(report_path, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(["Total des produits", "Quantite totale", "Valeur totale des stocks (EUR)"])
            writer.writerow([total_products, total_quantity, f"{total_value:.2f}"])
        print(f"Rapport généré dans le fichier : {report_path}")

    else:
        print("Extension de fichier non reconnue. Veuillez utiliser .txt ou .csv.")
