from datetime import datetime


__result_path = './result/'


def create_multiple_y_file(filename, data):
    timestamp = datetime.today().strftime('%Y-%m-%d_%H.%M')
    rel_pathway = f'{__result_path}{filename}_{timestamp}.txt'
    with open(rel_pathway, 'a') as new_file:
        new_file.write(data)
