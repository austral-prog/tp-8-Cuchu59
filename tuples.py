"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    return coordinate[0], coordinate[1]


def create_record(azara_record, rui_record):
    if azara_record[1] == rui_record[1][0]+rui_record[1][1]:
        return azara_record + rui_record
    else:
        return "not a match"
