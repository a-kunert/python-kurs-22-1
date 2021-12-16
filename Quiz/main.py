import json
import random
import replit

def get_countries():
    with open("countries.json") as file: 
        countries = json.load(file)
    return countries

def filter_countries(countries):
    countries = [
        country 
        for country in countries
        if country["continent"] in ["Europa","Asien"]
    ]
    return countries

def pick_country(countries, previous_countries):
    countries = [
        country
        for country in countries
        if country not in previous_countries
    ]
    random.shuffle(countries)
    country = countries[0]
    return country


def get_answer_options(countries, country):
    random.shuffle(countries)
    answer_options = [ 
        k["capital"] 
        for k in countries 
        if k["capital"] != country["capital"]
    ]
    answer_options = answer_options[0:3]
    answer_options.append(country["capital"]) 
    random.shuffle(answer_options)
    return answer_options

def display_question(answer_options, country):
    print(f"Was ist die Hauptstadt von { country['name'] }? ")
    for (index,option) in enumerate(answer_options): 
        print(f"({ index + 1 }) { option }")

def get_and_check_answer(answer_options, country):
    given_answer = int(input("Antwort: "))
    given_answer = answer_options[given_answer - 1]
    correct_answer = country["capital"]
    result = 0
    if given_answer == correct_answer: 
        result = 1
        print("Korrekt")
    else: 
        print("Das ist leider nicht richtig")

    input("\nDrücke Enter zum Weiterspielen")
    replit.clear()
    return result


countries = get_countries()
countries = filter_countries(countries)
previous_countries = []

score = 0
length = 7


for k in range(1, length + 1):
    active_country = pick_country(countries, previous_countries)
    previous_countries.append(active_country)
    answer_options = get_answer_options(countries, active_country)
    display_question(answer_options, active_country)
    score += get_and_check_answer(answer_options, active_country)

print(f"Du hattest {score} von {length} Fragen richtig beantwortet")

