import os
import csv
import requests
from bs4 import BeautifulSoup as soup
import time
import random
import email_guesser
import email_verifier
from datetime import date

path = os.getcwd()
print(path)
today = date.today()

char_to_replace = {'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e', 'ē': 'e', 'ė': 'e', 'ę': 'e',
                   'ÿ': 'y',
                   'û': 'u', 'ü': 'ue', 'ù': 'u', 'ú': 'u', 'ū': 'u',
                   'î': 'i', 'ï': 'i', 'í': 'i', 'ī': 'i', 'į': 'i', 'ì': 'i', 'ı': 'i',
                   'ô': 'o', 'ö': 'oe', 'ò': 'o', 'ó': 'o', 'œ': 'oe', 'ø': 'o', 'ō': 'o', 'õ': 'o',
                   'à': 'a', 'á': 'a', 'â': 'a', 'ä': 'ae', 'æ': 'ae', 'ã': 'a', 'å': 'a', 'ā': 'a',
                   'ß': 'ss', 'ś': 's', 'š': 's', 'ł': 's', 'ž': 'z', 'ź': 'z', 'ż': 'z',
                   'ç': 'c', 'ć': 'c', 'č': 'c', 'ñ': 'n', 'ń': 'n', 'ğ': 'g',
                   ',': '', '(': '', ')': '', '|': '', '"': '', "'": '',
                   'ph.d.': '', 'phd': '', 'ph. d.': '', 'ph d': '', 'dr.': '', 'dr ': '',
                   'professor': '', 'prof.': '', 'prof': '',
                   'b.sc.': '', 'm.sc.': '', 'b.sc': '', 'm.phil': '',
                   'bsc ': '', 'msc ': '', ' md': '', ' bsc': '', ' msc': ''}

valid_letters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def sleep():
    sleeptime = (random.randrange(0, 2000)/1000)
    time.sleep(sleeptime)



def get_profile_links(writer, term_writer, term_list, name_list):
    url1 = "https://scholar.google.de/scholar?start="
    terms = ['economics'] #enter search terms here
    for term in terms:
        for i in range(22, 0, -1):
            yhi = str(i)
            ylo = str(i-1)
            if len(yhi) == 1:
                yhi = '0' + yhi
            if len(ylo) == 1:
                ylo = '0' + ylo

            url2 = f'&q={term}&hl=de&as_sdt=0,5&as_ylo=20{ylo}&as_yhi=20{yhi}'
            for i in range(0, 1000, 10):
                page = int(i/10+1)
                print(f"Search Term: {term}, yearhi: {yhi}, yearlo: {ylo}, Page: {page}")
                search_term = [term, yhi, ylo, str(page)]
                if search_term in term_list: # if term is in csv skip execution
                    continue
                if len(str(i%100)) == 1 and i != 0: # sleep 10 minutes every 10 pages
                    time.sleep(600)
                url = (f"{url1}{i}{url2}")
                output = []
                #print(url)
                try:
                    # establish connection
                    response = requests.get(url, timeout=3)
                    page_soup = soup(response.content, "lxml")
                    authors = page_soup.find_all("div", class_="gs_a")

                    # print(authors)
                    for author in authors:
                        profile_links = author.find_all("a")
                        for profile_link in profile_links:
                            output = []
                            profile_link = profile_link.get("href")
                            profile_link = (f"https://scholar.google.de/{profile_link}")
                            response = requests.get(profile_link, timeout=3)
                            page_soup = soup(response.content, "lxml")

                            # get name
                            name = page_soup.find("div", id="gsc_prf_in").get_text().lower()

                            # replace umlauts
                            for key, value in char_to_replace.items():
                                name = name.replace(key, value)
                                name = name.replace(".", '').strip()
                            
                            # replace all other characters
                            for letter in name:
                                if letter not in valid_letters:
                                    name = name.replace(letter, '').strip()

                            # check duplicates
                            if name in name_list:
                                continue
                            name_list.append(name)

                            name_parts = name.split()
                            name = ""
                            for name_part in name_parts:
                                name_part = name_part.strip().capitalize()
                                name = name + name_part + " "
                            name = name.strip()
                            output.append(name)
                            print(name)

                            # uni
                            uni = page_soup.find("div", class_="gsc_prf_il").get_text().replace(";", ",").lower()
                            output.append(uni)
                            # print(uni)

                            # email
                            domain = page_soup.find("div", class_="gsc_prf_il", id="gsc_prf_ivh").get_text().lower()
                            domain = domain.replace("verified email at ", "")
                            domain = domain.replace("bestätigte e-mail-adresse bei ", "")
                            domain = domain.replace(" - homepage", "")
                            domain = domain.replace(" - startseite", "")
                            # print(domain)

                            # verify email
                            emails = email_guesser.guesser(name, domain)
                            email = email_verifier.verify(emails)
                            output.append(email)
                            writer.writerow(output)
                            sleep() #sleep a random time
                
                except Exception as e:
                    print('Exception:', e)
                    continue
                if output != []:
                    term_writer.writerow(search_term) # write search term to csv

def main():
    name_list = []    
    with open(f"{path}/out/emails.csv", "r", encoding="UTF-8-SIG") as email_csv:
        lines = csv.reader(email_csv, delimiter=';')
        for row in lines:
            name = row[0].strip().lower()
            if name not in name_list:
                name_list.append(name)
    
    term_list = []
    with open(f"{path}/out/terms.csv", "r", encoding="UTF-8_SIG") as searched_terms_csv, \
        open(f"{path}/out/terms.csv", "a", encoding="UTF-8_SIG") as new_terms_csv, \
        open(f"{path}/out/emails.csv", "a", encoding="UTF-8-SIG", newline="") as email_csv:
        term_writer = csv.writer(new_terms_csv)

        writer = csv.writer(email_csv, delimiter=';')
        
        lines = csv.reader(searched_terms_csv)
        for row in lines:
            term_list.append(list(row))
        get_profile_links(writer, term_writer, term_list, name_list)
        

if __name__ == "__main__":
    main()