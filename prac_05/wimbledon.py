FILE_NAME = "wimbledon.csv"
INDEX_CHAMPION = 2
INDEX_COUNTRY = 1


def main():
    records = load_data()
    winner_to_count = count_winners(records)
    print_winner_to_count(winner_to_count)
    countries_to_wins = count_winning_countries(records)
    print_winning_countries(countries_to_wins)


def print_winning_countries(countries_to_wins):
    winning_countries = list(countries_to_wins.keys())
    winning_countries.sort()
    print("These 12 countries have won the wimbledon:")
    print(', '.join(country for country in winning_countries))


def count_winning_countries(records):
    countries_to_wins = {}  # name: times_won
    for record in records:
        try:
            countries_to_wins[record[INDEX_COUNTRY]] += 1
        except KeyError:
            countries_to_wins[record[INDEX_COUNTRY]] = 1
    return countries_to_wins


def print_winner_to_count(winner_to_count):
    for winner, count in winner_to_count.items():
        print(f"{winner} {count}")


def count_winners(records):
    winner_to_count = {}  # name: times_won
    for record in records:
        try:
            winner_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            winner_to_count[record[INDEX_CHAMPION]] = 1
    return winner_to_count


# name_to_age[name] = age  # name and age to the dictionary with name being the key


def load_data():
    records = []
    with open(FILE_NAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # removes the header
        for line in in_file:
            year_data = line.strip().split(",")
            records.append(year_data)
    return records


main()
