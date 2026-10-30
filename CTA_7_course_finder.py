"""

Task: Using the latest version of Python, write a program that functions as a course information system. 
You will use multiple dictionaries to store and retrieve data based on a course number. 
You should develop your code in Visual Studio Code or any other tool of your preference.

Step 1: Data Specifications
Create three separate dictionaries to store the following data. 
In each dictionary, the Course Number must serve as the Key.

Step 2: Program Logic
Input: Prompt the user to enter a Course Number (e.g., CSC101).
Retrieval: Use that input to look up the corresponding values across your dictionaries.


Output: Display the Room Number, Instructor, and Meeting Time. If the course does not exist, provide a friendly error message.



"""

# course numbers are keys to all dictionaries.
ROOM_NUMBERS = {
    "CSC101": 3004,
    "CSC102": 4501,
    "CSC103": 6755,
    "NET110": 1244,
    "COM241": 1411,
}
#instructors
INSTRUCTORS = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee",
}

# meeting times
MEETING_TIMES = {
    "CSC101": "Monday, 9:00 AM",
    "CSC102": "Tuesday, 10:00 AM",
    "CSC103": "Wednesday, 11:00 AM",
    "NET110": "Thursday, 1:00 PM",
    "COM241": "Friday, 2:00 PM",
}


#function to get course information
def get_course_information(course_number: str) -> tuple[int, str, str]:
    """Return the room, instructor, and meeting time for a course."""
    room = ROOM_NUMBERS[course_number]
    instructor = INSTRUCTORS[course_number]
    meeting_time = MEETING_TIMES[course_number]

    return room, instructor, meeting_time

#main function
def main() -> None:
    print("")
    print("**************************")
    print("Course Information System")
    print("**************************")
    print("")

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
            print("")
            print(f"Thank You for using the Course Information System !")
            print("Goodbye!")
            print("")
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
