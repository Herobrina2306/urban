from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while file.readline() != '':
            all_data.append(file.readline())


filename = [f'./file {number}.txt' for number in range(1, 5)]

start1 = datetime.now()
for i in filename:
    read_info(i)

end1 = datetime.now()
print(f'Линейный: {end1-start1}')


