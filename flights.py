def format_itineraries(itineraries):


  formatted_itineraries = ""
  for index, itinerary in enumerate(itineraries):
    traveler_name, origin, destination = itinerary
   
    formatted_itinerary = f"Itinerary {index + 1}: {traveler_name} - From {origin} to {destination}\n"
    formatted_itineraries += formatted_itinerary

  return formatted_itineraries.rstrip("\n") 

itinerary_data = [
  ("Alice", "New York", "London"),
  ("Bob", "Tokyo", "San Francisco"),
]

formatted_string = format_itineraries(itinerary_data)

print(formatted_string)