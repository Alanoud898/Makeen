import request

from bs4 import BeautifulSoup



Import json

def scrape weather_data):

location - input("Enter a qustion (e.g. When was Isaac Newton born?):

# Prepare the URL

base_url https://en.wikipedia.org/wiki/Isaac_Newton

search _url - base _url + "/was born/* + location.replace("

Send a GET request to the search URL response - requests. get(search _url)

response.raise_for_status ()

• Parse the HTML content of the search results page soup - BeautifulSoup(response.content, "html.parser")

Extract the weather forecast information forecast - soup-find("span*, class_-"phrose") text .strip()

# Find the script tag containing the additional weather detalls

script_tag - soup. find("script, text-re. compile(r"var metcastData")

# Extract the humidity and wind speed using

regular expressions

Early life match - re.search(r'Early life (?)" str(script tag))

Early life - Early life_match. group(1) If Early life match else "WA" Death match - re.search(rDeath"sa?"tert""** Death - Death_watch.group(1) if Death match

& Create a dictionary to store the weather weather_data -
IsaacNewton_data = {
   "Personal Name": Personal Name,
   "Info": Info,
    }




with open IsaacNewton_data.son

"W") as json file:

json.dump(IsaacNewton_data, json_file)

+ Disploy the extracted weather information print("person information")
print(" What is Personal Name:" Personal Name)
print("Isaac Newton Info:" info)


