import csv
import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "geo.db"
COUNTRY_INFO_PATH = BASE_DIR / "country_info.txt"
ADMIN1_PATH = BASE_DIR / "admin1.txt"
CITIES_PATH = BASE_DIR / "cities15000.txt"


CONTINENTS = {
    "AF": "Africa",
    "AN": "Antarctica",
    "AS": "Asia",
    "EU": "Europe",
    "NA": "North America",
    "OC": "Oceania",
    "SA": "South America",
}


GAME_REGIONS = [
    (1, "Japan", "Very Competitive", 5),
    (2, "NA East", "Competitive", 4),
    (3, "China", "Competitive", 4),
    (4, "UK/Ireland", "Hard", 4),
    (5, "South Korea", "Hard", 4),
    (6, "EU West", "Moderate", 3),
    (7, "NA West", "Moderate", 3),
    (8, "NA Midwest", "Moderate", 3),
    (9, "South America", "Moderate", 3),
    (10, "Europe North/East", "Light", 2),
    (11, "Mexico", "Light", 2),
    (12, "Middle East", "Light", 2),
    (13, "Asia Southeast", "Obscure", 1),
    (14, "Asia South", "Obscure", 1),
    (15, "Central America", "Obscure", 1),
    (16, "Africa", "Obscure", 1),
    (17, "Oceania", "Obscure", 1),
]


COUNTRY_GAME_REGIONS = {
    "JP": 1,
    "US": 2,
    "CA": 2,
    "CN": 3,
    "HK": 3,
    "MO": 3,
    "TW": 3,
    "GB": 4,
    "IE": 4,
    "KR": 5,
    "AD": 6,
    "AT": 6,
    "BE": 6,
    "CH": 6,
    "DE": 6,
    "ES": 6,
    "FR": 6,
    "IT": 6,
    "LI": 6,
    "LU": 6,
    "MC": 6,
    "NL": 6,
    "PT": 6,
    "SM": 6,
    "VA": 6,
    "AR": 9,
    "BO": 9,
    "BR": 9,
    "CL": 9,
    "CO": 9,
    "EC": 9,
    "FK": 9,
    "GF": 9,
    "GY": 9,
    "PE": 9,
    "PY": 9,
    "SR": 9,
    "UY": 9,
    "VE": 9,
    "AL": 10,
    "BA": 10,
    "BG": 10,
    "BY": 10,
    "CZ": 10,
    "DK": 10,
    "EE": 10,
    "FI": 10,
    "GR": 10,
    "HR": 10,
    "HU": 10,
    "IS": 10,
    "LT": 10,
    "LV": 10,
    "MD": 10,
    "ME": 10,
    "MK": 10,
    "NO": 10,
    "PL": 10,
    "RO": 10,
    "RS": 10,
    "RU": 10,
    "SE": 10,
    "SI": 10,
    "SK": 10,
    "UA": 10,
    "XK": 10,
    "MX": 11,
    "AE": 12,
    "BH": 12,
    "CY": 12,
    "IL": 12,
    "IQ": 12,
    "IR": 12,
    "JO": 12,
    "KW": 12,
    "LB": 12,
    "OM": 12,
    "PS": 12,
    "QA": 12,
    "SA": 12,
    "SY": 12,
    "TR": 12,
    "YE": 12,
    "BN": 13,
    "ID": 13,
    "KH": 13,
    "LA": 13,
    "MM": 13,
    "MY": 13,
    "PH": 13,
    "SG": 13,
    "TH": 13,
    "TL": 13,
    "VN": 13,
    "AF": 14,
    "BD": 14,
    "BT": 14,
    "IN": 14,
    "LK": 14,
    "MV": 14,
    "NP": 14,
    "PK": 14,
    "AG": 15,
    "AI": 15,
    "AW": 15,
    "BB": 15,
    "BL": 15,
    "BM": 15,
    "BQ": 15,
    "BS": 15,
    "BZ": 15,
    "CR": 15,
    "CU": 15,
    "CW": 15,
    "DM": 15,
    "DO": 15,
    "GD": 15,
    "GL": 15,
    "GP": 15,
    "GT": 15,
    "HN": 15,
    "HT": 15,
    "JM": 15,
    "KN": 15,
    "KY": 15,
    "LC": 15,
    "MF": 15,
    "MQ": 15,
    "MS": 15,
    "NI": 15,
    "PA": 15,
    "PM": 15,
    "PR": 15,
    "SV": 15,
    "SX": 15,
    "TC": 15,
    "TT": 15,
    "VC": 15,
    "VG": 15,
    "VI": 15,
}


