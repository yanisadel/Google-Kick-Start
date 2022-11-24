folder_name = "Palindrome Free Strings/"
path = "palindrome_free_strings_sample_ts1.txt"

def fct(S, length):
    return "POSSIBLE"

with open(folder_name + path, "r") as f:
    T = int(f.readline())
    final_str = ""
    for i in range(1, T+1):
        length = int(f.readline())
        S = f.readline()
        res = fct(S, length)
        
        final_str += "Case #{}: {}".format(i, res)
        final_str += '\n'
    final_str = final_str[:-1]

with open(folder_name + "res_" + path, "w") as f:
    f.write(final_str)
