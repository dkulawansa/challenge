import argparse
import json
import os
import sys
from csv import reader, writer
import operator
from datetime import datetime


def main():
    """ This driver function reads command line arguments and does the followings.
        It calls create_combine() function to read all input data files and stores
        them in a new file for later use. Then it parses command line args and
        print the output.
    """

    text = """Displays a list of providers sorted by the following command line arguments. If no
    argument is provided it will be defaulted to ptype_lname """
    parser = argparse.ArgumentParser(description=text)
    parser.add_argument("--ptype_lname", action='store_true', help="sorted by provider "
                                                                   "type then by last name ascending.")
    parser.add_argument("--dob", action='store_true', help="sorted by birth date, ascending.")
    parser.add_argument("--lastname", action='store_true', help="sorted by last name, descending.")

    create_combine()  # call to read and stores provider data from all of the files into one file

    args = parser.parse_args()
    if args.dob:
        print_data(sorted_by_dob())
    elif args.lastname:
        print_data(sorted_by_lastname())
    else:
        print_data(sorted_by_provider_type_lastname())


def create_combine():
    """ This function uses a configuration file named 'config.py' to identify
        and read all input data files. The config.py file is required to run
        the program and it is extendable. If there are new data files to be
        processed they can be processed by adding to the config.py. Further more,
        if data column positions are switched that can be corrected too.
        Columns are arranged to the order Last name, First name, Middle Name,
        Gender, Date of Birth, and Provider Type. It creates a new file named
        'combine' and writes all the data into the new file.
     """

    # Column position assignments
    # Date of Birth = 0
    # Provider Type = 1

    if os._exists("combine"):   # remove combine if it already exists in the folder
        os.remove("combine")
    try:
        with open('config.py', 'r', encoding='utf-8') as fh:
            config_data = json.load(fh)
        data_format = config_data['data_format']
    except FileNotFoundError as ex:
        sys.stderr.write("FileNotFoundError: Please make sure {} "
                         "file in the current directory".format('config.py'))
        return
    file = ''
    try:
        providers = list()
        for file in data_format:
            with open(file['file_name'], 'r') as csvfile:
                rows = csvfile.readlines()
                cols = []
                cols.extend(file['cols_list'])
                for row in rows:
                    (*fullname, gender,
                     cols[file['cols_list'][0]],
                     cols[file['cols_list'][1]]) = row.strip().split(file['delimiter'])

                    mm, dd, yyyy = cols[0].split(file['date_delimiter'])
                    date_of_birth = format_date(mm, dd, yyyy)
                    gender = gender[:1]
                    provider = cols[1].strip().replace('.', '')
                    providers.append((fullname[0], fullname[1], gender, date_of_birth, provider))

    except FileNotFoundError as ex:
        sys.stderr.write(
            "FileNotFoundError: Please make sure a file "
            "named {} is in the current directory".format(file))
        return
    with open('combine', 'w', newline='') as csvfile:
        provider_writer = writer(csvfile, delimiter=',')
        data_sorted = sorted(providers, key=lambda x: x[0], reverse=False)
        provider_writer.writerows(data_sorted)


def format_date(mm, dd, yyyy):
    """ format date to have 2 digit day, 2 digit month and 4 digit year.
    It returns the formated date"""
    if len(mm) == 1:
        mm = '{}{}'.format(0, mm)
    if len(dd) == 1:
        dd = '{}{}'.format(0, dd)
    if len(yyyy) == 2:
        yyyy = '{}{}'.format(19, yyyy)
    return '{}/{}/{}'.format(mm, dd, yyyy)


def sorted_by_provider_type_lastname():
    """ This function first sort the provider data by provider type
    and then last name by ascending order """
    with open('combine', newline='') as csvfile:
        data = reader(csvfile, delimiter=',')
        data_sorted = sorted(data, key=operator.itemgetter(4, 0), reverse=False)
    return data_sorted


def sorted_by_lastname():
    """ This function sort the provider data by last name, descending order """
    with open('combine', newline='') as csvfile:
        data = reader(csvfile, delimiter=',')
        data_sorted = sorted(data, key=lambda x: x[0], reverse=True)
    return data_sorted


def sorted_by_dob():
    """ This function sort the provider data by date of birth, ascending order """
    with open('combine', newline='') as csvfile:
        data = reader(csvfile, delimiter=',')
        data_sorted = sorted(
            data, key=lambda row: datetime.strptime(row[3].strip(), "%m/%d/%Y"), reverse=False)
    return data_sorted


def print_data(data):
    """ print helper function """
    print('\n{0:28} {1}  {2}  {3}'.format(
        '{} {}'.format('Last Name', 'First name'), 'Gender', 'DoB   ', 'Provider Type'))
    print('{0:28} {1}  {2}  {3}\n'.format(
        '{} {}'.format('=========', '=========='), '======', '===   ', '=============='))
    for row in data:
        # print(', '.join(row))
        print('{0:30} {1}  {2}  {3}'.format(
            '{}, {}'.format(row[0], row[1]), row[2], row[3], row[4]))


if __name__ == '__main__':
    main()
