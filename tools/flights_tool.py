import json


def search_flights(source, destination):
    with open("data/flights.json", "r") as file:
        flights = json.load(file)

    results = []

    for flight in flights:
        if (
            flight["from"].lower() == source.lower()
            and flight["to"].lower() == destination.lower()
        ):
            results.append(flight)

    if not results:
        return "No flights found"

    results = sorted(results, key=lambda x: x["price"])

    output = []


    for flight in results:
        output.append(
            f"-{flight['airline']} | "
            f"(₹{flight['price']} )| "
            f"-Departure: {flight['departure_time']}"
        )

    return "\n".join(output)    