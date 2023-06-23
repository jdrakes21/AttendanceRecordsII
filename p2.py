"""
File: py2.py
Author: Jervon Drakes
Date: 17/11/2022
Lab Section: 32
Email:  jdrakes1@umbc.edu
Description:  This program returns various information cs it relates to the attendance of students
"""

# Comment the line below out if your have the load_dictionary function working!!
# Comment the line below out if your have the load_dictionary function working!!

# from dataEntryP2 import fillAttendanceData


# Comment the line above out if your have the load_dictionary function working!!
# Comment the line above out if your have the load_dictionary function working!!

MINUTE_CONSTANT = 60
SECOND_CONSTANT = 60


def load_roster(roster_file):
    """
  Loads a roster from a file which contains student's names. Those students are then placed into a list
  :param roster_file: A file containing student's names
  :return: A list of the class roster
  """
    # opens the roster file
    with open(roster_file) as file:
        # reads the file
        content = file.readlines()
        # sets an empty list called roster
        class_roster = []
        # loops through the file
        for student_name in content:
            # assigns the variable student name to each student in the file
            student_name = student_name.strip()
            # adds each student to the roster list
            class_roster.append(student_name)
        # returns the roster list
        return class_roster


def load_dictionary(infile):
    """
   Loads a file which contains multiple entries for student attendance logs. Those entries as well as the student names
   are placed in a dictionary
  :param infile: A file containing student attendance logs
  :return: A dictionary containing the students and their attendance data
  """
    # opens the file which contains student attendance information
    with open(infile) as file:
        # reads the file
        content_material = file.readlines()
        # sets an empty dictionary called data content
        data_content = {}
        # loops through the dictionary
        for entry in content_material:
            # splits each student's data
            student_data = entry.split(", ")
            # assigns name as the first and second pieces on information
            name = student_data[0] + ", " + student_data[1]
            # assigns date time as the third and fourth pieces of information
            date_time = student_data[2] + ", " + student_data[3]
            date_time = date_time.strip()
            # condition to determine whether the name is or is not in the dictionary
            if name not in data_content:
                data_content[name] = []
            # adds the student's date time information to the dictionary with his/her respective key
            data_content[name].append(date_time)
    # returns data content
    return data_content


def display_attendance_data_for_student(fixed_name, student_data):
    """
  Displays the log in data for a particular student
  :param fixed_name: A particular student for which the log in data will be determined for
  :param student_data: A dictionary which includes attendance data for students
  :return: The log in data for a particular student
  """
    # conditional to determine whether the student is within student data
    if fixed_name in student_data:
        # assigns the variable, name, as the specified student within student data
        name = student_data[fixed_name]
        # prints the student and their attendance data
        print(fixed_name, name)
    else:
        # otherwise this output is printed if the student has no attendance data
        print("No student of this name in attendance log")


def is_present(student_name, date, student_data):
    """
    Simply return True if a student logged into class on a specific date.
  :param student_name: A student used to determine whether they attended class on a specific date
  :param date: A specified date to determine whether a student attended class on this date
  :param student_data: A dictionary which includes attendance data for students
  :return: True or False as to if a particular student showed up on a date
  """
    # condition to determine if a particular student is within student
    if student_name in student_data:
        # loops through the keys in student data
        for element in student_data[student_name]:
            # condition to determine if a student has attendance data for a particular date
            if date in element:
                # if that student does True is returned
                return True
    # if they don't false is returned
    return False


def list_all_students_checked_in(specific_date, data_student):
    """
      Simply display the students who attended class on a particular date. This function will return a list of those
      students and the number of items within it
      :param specific_date: A specific date to determine the number of students that attended class that day
      :param data_student: A dictionary which includes attendance data for students
      :return: The students who are attended class on a specific data and the number of students
      """
    # sets an empty list called checked in
    checked_in = []

    # loops through data student
    for name_of_student in data_student:
        # assigns the variable dates the values each student has
        dates = data_student[name_of_student]
        # loops through dates
        for entry in dates:
            # splits each entry in dates
            data_1 = entry.split(", ")
            # assigns the variable date as the second piece of information within data 1 which is the date
            date = data_1[1]
            # conditional to determine if the data matches the specific date
            if date == specific_date:
                # adds the student to the checked in list if the conditional is met
                checked_in.append(name_of_student)
    # returns the checked in list
    return checked_in


