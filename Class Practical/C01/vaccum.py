rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

position = "A"

while "Dirty" in rooms.values():
    print("Vacuum is in room", position)

    if rooms[position] == "Dirty":
        print("Cleaning room", position)
        rooms[position] = "Clean"

    elif position == "A":
        position = "B"
        print("Moving to room B")

    else:
        position = "A"
        print("Moving to room A")

    if all(status == "Clean" for status in rooms.values()):
        break

print("Final room status:", rooms)
print("All rooms are clean!")