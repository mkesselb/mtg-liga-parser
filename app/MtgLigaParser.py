import json
import os

from app.CsvWriter import write_data
from app.DataAggregator import aggregate_data
from app.PdfParser import parse_pdf


if __name__ == "__main__":
    with open(r'F:\git\mtg\mtg-liga-parser\config.json') as configfile:
      config = json.load(configfile)

    pdf_folder = "pdfs"
    if "pdf_folder" in config:
        pdf_folder = config["pdf_folder"]

    aggregated_file = "ligadata.csv"
    if "aggregated_file" in config:
        aggregated_file = config["aggregated_file"]

    csv_delimiter = ";"
    if "csv_delimiter" in config:
        csv_delimiter = config["csv_delimiter"]

    pdfFiles = [f for f in os.listdir(pdf_folder) if os.path.isfile(os.path.join(pdf_folder, f))]
    print("found pdf files: ", pdfFiles)

    all_data = {}
    for pdf in pdfFiles:
        date, player_data = parse_pdf(os.path.join(pdf_folder, pdf))
        all_data[date] = player_data

    aggregated_data = aggregate_data(all_data)
    print("sorted data: ", aggregated_data)

    header = ["Name", "Punkte", "OMW%", "GW%", "OGW%", "Events"]
    for event_date in all_data.keys():
        header.append(event_date)
    write_data(aggregated_data, aggregated_file, header, csv_delimiter)

    print("writing done in: ", aggregated_file)