CONTINENT_GAME_REGION_DEFAULTS = {
    "AF": 16,
    "OC": 17,
}


# These countries belong to compact game regions where asking for a
# state/province/prefecture is useful but does not change the game region.
ADMIN1_COUNTRY_GAME_REGION_DEFAULTS = {
    "JP": 1,
    "CN": 3,
    "HK": 3,
    "MO": 3,
    "TW": 3,
    "GB": 4,
    "IE": 4,
    "KR": 5,
    "MX": 11,
}


ADMIN1_SELECTION_COUNTRIES = {
    "AU",
    "CA",
    "CN",
    "GB",
    "IE",
    "JP",
    "KR",
    "MX",
    "US",
}


ADMIN1_GAME_REGIONS = {
    "US.CT": 2,
    "US.DC": 2,
    "US.DE": 2,
    "US.FL": 2,
    "US.GA": 2,
    "US.MA": 2,
    "US.MD": 2,
    "US.ME": 2,
    "US.NC": 2,
    "US.NH": 2,
    "US.NJ": 2,
    "US.NY": 2,
    "US.PA": 2,
    "US.RI": 2,
    "US.SC": 2,
    "US.VA": 2,
    "US.VT": 2,
    "US.WV": 2,
    "US.AK": 7,
    "US.AZ": 7,
    "US.CA": 7,
    "US.CO": 7,
    "US.HI": 7,
    "US.ID": 7,
    "US.MT": 7,
    "US.NM": 7,
    "US.NV": 7,
    "US.OR": 7,
    "US.UT": 7,
    "US.WA": 7,
    "US.WY": 7,
    "US.AL": 8,
    "US.AR": 8,
    "US.IA": 8,
    "US.IL": 8,
    "US.IN": 8,
    "US.KS": 8,
    "US.KY": 8,
    "US.LA": 8,
    "US.MI": 8,
    "US.MN": 8,
    "US.MO": 8,
    "US.MS": 8,
    "US.ND": 8,
    "US.NE": 8,
    "US.OH": 8,
    "US.OK": 8,
    "US.SD": 8,
    "US.TN": 8,
    "US.TX": 8,
    "US.WI": 8,
    "CA.01": 7,
    "CA.02": 7,
    "CA.03": 8,
    "CA.04": 2,
    "CA.05": 2,
    "CA.07": 2,
    "CA.08": 2,
    "CA.09": 2,
    "CA.10": 2,
    "CA.11": 8,
    "CA.12": 7,
    "CA.13": 7,
    "CA.14": 2,
    "AU.01": 17,
    "AU.02": 17,
    "AU.03": 17,
    "AU.04": 17,
    "AU.05": 17,
    "AU.06": 17,
    "AU.07": 17,
    "AU.08": 17,
}


def clean_int(value):
    if value == "":
        return None
    return int(value)


def clean_float(value):
    if value == "":
        return None
    return float(value)


