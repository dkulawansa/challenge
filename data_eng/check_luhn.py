from csv import reader


def main():
    """ This function reads the provided list of NPI numbers from a text file.
        If for some reason the file named npi is missing it will throw the
        FileNotFound exception.
    """

    try:
        with open('npi') as csvfile:
            npireader = reader(csvfile, delimiter=' ')
            print('\n{0:12} {1}'.format('NPI Number', 'Valid?'))
            print('{0:12} {1}'.format('==========', '======'))
            for line in npireader:
                results = luhn_checksum('{}{}'.format(80840, line[0]))
                print('{0:12} {1}'.format(line[0], results))
    except FileNotFoundError as ex:
        raise("File with NPI numbers not found ")


def luhn_checksum(npi_number):
    """ this function checks the npi number passes a luhn mod-10 checksum """
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(npi_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return ((checksum % 10) == 0)

if __name__ == '__main__':
    main()
