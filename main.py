#!/usr/bin/env python3

import datetime
import json
import re
import typing


# globals
INPUT_FILE = "plant_info.json"
OUTPUT_FILE = "schedule.txt"
date_obj = typing.NewType("dat_obj", datetime.date)


def parse_json(filename: str) -> dict:
    # Your code here
    pass


def schedule_per_plant(plant_dict: dict, weeks: int, start_date: date_obj) -> dict:
    # Your code here
    pass


def create_final_schedule(
    plant_dict_with_schedule: dict, weeks: int, start_date: date_obj
) -> dict:
    # Your code here
    pass


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
