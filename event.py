def list_attendees_by_event(attendees, event_name):
 
 attending_names = []
 for attendee, attended_event in attendees:
    if attended_event == event_name:
      attending_names.append(attendee)

 return attending_names

def count_attendees_per_event(attendees):


  event_counts = {}
  for attendee, attended_event in attendees:
    if attended_event not in event_counts:
      event_counts[attended_event] = 0
    event_counts[attended_event] += 1

  return event_counts

attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
    ("David", "Python Conference"),
    ("Emily", "Web Development Workshop"),
]

event_to_list = "Python Conference"
attending_list = list_attendees_by_event(attendees, event_to_list)

if attending_list:
  print(f"Attendees for '{event_to_list}':")
  for name in attending_list:
    print(f"- {name}")
else:
  print(f"No attendees found for '{event_to_list}'.")

event_counts = count_attendees_per_event(attendees)

print("\nAttendees per Event:")
for event, count in event_counts.items():
  print(f"- {event}: {count} attendee(s)")