def list_all_students_checked_in_before(specified_date, assigned_time, data_attend):
    """
      Displays students that attended class on a given date and before a given time. The function will produce and
      return a list of those students and the number of items
      :param specified_date: A specified date used to determine the students which attended class for that date
      :param assigned_time: An assigned time to determine the students who arrived before it on that date
      :param data_attend : A dictionary which includes student attendance data
      :return: The students who attended class on a particular date and arrived before a given time and the number of
               students
      """
    # creates an empty list called attend
    attend = []

    # loops through data attend
    for name_of_student in data_attend:
        # assigns a variable for the student's attendance
        student_date = data_attend[name_of_student]
        # loops through student date
        for entry in student_date:
            # splits each entry
            data_2 = entry.split(", ")
            # assigns date as the second index value in data 2
            date = data_2[1]
            # assigns time as the first index value in data 2
            time_stamp = data_2[0]

            # returns integers for the hour portion of each time stamp
            time_stamp_hour = int(time_stamp[0:2])
            # returns minutes for the minutes portion of each time stamp
            time_stamp_minutes = int(time_stamp[3:5])
            # returns seconds for the seconds portion of each time stamp
            time_stamp_seconds = int(time_stamp[6:8])

            # converts the hours to seconds
            time_hour_conversion = time_stamp_hour * MINUTE_CONSTANT * SECOND_CONSTANT
            # converts the minutes to seconds
            time_minute_conversion = time_stamp_minutes * SECOND_CONSTANT
            # calculation to determine the total seconds
            total_seconds = time_hour_conversion + time_minute_conversion + time_stamp_seconds

            # returns integers for the hour portion of the assigned time stamp
            assigned_time_hour = int(assigned_time[0:2])
            # returns integers for the minutes portion of the assigned time stamp
            assigned_time_minutes = int(assigned_time[3:5])
            # returns integers for the seconds portion of the assigned time stamp
            assigned_time_seconds = int(assigned_time[6:8])

            # converts the hours of the assigned time stamp to seconds
            assigned_hour_conversion = assigned_time_hour * MINUTE_CONSTANT * SECOND_CONSTANT
            # converts the minutes of the assigned time stamp to seconds
            assigned_minute_conversion = assigned_time_minutes * SECOND_CONSTANT
            # calculates the total seconds for the assigned time stamp
            total_assigned_seconds = assigned_hour_conversion + assigned_minute_conversion + assigned_time_seconds

            # conditional to determine whether the date matches the specified date and the total seconds are less
            # than the assigned time stamp seconds
            if date == specified_date and total_seconds < total_assigned_seconds:
                attend.append(name_of_student)

    return attend


def list_students_attendance_count(num_days, stu_data, roster_class):
    """
      Displays the students who attended class for a specific number of days. The function will produce and return those
      students and the number of items
      :param num_days: A particular number of days given
      :param stu_data: A dictionary which includes student attendance data
      :param roster_class: A list of students
      :return: The students who attended class for the given number of days and the number of students
      """
    # creates an empty list called attendance
    attendance = []
    # conditional for when the number of days is 0
    if num_days == 0:
        # once conditional is met the roster is looped through
        for student_name in roster_class:
            # conditional to determine if the student's name appears in stu data
            if student_name not in stu_data.keys():
                # if the conditional is met the student's name is added to the attendance list
                attendance.append(student_name)
    else:
        # loops through stu data
        for i in stu_data:
            # conditional to determine if the entries for each student in stu data matches the number of days
            if len(stu_data[i]) == num_days:
                # once the conditional is met the student is added to the attendance list
                attendance.append(i)
    return attendance


def get_first_student_to_enter(class_date, s_data):
    """
      This function simply displays the students who swiped in first on a specific date
      :param class_date: A particular class date used
      :param s_data: A dictionary which includes student attendance data
      :return: The students who swiped in first on a specific date
      """
    # sets the earliest person as the first person within s data
    earliest_person = list(s_data.keys())[0]
    # splits the time and dates for that respective person
    earliest_time_split = s_data[earliest_person][0].split(", ")
    # sets the earliest time as the first index of the earliest time split
    earliest_time = earliest_time_split[0]

    # loops through s data
    for name in s_data:
        # assigns a variable of name list which includes the times and dates for students
        name_list = s_data[name]
        # loops through name list
        for entry in name_list:
            # splits each entry
            entry_split = entry.split(", ")
            # conditional to determine if the specified class date matches the second index of entry split
            if class_date == entry_split[1]:
                # once that conditional is met the earliest person on that specific date is determined by this
                # comparison
                if entry_split[0] < earliest_time:
                    # earliest person is assigned
                    earliest_person = name
                    # earliest time is assigned
                    earliest_time = entry_split[0]
    return earliest_person


