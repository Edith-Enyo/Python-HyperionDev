print("Type of award to be received in a triathlon")
# Prompt user for events and the time in minutes taken
swimming_time = float(input("Enter the time taken in minutes to complete swimming event: "))
cycling_time = float(input("Enter the time taken in minutes to complete cycling event: "))
running_time = float(input("Enter the time taken in minutes to complete running event: "))
# Calculate total time taken for the events to be completed
total_time_taken = swimming_time + running_time + cycling_time

# Awarded provincial Colours if within qualifying time
if total_time_taken <= 100:
    print("Participant will receive Provincial Colours")
# Awarded Provincial Half Colours if within 5 minutes of qualifying time
elif total_time_taken <= 105:
    print("Participant will receive Provincial Half Colours")
# Awarded Provincial Scroll if within 10 minutes of qualifying time
elif total_time_taken <= 110:
    print("Participant will receive a Provincial Scroll")
# No awards  if more than 10 minutes of qualifying time
else:
    print("Participant does not qualify for an award")

