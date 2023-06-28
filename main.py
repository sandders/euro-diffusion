# main.py

from algorithm import Algorithm

def write_result(file, i, result):
    file.write(f'\nCase Number {i}\n')
    for r in result:
        file.write(f'{r[0]} {r[1]}\n')


def parse_cases(filename):
    with open(filename, 'r') as file:
        country_count = int(file.readline())

        cases = []

        while country_count:
            if not 1 <= country_count <= 20:
                print('Error: The number of countries (1 ≤ c ≤ 20)')
                return None

            lines = []

            for i in range(country_count):
                line = file.readline().strip()
                if not line:
                    print(f'Error: Missing data for country {i+1} in case {len(cases)+1}')
                    return None
                lines.append(line)

            cases.append(lines)

            country_count = int(file.readline())

        return cases


if __name__ == '__main__':
    cases = parse_cases('input.txt')
    if cases:
        case_number = 1
        with open('output.txt', 'w') as output_file:
            for lines in cases:
                try:
                    algorithm = Algorithm()

                    for line in lines:
                        algorithm.add_country(line)

                    result = algorithm.run()
                    write_result(output_file, case_number, result)

                    case_number += 1
                except Exception as e:
                    print(f'\nCase Number {case_number}\n')
                    print(f'Error: {str(e)}\n')
    else:
        print('Error: No tasks found')