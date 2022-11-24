path = "speed_typing_sample_ts1_input.txt"

def fct(I, P):
    n = len(I)
    p = len(P)
    if p < n:
        return "IMPOSSIBLE"

    else:
        counter = 0
        j = 0
        i = 0
        while i < p and j < n:
            while i < p and P[i] != I[j]:
                counter += 1
                i += 1
            j += 1
            i += 1

        if j == n:
            return counter
        else:
            return "IMPOSSIBLE"


with open(path, "r") as f:
    T = int(f.readline())
    final_str = ""
    for i in range(1, T+1):
        I = f.readline()
        P = f.readline()
        res = fct(I, P)
        final_str += "Case #{}: {}".format(i, res)
        final_str += '\n'
    final_str = final_str[:-1]

with open("res_" + path, "w") as f:
    f.write(final_str)
