def read_file(day):
    with open('day{:02d}-puzzle-input.txt'.format(day), 'r') as f:
        return [line.strip() for line in f.readlines()] 

def load_list(day, integers=True):
    data = read_file(day)
    if integers:
        return [int(val) for val in data]
    return data
