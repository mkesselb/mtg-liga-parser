import json
import os

from app.CsvWriter import write_data
from app.DataAggregator import aggregate_data
from app.PdfParser import parse_pdf

with open(r'F:\git\mtg\mtg-liga-parser\config.json') as configfile:
  config = json.load(configfile)

pdf_folder = "pdfs"
if "pdf_folder" in config:
    pdf_folder = config["pdf_folder"]

aggregated_file = "ligadata.csv"
if "aggregated_file" in config:
    aggregated_file = config["aggregated_file"]

pdfFiles = [f for f in os.listdir(pdf_folder) if os.path.isfile(os.path.join(pdf_folder, f))]
print("found pdf files: ", pdfFiles)

all_data = {}
for pdf in pdfFiles:
    date, player_data = parse_pdf(os.path.join(pdf_folder, pdf))
    all_data[date] = player_data

aggregated_data = aggregate_data(all_data)
sorted_data = sorted(aggregated_data.items(), key=lambda dict_tuple: dict_tuple[1]["Punkte"], reverse=True)
print("sorted data : ", sorted_data)

# import all pdfs from a pdfs resource folder
# aggregate the whole data
# TODO: then save out a .csv file for easy excel opening
write_data(sorted_data, aggregated_file)
