![LOGO](img/happy_flower.jpeg)

# The Backend Botanist

### Learning Objectives

- Familiarize using [datetime](https://docs.python.org/3/library/datetime.html#module-datetime) library.
- Learn how to use table modules [tabulate](https://github.com/astanin/python-tabulate), [PrettyTable](https://github.com/jazzband/prettytable), or [texttable](https://github.com/foutaise/texttable) to beautify outputs.
- Get more practice reading information from [JSON](https://docs.python.org/3/library/json.html#module-json) files.

### Assignment Goals

- Using the supplied [`plant_info.json`](./plant_info.json) file as input, write a Python program that will create a plant watering schedule that covers the next 12 weeks from an arbitrary start date.
- The plant watering schedule will be a plain text output file named `schedule.txt`. The format of the schedule will be a table of dates, and the specific plants that need watering on that particular date. The starting date of the schedule should be the Monday that follows the arbitrary start date.
- **There is a constraint:** No plants are watered on Saturdays or Sundays (weekends).
- Each plant must be watered as close to it's own interval as possible, as specified in the `plant_info.json` file, taking into account the weekend constraint.

### Part A

Write a function, `parse_json()` to read the [`plant_info.json`](./plant_info.json) file. Then transform it into a single Python dictionary. The **keys** of this dictionary will be the plant names. The **values** for this dictionary will be a dictionaries (yes, dictionaries inside a dictionary) containing `'water_after'` as the **key** and the plant's watering interval as the **value**. The function should return this completed, all-encompassing dictionary.

#### Example Output

```python
{'Fiddle Leaf Fig': {'water_after': 7}, 'Snake Plant': {'water_after': 14}, ... }
```

### Part B

Write a function `schedule_per_plant()` that adds a key value pair, with the key being `schedule`, to each plant's dictionary of the days that plant has to be watered, without being concerned with weekends quite yet. (Hint: Use the pprint library to more easily view this dictionary)

#### Example Output

```python
{
  'Fiddle Leaf Fig': {
    'water_after': 7,
    'schedule': [
      datetime.date(2019, 12, 16),
      datetime.date(2019, 12, 23),
      datetime.date(2019, 12, 30),
      datetime.date(2020, 1, 6),
      datetime.date(2020, 1, 13),
      datetime.date(2020, 1, 20),
      datetime.date(2020, 1, 27),
      datetime.date(2020, 2, 3),
      datetime.date(2020, 2, 10),
      datetime.date(2020, 2, 17),
      datetime.date(2020, 2, 24),
      datetime.date(2020, 3, 2),
      datetime.date(2020, 3, 9),
    ]
  },
  'Snake Plant': {
    'water_after': 14,
    'schedule': [
      datetime.date(2019, 12, 16),
      datetime.date(2019, 12, 30),
      datetime.date(2020, 1, 13),
      datetime.date(2020, 1, 27),
      datetime.date(2020, 2, 10),
      datetime.date(2020, 2, 24),
      datetime.date(2020, 3, 9),
    ]
  },
  ...
}
```

### Part C

Write a function `create_final_schedule()` to create a dictionary of all the days in the 12 week period as the keys and a list of all the plants that need to be watered on that day as the values.

#### Example Output

```python
{
  datetime.date(2019, 12, 16): [
      'Fiddle Leaf Fig',
      'Snake Plant',
      'Money Tree',
      "Bird's Nest Fern",
      'Croton',
      'Bell Pepper Plant',
      'Strawberry Plant',
      'Dracaena',
      'Spider Plant',
      'Jade',
      'Wavy Fern'
    ],
    datetime.date(2019, 12, 17): [],
    datetime.date(2019, 12, 18): ['Wavy Fern'],
    datetime.date(2019, 12, 19): [
      "Bird's Nest Fern",
      'Bell Pepper Plant',
      'Strawberry Plant'
    ],
    ...
}
```

### Part D

Write a function `weekend_filter()` to implement in your `schedule_per_plant` function. It should subtract a day if the plant were to land on a Saturday, and add a day if it were to land on a Sunday.

### Part E

Write a function `create_table()` that converts the final schedule into a 'beautified' table format using any Python table library such as . Write this now beautified table to `schedule.txt`.

### Example Output

```
+-------------------+------------+------------+-------------------+------------+------------+------------+
|     12-16-2019    | 12-17-2019 | 12-18-2019 |     12-19-2019    | 12-20-2019 | 12-21-2019 | 12-22-2019 |
+-------------------+------------+------------+-------------------+------------+------------+------------+
|  Fiddle Leaf Fig  |            | Wavy Fern  |  Bird's Nest Fern | Wavy Fern  |            |            |
|    Snake Plant    |            |            | Bell Pepper Plant |            |            |            |
|     Money Tree    |            |            |  Strawberry Plant |            |            |            |
|  Bird's Nest Fern |            |            |                   |            |            |            |
|       Croton      |            |            |                   |            |            |            |
| Bell Pepper Plant |            |            |                   |            |            |            |
```

### Testing
Use [unittest](https://docs.python.org/3/library/unittest.html) to run the test suite.
```shell
python -m unittest discover
```

## Background

![LOGO](img/eg_headshot.jpeg) ![LOGO](img/eh_headshot.jpeg)

This is a real world entry level application, based off a take home programming challenge given by a company in Chicago in Dec 2019. The original challenge did not outline the steps that needed to be taken to accomplish the challenge. The steps are based off of the solution Enrique Galindo (SE6) wrote and Eric Hanson contributed to.

### PR (Pull Request) Workflow for this Assignment

1. This repo does not allow forking. Instead, create a copy by using the green "Use This Template" button.
2. _Clone_ your copy of the repo to your local development machine.
3. Create a separate branch named `dev`, and checkout the branch.
4. Commit your changes, then `git push` the branch back to your own github account.
5. From your own Github repo, create a pull request (PR) from your `dev` branch back to your own master.
6. Copy/Paste the URL **link to your PR** as your assignment submission in Canvas.
7. Your grader will post code review comments inline with your code, in your github account. Be sure to respond to any comments and make requested changes. **RESUBMIT** a new link to your PR after making changes. This is the code review iteration cycle.
