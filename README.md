## Google Scholar Scrape
A Python script that scrapes Google Scholar profiles for name and domain, guesses how they could be combined in an email-address and verifies whether these addresses exists using the isitaralemail API. 

# Features 
- Navigates the first 100 results pages for a given search term (scholar does not show 100+ pages)
- Looks for links to authors' profiles
- Scrapes name and domain from profile page (see picture below)
- Automatically removes non-Latin and non-English (ä, ü, ö, ...) characters from the name 
- Depending on the number of names of a person combines them into email-'guesses'
- Sends these guesses to isitaralemail API 
- Writes verified Emails to a .csv
- Automatically sleeps to not trip Bot detection
- Saves already found names, searched for terms in pages in .csv files to allow restarting the script and to not double verify Emails

# Scholar profile page

<img width="1127" alt="scholar profile" src="https://user-images.githubusercontent.com/78418209/182850079-2d914f25-d058-4679-9969-dec037904392.png">
