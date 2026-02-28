# Project 3 Graduate Rate (2017-2018)
# Name:
# Instructor: Dr. S. Einakian
# Section:
# main program: You need to call the functions you created in the
# graduate_funcs.py in an order to create the csv files for each division and
# analyzing your data by calling the final two functions and print the results.

from graduate_funcs import read_file, create_division, create_graduate, create_files


def main() -> None:
    header, data = read_file("graduate_rate.csv")

    divisions = create_division(data)
    graduates = create_graduate(data)

    create_files(divisions, graduates)

    print("Divisions:")
    for d in divisions:
        print(d)

    print("\nFirst 5 Graduate objects:")
    for g in graduates[:5]:
        print(g)


if __name__ == "__main__":
    main()


