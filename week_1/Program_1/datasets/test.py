def make_dictionary(data, kind="min"):
    new_dict = {}
    prev_entry = 0
    curr_entry = 0
    min_entry = 20000000000

    for row in data:
        row = row.strip()
        row = row.split(',')
        
        curr_entry = int(row[9])

        if min_entry > (curr_entry - prev_entry):
            min_entry = curr_entry - prev_entry
            new_dict[row[3]] = min_entry

        prev_entry = int(row[9])

    print(new_dict)


def main():
   
    file_name = 'turnstile_220611.txt'
    with open(file_name,encoding='UTF-8') as file_d:
        lines = file_d.readlines()

    data = lines[1:]


    min_dict = make_dictionary(data, kind = "min")
   

if __name__ == "__main__":
    main()