"""List of constans for DB <=> CSV mapping."""

INFO_FIELDS = {
    # "Lev.1": "level",
    "POS": "position",
    "Age": "age",
}

RATINGS_FIELDS = {
    # batting
    "CON": "contact",
    "GAP": "gap_power",
    "POW": "power",
    "EYE": "eye",
    "K's": "k",
    # batting pot
    "CON P": "contact_potential",
    "GAP P": "gap_power_potential",
    "POW P": "power_potential",
    "EYE P": "eye_potential",
    "K P": "k_potential",
    # pitching
    "STU": "stuff",
    "MOV": "movement",
    "CON.1": "control",
    # pitching pot
    "STU P": "stuff_potential",
    "MOV P": "movement_potential",
    "CON P.1": "control_potential",
}

LEVEL_MAPPING = {
    "MLB": 1,
    "AAA": 2,
    "AA": 3,
    "A+": 4,
    "A": 5,
    "R": 6,
    "INT": 7,
}
