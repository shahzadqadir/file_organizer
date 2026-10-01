import os

with open('data.txt') as file:
    for line in file:
        os.system(f'touch data/{line.strip()}')
