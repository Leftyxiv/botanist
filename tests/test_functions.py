#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import os
import unittest

import main

# globals
ONE_DAY = datetime.timedelta(days=1)
START_DATE = datetime.date(2019, 12, 16)
WEEKS = 12
SCHEDULE = main.schedule_per_plant(
    main.parse_json(main.INPUT_FILE), weeks=WEEKS, start_date=START_DATE
)


class TestFunctions(unittest.TestCase):
    def test_no_weekends(self):
        """checks to make sure that no plants are being watered on a weekend"""
        for plant in SCHEDULE:
            for date in SCHEDULE[plant]["schedule"]:
                self.assertNotEqual(date.weekday(), 5)
                self.assertNotEqual(date.weekday(), 6)

    def test_timedeltas(self):
        """checks to make sure that the distance between waterings for any given plant
        is no more or less than one day from its desired watering interval"""
        for plant in SCHEDULE:
            date_list = SCHEDULE[plant]["schedule"]
            delta = datetime.timedelta(days=SCHEDULE[plant]["water_after"])
            prev_day = date_list[0]
            for date in date_list[1:]:
                self.assertGreaterEqual(date - prev_day, delta - ONE_DAY)
                self.assertLessEqual(date - prev_day, delta + ONE_DAY)
                prev_day = date

    def test_twelve_weeks(self):
        for plant in SCHEDULE:
            date_list = SCHEDULE[plant]["schedule"]
            total_days = date_list[-1] - date_list[0]
            weeks = total_days.days / 7.0
            self.assertGreaterEqual(weeks, weeks - 1)

    def test_file_exists(self):
        self.assertTrue(os.path.exists("schedule.txt"))


    
