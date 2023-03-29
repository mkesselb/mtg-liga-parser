import csv


def write_data(aggregated_data, file, header, delimiter):
    with open(file, "w", encoding="UTF8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header, delimiter=delimiter)
        writer.writeheader()
        writer.writerows(aggregated_data)

    return
