from datetime import datetime
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while file.readline() != '':
            all_data.append(file.readline())


filename = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.now()
        pool.map(read_info, filename)
        end = datetime.now()
        print(f'Многопроцессорный: {end-start}')
