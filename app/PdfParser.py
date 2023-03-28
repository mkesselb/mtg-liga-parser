from pypdf import PdfReader
import re


def parse_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    event_date = "none"
    player_data = []
    parsing = False

    for line in text.split("\n"):
        if parsing and re.search("^\d+", line) is not None:
            # here we remove pdf whitespaces so that splitting can work fine
            print(line)
            line_replaced = line.replace(u"\u00A0", "\t")
            lineparts = re.split("\t+", line_replaced)
            player_data.append({"Rang": int(lineparts[0].strip()),
                                "Name": lineparts[1].strip(),
                                "Punkte": int(lineparts[2].strip()),
                                "OMW%": int(lineparts[3].strip()),
                                "GW%": int(lineparts[4].strip()),
                                "OGW%": int(lineparts[5].strip()),
                                })

        if line.startswith("------"):
            print("start parsing")
            parsing = True
        if line.startswith("Event-Dat"):
            lineparts = re.split("\s", line)
            event_date = lineparts[-1]

    print(player_data)

    return event_date, player_data

