main_dict = {}
dict_temp = {}

with open('grades.txt') as f:
    f.readline()
    for line in f:
        try:
            id, name, score, birth, gender = line.replace('-', '').replace(':', '').strip('\n').split()
            main_dict[int(id)] = {'name' : name, 'score' : int(score), 'birth' : int(birth), 'gender' : gender}
        except ValueError:
            continue

print(main_dict)

oldest = 1
highest_score = 1
lst = []

for i in list(main_dict.keys()):
    lst.append(main_dict[i]['score'])
    if main_dict[i]['birth'] < main_dict[oldest]['birth']:
        oldest = i
    if main_dict[i]['score'] > main_dict[highest_score]['score']:
        highest_score = i

print("Oldest Person has an ID of", oldest)
print("Average Score is", sum(lst) / len(lst))
print("Person with the highest score has a gender (", main_dict[highest_score]['gender'], ')')



