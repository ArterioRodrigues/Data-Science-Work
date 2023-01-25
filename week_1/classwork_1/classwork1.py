"""
Name:  Arterio Rodrigues
Email: arterio.rodrigues47@myhunter.cuny.edu
Resources:  Python3.8
I attended lecture today.
Row:  2
Seat:  72
"""

def make_dict(file_name, sep=': ') :
    """Function para are a file name and a sep to create a dic of give value"""
    with open(file_name, encoding="utf8") as file:

        file_dict = {}

        for line in file:

            line = line.strip()
            line = line.split(sep)

            if len(line) > 1:
                file_dict[line[0]] = line[1]



    return file_dict
