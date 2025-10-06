import re
import csv


def parse_title(title):
    match = re.search(r'\((\d{4})\)\s*$', title.strip())
    if match:
        year = int(match.group(1))
        clean_title = title[:match.start()].strip()
        clean_title = clean_title.rstrip()
        return clean_title, year
    else:
        return title.strip(), None

def escape_sql(s):
    return s.replace("'", "''")

def main():

    with open('db_init.sql', 'w', encoding='utf-8') as f:
        f.write("DROP TABLE IF EXISTS ratings;\n")
        f.write("DROP TABLE IF EXISTS tags;\n")
        f.write("DROP TABLE IF EXISTS movies;\n")
        f.write("DROP TABLE IF EXISTS users;\n\n")


        f.write("""CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    gender TEXT,
    register_date TEXT,
    occupation TEXT
);\n\n""")

        f.write("""CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    year INTEGER,
    genres TEXT
);\n\n""")

        f.write("""CREATE TABLE ratings (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    movie_id INTEGER,
    rating REAL,
    timestamp INTEGER
);\n\n""")

        f.write("""CREATE TABLE tags (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    movie_id INTEGER,
    tag TEXT,
    timestamp INTEGER
);\n\n""")



        with open('users.txt', 'r', encoding='utf-8') as users_file:
            for line in users_file:
                parts = line.strip().split('|')
                if len(parts) != 6:
                    continue
                uid, name, email, gender, reg_date, occ = parts
                f.write(f"INSERT INTO users (id, name, email, gender, register_date, occupation) "
                        f"VALUES ({uid}, '{escape_sql(name)}', '{email}', '{gender}', '{reg_date}', '{escape_sql(occ)}');\n")
        f.write('\n')

        with open('movies.csv', 'r', encoding='utf-8') as movies_file:
            reader = csv.reader(movies_file)
            header = next(reader, None)  # Skip header
            for row in reader:
                if not row:
                    continue
                if len(row) < 3:
                    continue
                movie_id = row[0]
                title = row[1]
                genres_str = row[2]

                title_clean, year = parse_title(title)
                if genres_str == "(no genres listed)":
                    genres_str = ""

                year_sql = str(year) if year is not None else "NULL"
                f.write(f"INSERT INTO movies (id, title, year, genres) "
                        f"VALUES ({movie_id}, '{escape_sql(title_clean)}', {year_sql}, '{escape_sql(genres_str)}');\n")
        f.write('\n')

        rating_id = 1
        with open('ratings.csv', 'r', encoding='utf-8') as ratings_file:
                reader = csv.reader(ratings_file)
                header = next(reader, None)
                for row in reader:
                    if len(row) < 4:
                        continue
                    user_id, movie_id, rating, timestamp = row[:4]
                    f.write(f"INSERT INTO ratings (id, user_id, movie_id, rating, timestamp) "
                            f"VALUES ({rating_id}, {user_id}, {movie_id}, {rating}, {timestamp});\n")
                    rating_id += 1
        f.write('\n')

        tag_id = 1
        with open('tags.csv', 'r', encoding='utf-8') as tags_file:
                reader = csv.reader(tags_file)
                for row in reader:
                    if len(row) < 4:
                        continue
                    if row[0].startswith('!'):
                        continue
                    try:
                        user_id = int(row[0])
                        movie_id = int(row[1])
                        tag = row[2]
                        timestamp = int(row[3])
                    except (ValueError, IndexError):
                        continue
                    f.write(f"INSERT INTO tags (id, user_id, movie_id, tag, timestamp) "
                            f"VALUES ({tag_id}, {user_id}, {movie_id}, '{escape_sql(tag)}', {timestamp});\n")
                    tag_id += 1

if __name__ == '__main__':
    main()