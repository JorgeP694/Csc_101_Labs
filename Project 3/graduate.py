# Project 3 – Graduate Rate (2017-2018)
# Name:
# Instructor: Dr. S. Einakian
# Section:

from graduate_funcs import (
    read_file,
    create_division,
    create_graduate,
    create_files,
    find_total_avg_of_division,
    find_graduate_total_avg
)


def main() -> None:

    # Read file
    header, data = read_file("graduate_rate.csv")

    # Create objects
    divisions = create_division(data)
    graduates = create_graduate(data)

    # Create division CSV files
    create_files(divisions, graduates)

    print("Divisions:")
    for d in divisions:
        print(d)

    print("\nTotal and Average per Division:")

    for d in divisions:
        first_word = d.division_name.split()[0]

        total, average = find_total_avg_of_division(first_word)

        print(first_word)
        print("Total:", total)
        print("Average:", average)
        print()

    print("Overall Total and Average (All Majors):")

    total_all, average_all = find_graduate_total_avg(graduates)

    print("Total:", total_all)
    print("Average:", average_all)


if __name__ == "__main__":
    main()
