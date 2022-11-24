folder_name = "Challenge Nine/"
path = "challenge_nine_sample_ts1_input.txt"

def fct(N):
    sum = 0
    to_str = str(N)
    length = len(to_str)
    for letter in to_str:
        sum += int(letter)
    
    sum %= 9
    nb_to_add = 9 - sum

    i = 0
    while i < length:
        if nb_to_add >= int(to_str[i]):
            i += 1
        else:
            break 
        
    res = to_str[0:i] + str(nb_to_add) + to_str[i:]
    res = int(res)

    return res

with open(folder_name + path, "r") as f:
    T = int(f.readline())
    final_str = ""
    for i in range(1, T+1):
        N = int(f.readline())
        res = fct(N)
        final_str += "Case #{}: {}".format(i, res)
        final_str += '\n'
    final_str = final_str[:-1]

with open(folder_name + "res_" + path, "w") as f:
    f.write(final_str)

