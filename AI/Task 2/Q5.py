from Q4 import main_dict

with open("filtered.txt", "w") as f:
    for i in main_dict:
        x = main_dict[i]['name']
        y = main_dict[i]['birth']
        f.write(f'{i} {x} - {y} \n')
f.close()