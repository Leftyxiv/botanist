#!/usr/bin/env python3

import datetime
import json
import re
import typing
import json
import math


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

def create_final_schedule(
    plant_dict_with_schedule: dict, weeks: int, start_date: date_obj
) -> dict:
    date = start_date(datetime.date(2019, 12, 16))
    td = datetime.timedelta(1)
    date_dict = {}
    for _ in range(7 * weeks):
        date_dict[date] = []
        for plant in plant_dict_with_schedule:
            for day in plant_dict_with_schedule[plant]['schedule']:
                if day == date:
                    date_dict[date].append(plant)
        date += td
    print(date_dict)
    pass

create_final_schedule(schedule_per_plant(parse_json('plant_info.json'), 12, date_obj), 12, date_obj)


def weekend_filter(date) -> date_obj:
    # Your code here
    pass


def create_table(final_schedule: dict) -> None:
    # Your code here
    pass


def main(weeks: int, start_date: date_obj) -> None:
    # Your code here
    pass


if __name__ == "__main__":
    main()
