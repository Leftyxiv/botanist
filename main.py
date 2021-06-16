#!/usr/bin/env python3

import datetime
import json
import re
import typing
import json
import math
from prettytable import PrettyTable


# globals
INPUT_FILE = "plant_info.json"
OUTPUT_FILE = "schedule.txt"
date_obj = typing.NewType("dat_obj", datetime.date)
# date_obj = datetime.date

def parse_json(filename: str) -> dict:
    d = {}
    with open(filename) as f:
        data = f.read()
    obj = json.loads(data)
    for plant in obj:
        d[plant['name']] = { 'water_after': plant['water_after'] }
    return d

def schedule_per_plant(plant_dict: dict, weeks: int, start_date: date_obj) -> dict:
    for plant in plant_dict:
        water_period = plant_dict[plant]['water_after'][0:-4]
        td = datetime.timedelta(int(water_period))
        water_times = math.floor((weeks * 7) / int(water_period))
        last_date = start_date(datetime.date(2019, 12, 16))
        for _ in range(water_times):
            if not plant_dict[plant].get('schedule'):
                plant_dict[plant]['schedule'] = [last_date]
            else:
                plant_dict[plant]['schedule'].append(last_date)
            last_date = last_date + td
    # print(plant_dict)
    return plant_dict

# schedule_per_plant(parse_json('plant_info.json'), 12, date_obj)

def weekend_filter(date) -> date_obj:
    td = datetime.timedelta(1)
    if date.weekday() == 5:
        return date - td
    elif date.weekday() == 6:
        return date + td
    else:
        return date

def create_final_schedule(
    plant_dict_with_schedule: dict, weeks: int, start_date: date_obj
) -> dict:
    dict_set_date = start_date(datetime.date(2019, 12, 16))
    date = start_date(datetime.date(2019, 12, 16))
    td = datetime.timedelta(1)
    date_dict = {}
    for _ in range(7 * weeks):
        date_dict[dict_set_date] = []
        dict_set_date += td
    # print(date_dict)
    for _ in range(7 * weeks):
        # date_dict[date] = []
        for plant in plant_dict_with_schedule:
            for day in plant_dict_with_schedule[plant]['schedule']:
                if day == date:
                    new_date = weekend_filter(date)
                    date_dict[new_date].append(plant)
        date += td
    # print(date_dict)
    return date_dict

# create_final_schedule(schedule_per_plant(parse_json('plant_info.json'), 12, date_obj), 12, date_obj)



def create_table(final_schedule: dict) -> None:
    my_table = PrettyTable()

    for day in final_schedule:
        # print(day, final_schedule[day])
        while len(final_schedule[day]) < 12:
            final_schedule[day].append("")
        my_table.add_column(str(day), final_schedule[day])
    with open('schedule.txt', 'w') as f:
        f.write(str(my_table))



def main(weeks: int, start_date: date_obj) -> None:
    create_table(create_final_schedule(schedule_per_plant(parse_json('plant_info.json'), 12, date_obj), 12, date_obj))
    pass


if __name__ == "__main__":
    main(12, date_obj)
