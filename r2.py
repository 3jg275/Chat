def read_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None                   # None for default empty value
    for line in lines:              # skip 'Allen' by continue function
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':         # skip 'Tom' by continue function
            person = 'Tom'
            continue
        if person:                  # do appending if person is existing
            new.append(person + ': ' + line)
    return(new)                      # send them back one by one

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = convert(lines)          # replacing values
    write_file('output.txt', lines)

main()