from app.PdfParser import parse_pdf

from typing import Any


def aggregate_data(event_player_data: dict[str, Any]):
    aggregated_data = {}

    for event in event_player_data.keys():
        player_data = event_player_data[event]
        for pdata in player_data:
            name_lower = pdata["Name"].lower()
            if name_lower not in aggregated_data.keys():
                aggregated_data[name_lower] = {"Name": pdata["Name"],
                                               "Punkte": 0,
                                               "OMW%": 0,
                                               "GW%": 0,
                                               "OGW%": 0}
            aggregated_data[name_lower]["Punkte"] += pdata["Punkte"]
            aggregated_data[name_lower]["OMW%"] += pdata["OMW%"]
            aggregated_data[name_lower]["OMW%"] += pdata["OMW%"]
            aggregated_data[name_lower]["OMW%"] += pdata["OMW%"]

    return aggregated_data


# TODO: import all pdfs from a pdfs resource folder
# aggregate the whole data
# then save out a .csv file for easy excel opening

# TODO: (optional) read in config from a .json file (name of pdf folder, name of result .csv file, .csv separator)

date, player_data = parse_pdf(r"F:\git\mtg\mtg-liga-parser\resources\16032023.pdf")
aggregated_data = aggregate_data({date: player_data})

sorted_ad = sorted(aggregated_data.items(), key=lambda dict_tuple: dict_tuple[1]["Punkte"], reverse=True)
print(sorted_ad)
