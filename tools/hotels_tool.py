import json
def search_hotels(city):
    with open("data/hotels.json", "r") as file:
        hotels = json.load(file)

        results = []
        
        for hotel in hotels:
            if hotel["city"].lower() == city.lower():
                results.append(hotel)
        if not results:
            return "No hotels found"
        results = sorted (results, key=lambda x: x["price_per_night"])

        output = []

        for hotel in results:
            output.append(
                        f"Hotel Name: {hotel['name']} | "
                        f"Price per Night: ₹{hotel['price_per_night']} | "
                        f"City: {hotel['city']} |"
                        f"Stars: {hotel['stars']} |"
                        f"Amenities: {','.join(hotel['amenities'])}"
                        )
            return "\n".join(output)