def print_list(xlist):
    """
    This function simply prints the list. The function should not be able to change any
    values of that list passed in.
    :param xlist: List of the values return
    :return: The list of all the values returned
    """
    # loops through xList
    for element in xlist:
        # prints each element in xList
        print(element)
    print()


def print_count(xlist):
    """
    This function simply prints the number of items in a list.
    :param xlist: List of the values return
    :return: The number of items in a list for specific functions
    """
    # sets count to 0
    count = 0
    # loops through x =List
    for i in range(len(xlist)):
        # increments count by 1
        count += 1
    # prints the number of items within a specific list for a function
    print("There are", count, "number of items in list")
    print()
    return count


def print_dictionary(dict_1):
    """
    This function simply prints the dictionary which was loaded
    :param dict_1: A dictionary which contains the log in attendance for students
    :return: The dictionary of the attendance log in data
    """
    # loops through dict 1
    for name in dict_1:
        # prints the student name and the attendance log for each student
        print(name, dict_1[name])


def connect_to_data_file(filename):
    # will return connection to data file
    infile = ""

    try:
        # infile = open("data.txt", "r")
        # infile = open("dataAllShow1stClass.txt", "r")
        infile = open("dataAllShow1stAnd2ndClass.txt", "r")
        infile = open("rosters.txt", "r")
    except FileNotFoundError:
        print("file was not found, try again")

    return infile  # connection with the file


if __name__ == '__main__':

    infile = connect_to_data_file("randomData.txt")
    if infile:
        print("connected to data file...")
    else:
        print("issue with data file... STOP")
        exit(1)

    data = load_dictionary("dataAllShow1stAnd2ndClass.txt")
    roster = load_roster("rosters.txt")
    # ************************
    # OR MANUALLY!!!
    # ************************

    # just making sure the data collected is good
    print("** This is the entire Dictionary Data currently stored **")
    print_dictionary(data)
    print()

    print("********* Looking up Student Attendance Data ***********")
    display_attendance_data_for_student("Morrison, Simon", data)
    display_attendance_data_for_student("Arsenault, Al", data)
    print()

    print("********* Looking to see if Student was present on date ***********")
    print(is_present("Bower, Amy", "11/5/2022", data))
    print(is_present("Bower, Amy", "11/17/2022", data))
    print()

    # display when students first signed in
    print("**** Students present on this date ****")
    result = list_all_students_checked_in("11/5/2022", data)
    print_list(result)
    print_count(result)

    print("**** Those present on date & before a time assigned ****")
    result = list_all_students_checked_in_before("11/5/2022", "08:55:04", data)
    print_list(result)
    print_count(result)

    # list the good students that showed up both days
    print("**** Those who attended BOTH classes ****")
    result = (list_students_attendance_count(2, data, roster))
    print_list(result)
    print_count(result)

    # list the  students that showed up ONE of the days
    print("**** Those who attended ONE class ****")
    result = (list_students_attendance_count(1, data, roster))
    print_list(result)
    print_count(result)

    # list the  students that have not shown up
    print("**** Those who have NOT attended a SINGLE class ****")
    result = (list_students_attendance_count(0, data, roster))
    print_list(result)
    print_count(result)

    # list the first student to enter on this date
    print("**** First student to enter on 11/2/2022 ****")
    print(get_first_student_to_enter("11/2/2022", data))

    # list the first student to enter on this date
    print("**** First student to enter on 11/3/2022 ****")
    print(get_first_student_to_enter("11/3/2022", data))

    # list the first student to enter on this date
    print("**** First student to enter on 11/4/2022 ****")
    print(get_first_student_to_enter("11/4/2022", data))

    # list the first student to enter on this date
    print("**** First student to enter on 11/5/2022 ****")
    print(get_first_student_to_enter("11/5/2022", data))
