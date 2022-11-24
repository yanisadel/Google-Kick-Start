folder_name = ""
path = ""

def fct():
    return 1

with open(folder_name + path, "r") as f:
    T = int(f.readline())
    final_str = ""
    for i in range(1, T+1):
        N = f.readline()
        res = fct()
        
        final_str += "Case #{}: {}".format(i, res)
        final_str += '\n'
    final_str = final_str[:-1]

with open(folder_name + "res_" + path, "w") as f:
    f.write(final_str)
