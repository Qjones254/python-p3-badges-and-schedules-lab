def badge_maker(name):
    return f"Hello, my name is {name}."
 

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

print(badge_maker("Arel")) 

names = ["Arel", "Jimmy", "Quincy","Kelvin"]
badges = batch_badge_creator(names)
print(badges)  


def assign_rooms(names):
    rooms = list(range(1,9))

    room_assignments =[]
    for i in range(len(names)):
        name = names[i]
        room = rooms[i]
        room_assignments.append(f"Hello, {name}! You'll be assigned to room {room}!")
    return room_assignments

speakers = ["Alice", "Jimmy", "Charlie", "David", "Quincy", "Arel", "Kelvin", "Hannah"]
assignments = assign_rooms(speakers)
for assignment in assignments:
    print(assignment)

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print (badge)
    assignments = assign_rooms(names)
    for assignment in assignments:
        print (assignment)
    return None
