"""
projekt_3.py: treti projekt do Engeto Online Python Akademie - Election Scrapper

author: Lizal Adam
email: lizaladam@seznam.cz
discord: Adam_L



"""


import sys
import csv
from bs4 import BeautifulSoup
import requests


def get_response(link):
    """Get response from the link and return the page content"""

    content = requests.get(link)

    if content.status_code == 200:
        html = BeautifulSoup(content.text, "html.parser")
        print(f"Downloading the data from {link}")

        return html

    else:
        print(f"Failed to retrieve the page. Status code: {content.status_code}")


def get_id_code(html) -> list:
    """Find all the id codes for all cities and save them to the new list"""

    id_html = html.select("td.cislo")
    town_id = [_id.text for _id in id_html]

    return town_id


def get_town_name(html) -> list:
    """Find all the names of all cities and save them to the new list"""
    town_html = html.select("td.overflow_name")
    town_name = [name.text for name in town_html]

    return town_name


def get_district_links(html) -> list:
    """Save all links for each disctrict to the new list"""

    link_html = html.select("td.cislo a")
    baseurl = "https://volby.cz/pls/ps2017nss/"
    links = [baseurl + link["href"] for link in link_html]

    return links


def get_name_parties(links) -> list:
    """Collect and save all names of candidating parties to the new list"""

    html = get_response(links[0])
    party_html = html.select("td.overflow_name")

    parties = [name.text for name in party_html]

    return parties


def get_parties_votes(links) -> list:
    """Collect and save legitimit votes for each candidating party in every district"""

    votes = []
    for link in links:
        html = get_response(link)
        votes_html = html.select(
            "td[headers = 't1sa2 t1sb3'], td[headers = 't2sa2 t2sb3']"
        )
        one = [num.text.replace("\xa0", " ") for num in votes_html]
        votes.append(one)

    return votes


# return [for link in links
# [ num.text.replace.("\xa0", " ") for num in get_response(link).select("td[headers = 't1sa2 t1sb3']")]
# ]


def get_votes_and_envelopes(links) -> list:
    """"""

    zipped_votes = []

    for link in links:
        html = get_response(link)
        regis = html.select("td[headers='sa2']")
        envelop = html.select("td[headers='sa3']")
        vali = html.select("td[headers='sa6']")

        zipped_votes.append(
            (
                reg.text.replace("\xa0", " "),
                val.text.replace("\xa0", " "),
                env.text.replace("\xa0", " "),
            )
            for reg, env, val in zip(regis, envelop, vali)
        )

    return zipped_votes


def create_csv(header, file, content):
    """Create CSV file with a given header and content"""

    try:
        with open(file, "w", newline="") as f:
            f_writer = csv.writer(f)
            f_writer.writerow(header)
            f_writer.writerows(content)
        print("Data saved into the file:", file)
    except Exception as e:
        print("Error occured while saving data:", e)


def election_scrapper(link, file):
    try:
        html = get_response(link)
        id_code = get_id_code(html)
        town_name = get_town_name(html)
        links = get_district_links(html)
        parties_name = get_name_parties(links)
        parties_votes = get_parties_votes(links)
        votes_envelopes = get_votes_and_envelopes(links)

        header = [
            "Kód obce",
            "Název obce",
            "Voliči v seznamu",
            "Vydané obálky",
            "Platné hlasy",
        ] + parties_name

        content = []

        for i in range(len(town_name)):
            row = [id_code[i], town_name[i]]
            row.extend(next(votes_envelopes[i]))
            row.extend(parties_votes[i])
            content.append(row)

        create_csv(header, file, content)
        print("Process completed: ", sys.argv[0])
    except Exception as e:
        print("Error occured: ", e)
        quit()


if __name__ == "__main__":
    arguments = sys.argv[0:]

    if len(sys.argv) != 3:
        print(f"ERROR: 3 arguments expected, {len(arguments)} was given!")
        print(" Right example: python name.py arg2('https://....') arg3('name.csv')")
        sys.exit()

    url = sys.argv[1]
    file_name = sys.argv[2]
    election_scrapper(url, file_name)
