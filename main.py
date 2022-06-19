import os.path

# Main Function - Entry Point to the code
def main():
    ## PART A
    # Storing filename variable
    filename = "students.txt"
    # Storing absolute path of filename
    abs_file_path = os.path.abspath(filename)
    # Storing directory name of filename
    dir_name = os.path.dirname(abs_file_path)
    # New Lines
    print()
    print()
    # Printing absolute path of file
    print("Absolute Path : ", abs_file_path)
    # Printing directory name of file
    print("Directory : ", dir_name)
    # Getting base name of file using its absolute path and printing it
    print("Base Name : ", os.path.basename(abs_file_path))
    # Getting file size of file using its absolute path and printing it
    print("File Size : ", os.path.getsize(abs_file_path))
    # Checking if filename is a file using its absolute path and printing return value
    print("Is A File? : ", os.path.isfile(abs_file_path))
    # Checking if filename is a directory using its absolute path and printing return value
    print("Is A Directory : ", os.path.isdir(abs_file_path))
    ## PART B
    # Opening students.txt
    student_file = open(filename)
    # Reading all lines of file
    file_data = student_file.readlines()

    # Printing Header of data
    print("\nName Age Average GPA")

    # Iterating in each line data of students.txt
    for data in file_data:
        # Splitting line data
        each_data=data.split()

        # Calculating averageGPA by iterating from index 2 to 6 (that is last index value)
        total = 0.0
        for index in range(2,len(each_data)):
        total += float(each_data[index])
        averageGPA = total/5

        # Printing Student Name, Age and their average GPA value
        print(each_data[0] + " " + each_data[1] + " " + str(averageGPA))

if __name__ == "__main__":
    main()