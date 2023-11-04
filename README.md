# ISYS 5713 Demo Project - *College Football Points-Per-Game*

> 1. Setup your python environment: `pip install requirements.txt`

> 2. **Backend** app entry point: `app.py`
>    * Make sure to download `auth_key.txt` from Blackboard and add to the main folder

> 3. **Frontend** app entry point: `\views\frontend.ipybn`

## API Documentation
This API provides important analytics to college football fans so that they can make informed decisions when choosing who to root for each week. The API also provides a mechanism for college football teams to be viewed, added, updated, and deleted.

**Table of Contents**
1. [Analytics Endpoints](#analytics-endpoints)
    - [Get Teams ranked by Points-Per-Game](#ppg)
2. [Teams Endpoints](#teams-endpoints)
    - [Get single Team by ID](#get-single-team)
    - [Get all Teams](#get-all-teams)
    - [Add Team](#add-team)
    - [Update Team](#update-team)
    - [Delete Team](#delete-team)
    - [Get Conferences](#get-conferences)
    - [Get Seasons](#get-seasons)

<a id="analytics-endpoints"></a>
## Analytics Endpoints
<a id="ppg"></a>
### `/ppg`

|METHOD|`GET`|
|-------|-----|
|**Description**|Returns the teams and their Points-Per-Game (ppg) ranked from highest to lowest|
|**Parameters**|*limit* (optional) - limits the number of results returned|

#### Example Request
http://localhost:5000/ppg?limit=10

#### Example Response:
```json
[
    {
        "rank": 1,
        "school": "North Central",
        "ppg": 53.91
    },
    {
        "rank": 2,
        "school": "Incarnate Word",
        "ppg": 53.0
    },
    ...
]
```
<a id="teams-endpoints"></a>
## Teams Endpoints  

<a id="get-single-team"></a>
### `/teams/{team_id}`

|METHOD|`GET`|
|-------|-----|
|**Description**|Gets a single Team based on the given ID|
|**Parameters**|-|

#### Example Request
http://localhost:5000/teams/2

#### Example Response:
```json
{
    "id": 2,
    "school": "Auburn",
    "abbreviation": "AUB",
    "alt_color": "#f1f2f3",
    "color": "#03244d",
    "conference": "SEC",
    "mascot": "Tigers"
}
```

---------------------
<a id="get-all-teams"></a>
### `/teams`

|METHOD|`GET`|
|-------|-----|
|**Description**|Gets all Teams|
|**Parameters**|*conference* (optional) - filters teams by a given conference|

#### Example Request
http://localhost:5000/teams?conference=SEC

#### Example Response:
```json
[
    {
        "id": 2,
        "school": "Auburn",
        "abbreviation": "AUB",
        "alt_color": "#f1f2f3",
        "color": "#03244d",
        "conference": "SEC",
        "mascot": "Tigers"
    },
    ...
]
```

---------------------
<a id="add-team"></a>
### `/teams`

|METHOD|`POST`|
|-------|-----|
|**Description**|Adds a new team|
|**Body**|Takes a json object with the foloowing attributes: `id`, `school`, `abbreviation`, `mascot`, `conference`, `color`, `alt_color`|

#### Example Request
http://localhost:5000/teams

#### Example Body
```json
{
    "id": 1,
    "school": "Pete University",
    "abbreviation": "PETE",
    "alt_color": "#f1f2f3",
    "color": "#03244d",
    "conference": "Best Conference",
    "mascot": "Elephant"
    
}
```

#### Example Response:
```json
"Sucessfully added Team ID 1"
```

---------------------
<a id="update-team"></a>
### `/teams/{team_id}`

|METHOD|`PUT`|
|-------|-----|
|**Description**|Updates a new team|
|**Body**|Takes a json object with the foloowing attributes: `id`, `school`, `abbreviation`, `mascot`, `conference`, `color`, `alt_color`|

#### Example Request
http://localhost:5000/teams/1

#### Example Body
```json
{
    "abbreviation": "PETE",
    "alt_color": "#f1f2f3",
    "color": "#03244d",
    "conference": "Best Conference",
    "id": 1,
    "mascot": "Rockets",
    "school": "Pete Community College"
}
```

#### Example Response:
```json
"Sucessfully updated Team ID 1"
```

---------------------
<a id="delete-team"></a>
### `/teams/{team_id}`

|METHOD|`DELETE`|
|-------|-----|
|**Description**|Deletes a team|

#### Example Request
http://localhost:5000/teams/1

#### Example Response:
```json
"Sucessfully removed Team ID 1"
```

---------------------
<a id="get-conferences"></a>
### `/conferences`

|METHOD|`GET`|
|-------|-----|
|**Description**|Gets list of team conferences|
|**Parameters**||

#### Example Request
http://localhost:5000/conferences

#### Example Response:
```json
[
    null,
    "ACC",
    "American Athletic",
    "American Rivers",
    "American Southwest",
    "Big 12",
    "Big Sky",
    ...
]
```

---------------------
<a id="get-seasons"></a>
### `/seasons`

|METHOD|`GET`|
|-------|-----|
|**Description**|Gets list of seasons|
|**Parameters**||

#### Example Request
http://localhost:5000/conferences

#### Example Response:
```json
[
    2022,
    2023,
    ...
]
```
