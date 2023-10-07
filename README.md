# API Documentation
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
        "ppg": 53.91,
        "rank": 1,
        "school": "North Central"
    },
    {
        "ppg": 53.0,
        "rank": 2,
        "school": "Incarnate Word"
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
    "abbreviation": "AUB",
    "alt_color": "#f1f2f3",
    "color": "#03244d",
    "conference": "SEC",
    "id": 2,
    "mascot": "Tigers",
    "school": "Auburn"
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
        "abbreviation": "AUB",
        "alt_color": "#f1f2f3",
        "color": "#03244d",
        "conference": "SEC",
        "id": 2,
        "mascot": "Tigers",
        "school": "Auburn"
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
    "abbreviation": "PETE",
    "alt_color": "#f1f2f3",
    "color": "#03244d",
    "conference": "Best Conference",
    "id": 1,
    "mascot": "Elephant",
    "school": "Pete University"
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
