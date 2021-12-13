from bs4 import BeautifulSoup
import html2text
import requests
import sys

# Process arguments

if (len(sys.argv) != 4):
	print("Usage: main.py [year] [day number] [session ID]")
	exit()

year_number = sys.argv[1]
day_number = sys.argv[2]
session_id = sys.argv[3]

# Get and process the webpage

raw_page_data = requests.get(
	f"https://adventofcode.com/{year_number}/day/{day_number}",
	headers = {
		"cookie": f"session={session_id}"
	}
).text
page_soup = BeautifulSoup(raw_page_data, "html.parser")
articles = page_soup.findAll("article")

# Get the input

raw_input = requests.get(
	f"https://adventofcode.com/{year_number}/day/{day_number}/input",
	headers = {
		"cookie": f"session={session_id}"
	}
).text.removesuffix("\n", ) # Requests gives an extra new line, so I'll just manually remove it (for now)

# Save the input file

input_file = open("./input.txt", "w")
input_file.write(raw_input)

# Write the webpage to Markdown

h = html2text.HTML2Text()
h.body_width = 0

if (len(articles) == 0):
	print("No articles were found. This day has likely not been unlocked yet.")

elif (len(articles) == 1):
	article_one_file = open("./instructions-one.md", "w")
	article_one_file.write(
		h.handle(str(articles[0])).lstrip("\n").rstrip("\n")
	)

else:
	article_one_file = open("./instructions-one.md", "w")
	article_one_file.write(
		h.handle(str(articles[0])).lstrip("\n").rstrip("\n")
	)

	article_two_file = open("./instructions-two.md", "w")
	article_two_file.write(
		h.handle(str(articles[1])).lstrip("\n").rstrip("\n")
	)
