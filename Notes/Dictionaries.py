travel_log1 = {
    "cities_visited_by_country": {
        "France": [
            {
            "name": "Paris",
            "count": 1
            },
            {
            "name": "Lille",
            "count": 0,
            },
            {
            "name": "Dijon",
            "count": 0   
            }],
        "Germany": [
            {
            "name": "Berlin",
            "count": 0
            },
            {
            "name": "Hamburg",
            "count": 0,
            },
            {
            "name": "Stuttgart",
            "count": 0,
            }
        ]
    }
}



#travel_log2["cities_visited_by_country"]["France"]["Paris"]
travel_log2 = {
    "cities_visited_by_country": {
        "France": {
            "Paris": 1,
            "Lille": 0,
            "Dijon": 0
        },
        "Germany": {
            "Berlin": 0,
            "Hamburg": 0,
            "Stuttgart": 0
        }
    }
}





travel_log3 = [
    {
    "country": "France", 
    "cities_visited": {
        "Paris": 1,
        "Lille": 0,
        "Dijon": 0
        }
    },
    {
    "country": "Germany", 
    "cities_visited": {
        "Berlin": 0,
        "Hamburg": 0,
        "Stuttgart": 0
        }
    }
]
    

def add_new_country(name, cities_visited):
    travel_log3.append({
        "country": name,
        "cities_visited": cities_visited
    })

add_new_country("Russia", {"Moscow": 0, "Saint Petersburg": 0})

print(travel_log3)

