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
            aggregated_data[name_lower]["GW%"] += pdata["GW%"]
            aggregated_data[name_lower]["OGW%"] += pdata["OGW%"]

    return aggregated_data

