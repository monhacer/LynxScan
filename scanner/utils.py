import csv

def save_to_csv(target, results, filename=None):
    filename = filename or f"{target}_scan_results.csv"
    with open(filename, "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Port", "Status"])
        writer.writerows(results)