def create_schema(conn):
    conn.executescript(
        """
        DROP TABLE IF EXISTS admin1_game_regions;
        DROP TABLE IF EXISTS country_game_regions;
        DROP TABLE IF EXISTS game_regions;
        DROP TABLE IF EXISTS cities;
        DROP TABLE IF EXISTS admin1_regions;
        DROP TABLE IF EXISTS countries;
        DROP TABLE IF EXISTS continents;

        CREATE TABLE continents (
            code TEXT PRIMARY KEY,
            name TEXT NOT NULL
        );

        CREATE TABLE countries (
            iso2 TEXT PRIMARY KEY,
            iso3 TEXT,
            iso_numeric TEXT,
            fips TEXT,
            name TEXT NOT NULL,
            capital TEXT,
            area_sq_km REAL,
            population INTEGER,
            continent_code TEXT NOT NULL,
            tld TEXT,
            currency_code TEXT,
            currency_name TEXT,
            phone TEXT,
            postal_code_format TEXT,
            postal_code_regex TEXT,
            languages TEXT,
            geoname_id INTEGER,
            neighbours TEXT,
            equivalent_fips_code TEXT,
            FOREIGN KEY (continent_code) REFERENCES continents(code)
        );

        CREATE TABLE admin1_regions (
            code TEXT PRIMARY KEY,
            country_iso2 TEXT NOT NULL,
            admin1_code TEXT NOT NULL,
            name TEXT NOT NULL,
            ascii_name TEXT,
            geoname_id INTEGER,
            FOREIGN KEY (country_iso2) REFERENCES countries(iso2)
        );

        CREATE TABLE cities (
            geoname_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            ascii_name TEXT,
            alternate_names TEXT,
            latitude REAL,
            longitude REAL,
            feature_class TEXT,
            feature_code TEXT,
            country_iso2 TEXT NOT NULL,
            cc2 TEXT,
            admin1_code TEXT,
            admin2_code TEXT,
            admin3_code TEXT,
            admin4_code TEXT,
            population INTEGER,
            elevation INTEGER,
            dem INTEGER,
            timezone TEXT,
            modification_date TEXT,
            FOREIGN KEY (country_iso2) REFERENCES countries(iso2)
        );

        CREATE TABLE game_regions (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            difficulty_name TEXT NOT NULL,
            difficulty_level INTEGER NOT NULL
        );

        CREATE TABLE country_game_regions (
            country_iso2 TEXT PRIMARY KEY,
            game_region_id INTEGER NOT NULL,
            requires_admin1_selection INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (country_iso2) REFERENCES countries(iso2),
            FOREIGN KEY (game_region_id) REFERENCES game_regions(id)
        );

        CREATE TABLE admin1_game_regions (
            admin1_code TEXT PRIMARY KEY,
            game_region_id INTEGER NOT NULL,
            FOREIGN KEY (admin1_code) REFERENCES admin1_regions(code),
            FOREIGN KEY (game_region_id) REFERENCES game_regions(id)
        );

        CREATE INDEX idx_countries_continent
            ON countries(continent_code);

        CREATE INDEX idx_admin1_country
            ON admin1_regions(country_iso2);

        CREATE INDEX idx_cities_country
            ON cities(country_iso2);

        CREATE INDEX idx_cities_country_population
            ON cities(country_iso2, population DESC);

        CREATE INDEX idx_cities_admin1
            ON cities(country_iso2, admin1_code);

        CREATE INDEX idx_country_game_regions_region
            ON country_game_regions(game_region_id);

        CREATE INDEX idx_admin1_game_regions_region
            ON admin1_game_regions(game_region_id);
        """
    )


def import_continents(conn):
    conn.executemany(
        "INSERT INTO continents (code, name) VALUES (?, ?)",
        sorted(CONTINENTS.items()),
    )


