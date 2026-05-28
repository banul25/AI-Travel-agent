from tools.flights_tool import search_flights
from tools.hotels_tool import search_hotels
from tools.places_tool import search_places
from tools.weather_tool import get_weather


def agent(query):

    query = query.lower()

    city = None

    cities = [
        "goa",
        "bangalore",
        "delhi",
        "mumbai",
        "hyderabad",
        "chennai",
        "kolkata",
        "jaipur"
    ]

    for c in cities:
        if c in query:
            city = c
            break

    if not city:
        return "Please mention a destination city."

    # ---------------- FLIGHTS ----------------

    flight_output = "No flights found"

    try:

        if "from" in query and "to" in query:

            source = query.split("from")[1].split("to")[0].strip()

            destination = query.split("to")[1].strip().split()[0]

            flight_output = search_flights(source, destination)

        else:

            source = "delhi"

            flight_output = search_flights(source, city)

    except Exception as e:

        flight_output = f"Could not process flights: {e}"

    # ---------------- HOTELS ----------------

    hotel_output = search_hotels(city)

    # ---------------- WEATHER ----------------

    weather_output = get_weather(city)

    # ---------------- PLACES ----------------

    places_output = search_places(city)

    # ---------------- ITINERARY ----------------

    itineraries = {

        "goa": """
### Day 1
- Baga Beach
- Candolim Market
- Beachside Dinner

### Day 2
- Basilica of Bom Jesus
- Old Goa Heritage Walk
- Fort Aguada

### Day 3
- Water Sports at Calangute
- Shopping
- Sunset Cruise
""",

        "delhi": """
### Day 1
- India Gate
- Connaught Place
- Chandni Chowk Food Tour

### Day 2
- Red Fort
- Qutub Minar
- Lotus Temple

### Day 3
- Akshardham Temple
- Dilli Haat
- Shopping & Street Food
""",

        "bangalore": """
### Day 1
- Lalbagh Botanical Garden
- Cubbon Park
- Brigade Road

### Day 2
- Bangalore Palace
- ISKCON Temple
- UB City Mall

### Day 3
- Nandi Hills
- Café Hopping
- Shopping
""",

        "mumbai": """
### Day 1
- Gateway of India
- Marine Drive
- Colaba Causeway

### Day 2
- Juhu Beach
- Siddhivinayak Temple
- Bandra

### Day 3
- Film City Tour
- Shopping
- Café Hopping
""",

        "hyderabad": """
### Day 1
- Charminar
- Laad Bazaar
- Hyderabadi Biryani Dinner

### Day 2
- Golconda Fort
- Salar Jung Museum
- Hussain Sagar Lake

### Day 3
- Ramoji Film City
- Shopping
- Street Food Tour
""",

        "chennai": """
### Day 1
- Marina Beach
- Kapaleeshwarar Temple
- Local Food Tour

### Day 2
- Mahabalipuram
- Dakshinachitra
- Shopping

### Day 3
- Elliot Beach
- Café Visit
- Cultural Show
""",

        "kolkata": """
### Day 1
- Victoria Memorial
- Park Street
- Howrah Bridge

### Day 2
- Dakshineswar Temple
- Indian Museum
- College Street

### Day 3
- Eco Park
- Shopping
- Bengali Food Tour
""",

        "jaipur": """
### Day 1
- Hawa Mahal
- City Palace
- Local Market

### Day 2
- Amer Fort
- Jal Mahal
- Nahargarh Fort

### Day 3
- Chokhi Dhani
- Shopping
- Cultural Show
"""
    }

    itinerary_output = itineraries.get(
        city,
        "Explore local attractions and enjoy your trip."
    )

    # ---------------- FINAL RESPONSE ----------------

    final_response = f"""
# ✈️ Your 3-Day Trip to {city.title()}

## 🛫 Flight Selected
{flight_output}

---

## 🏨 Hotel Recommendation
{hotel_output}

---

## 🌦️ Weather Forecast
{weather_output}

---

## 📍 Itinerary
{itinerary_output}

---

## ⭐ Recommended Tourist Places
{places_output}

---

## 💰 Estimated Budget

- Flights: ₹4800
- Hotel: ₹6400
- Food & Travel: ₹2500

# ✅ Total Estimated Cost: ₹13,700
"""

    return final_response