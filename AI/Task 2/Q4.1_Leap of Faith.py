# I tried a more general way to maintain any number of column entry
# But reached a dead end

dict1 = {}
main_dict = {}
lst = []
with open('grades.txt') as f:
    first_line = f.readline().strip('\n')
    key = first_line[3:].replace('-', '').replace(':', '').replace('  ', ' ')
    for i in key.split():
        dict1[i] = ''
    for line in f:
        line = line.replace('-', '').replace(':', '').replace('  ', ' ').strip('\n')
        main_dict[int(line.split(' ')[0])] = ''
        for i, k in enumerate(dict1.keys()):
            dict1[k] = line.split(' ')[1:][i]
        print(dict1)
        #print(main_dict)
f.close()