def import_countries(conn):
    rows = []

    with COUNTRY_INFO_PATH.open("r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file, delimiter="\t")

        for row in reader:
            if not row or row[0].startswith("#"):
                continue

            rows.append(
                (
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    clean_float(row[6]),
                    clean_int(row[7]),
                    row[8],
                    row[9],
                    row[10],
                    row[11],
                    row[12],
                    row[13],
                    row[14],
                    row[15],
                    clean_int(row[16]),
                    row[17],
                    row[18] if len(row) > 18 else "",
                )
            )

    conn.executemany(
        """
        INSERT INTO countries (
            iso2, iso3, iso_numeric, fips, name, capital, area_sq_km,
            population, continent_code, tld, currency_code, currency_name,
            phone, postal_code_format, postal_code_regex, languages,
            geoname_id, neighbours, equivalent_fips_code
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        rows,
    )


def import_admin1_regions(conn):
    rows = []

    with ADMIN1_PATH.open("r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file, delimiter="\t")

        for row in reader:
            if not row:
                continue

            code = row[0]
            country_iso2, admin1_code = code.split(".", 1)

            rows.append(
                (
                    code,
                    country_iso2,
                    admin1_code,
                    row[1],
                    row[2],
                    clean_int(row[3]),
                )
            )

    conn.executemany(
        """
        INSERT INTO admin1_regions (
            code, country_iso2, admin1_code, name, ascii_name, geoname_id
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        rows,
    )


def import_cities(conn):
    rows = []

    with CITIES_PATH.open("r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file, delimiter="\t")

        for row in reader:
            if not row:
                continue

            rows.append(
                (
                    clean_int(row[0]),
                    row[1],
                    row[2],
                    row[3],
                    clean_float(row[4]),
                    clean_float(row[5]),
                    row[6],
                    row[7],
                    row[8],
                    row[9],
                    row[10],
                    row[11],
                    row[12],
                    row[13],
                    clean_int(row[14]),
                    clean_int(row[15]),
                    clean_int(row[16]),
                    row[17],
                    row[18],
                )
            )

    conn.executemany(
        """
        INSERT INTO cities (
            geoname_id, name, ascii_name, alternate_names, latitude, longitude,
            feature_class, feature_code, country_iso2, cc2, admin1_code,
            admin2_code, admin3_code, admin4_code, population, elevation,
            dem, timezone, modification_date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        rows,
    )


def import_game_regions(conn):
    conn.executemany(
        """
        INSERT INTO game_regions (
            id, name, difficulty_name, difficulty_level
        )
        VALUES (?, ?, ?, ?)
        """,
        GAME_REGIONS,
    )

    country_rows = dict(COUNTRY_GAME_REGIONS)
    for iso2, continent_code in conn.execute(
        "SELECT iso2, continent_code FROM countries"
    ):
        if iso2 not in country_rows and continent_code in CONTINENT_GAME_REGION_DEFAULTS:
            country_rows[iso2] = CONTINENT_GAME_REGION_DEFAULTS[continent_code]

    countries_with_admin1 = {
        row[0]
        for row in conn.execute(
            "SELECT DISTINCT country_iso2 FROM admin1_regions"
        )
    }

    conn.executemany(
        """
        INSERT INTO country_game_regions (
            country_iso2, game_region_id, requires_admin1_selection
        )
        VALUES (?, ?, ?)
        """,
        [
            (
                iso2,
                game_region_id,
                int(iso2 in ADMIN1_SELECTION_COUNTRIES and iso2 in countries_with_admin1),
            )
            for iso2, game_region_id in sorted(country_rows.items())
        ],
    )

    admin1_rows = dict(ADMIN1_GAME_REGIONS)
    for code, country_iso2 in conn.execute(
        "SELECT code, country_iso2 FROM admin1_regions"
    ):
        if country_iso2 in ADMIN1_COUNTRY_GAME_REGION_DEFAULTS:
            admin1_rows.setdefault(
                code,
                ADMIN1_COUNTRY_GAME_REGION_DEFAULTS[country_iso2],
            )

    conn.executemany(
        """
        INSERT INTO admin1_game_regions (
            admin1_code, game_region_id
        )
        VALUES (?, ?)
        """,
        sorted(admin1_rows.items()),
    )


def print_counts(conn):
    for table_name in (
        "continents",
        "countries",
        "admin1_regions",
        "cities",
        "game_regions",
        "country_game_regions",
        "admin1_game_regions",
    ):
        count = conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
        print(f"{table_name}: {count}")


def main():
    for path in (COUNTRY_INFO_PATH, ADMIN1_PATH, CITIES_PATH):
        if not path.exists():
            raise FileNotFoundError(f"Missing required file: {path}")

    if DB_PATH.exists():
        DB_PATH.unlink()

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        create_schema(conn)
        import_continents(conn)
        import_countries(conn)
        import_admin1_regions(conn)
        import_cities(conn)
        import_game_regions(conn)
        conn.commit()
        print_counts(conn)

    print(f"Created {DB_PATH}")


if __name__ == "__main__":
    main()
