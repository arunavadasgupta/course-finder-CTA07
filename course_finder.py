"""Look up course rooms, instructors, and fictional meeting times."""

ROOM_NUMBERS = {
    "CSC101": 3004,
    "CSC102": 4501,
    "CSC103": 6755,
    "NET110": 1244,
    "COM241": 1411,
}

INSTRUCTORS = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee",
}

# Fictional meeting times used for this assignment.
MEETING_TIMES = {
    "CSC101": "Monday, 9:00 AM",
    "CSC102": "Tuesday, 10:00 AM",
    "CSC103": "Wednesday, 11:00 AM",
    "NET110": "Thursday, 1:00 PM",
    "COM241": "Friday, 2:00 PM",
}


def get_course_information(course_number: str) -> tuple[int, str, str]:
    """Return the room, instructor, and meeting time for a course."""
    room = ROOM_NUMBERS[course_number]
    instructor = INSTRUCTORS[course_number]
    meeting_time = MEETING_TIMES[course_number]

    return room, instructor, meeting_time


def main() -> None:
    """Look up courses repeatedly until the user enters 'q'."""
    print("Course Information System")

    while True:
        try:
            course_number = input(
                "\nEnter a course number (e.g., CSC101) "
                "or 'q' to quit: "
            ).strip().upper()
        except EOFError:
            print("\nInput ended. Goodbye!")
            break
        except KeyboardInterrupt:
            print("\nCourse lookup cancelled. Goodbye!")
            break

        if course_number == "Q":
            print("Goodbye!")
            break

        if not course_number:
            print("Please enter a course number.")
            continue

        try:
            room, instructor, meeting_time = get_course_information(
                course_number
            )
        except KeyError:
            print(
                f"Sorry, complete information for '{course_number}' "
                "could not be found. Please check the course number."
            )
            continue

        print(f"\nCourse Number: {course_number}")
        print(f"Room Number: {room}")
        print(f"Instructor: {instructor}")
        print(f"Meeting Time: {meeting_time}")


if __name__ == "__main__":
    main()
