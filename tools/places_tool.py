import json

def search_places(city):
    with open("data/places.json", "r") as file:
        places = json.load(file)

        results = []

        for place in places:
            if place["city"].lower() == city.lower():
                results.append(place)

        if not results:
            return "No places found"

        results = sorted(results, key=lambda x: x["rating"], reverse=True)
        output = []
        for place in results:
            output.append(
                f"Place Name: {place['name']} | "
                f"Type: {place['type']} | "
                f"Rating: {place['rating']}"
            )
        return "\n".join(output)