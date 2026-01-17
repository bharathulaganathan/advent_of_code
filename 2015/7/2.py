import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

calcs = {}

with open(file_path, "r") as input:
    for row in input:
        expression, value = row.split(" -> ")
        calcs[value.strip()] = expression

calcs_copy = {}
for calc in calcs:
    calcs_copy[calc] = calcs[calc]

to_eval = "a"
override = "b"

def eval(unknown):
    try:
        return int(unknown)
    except:
        pass
    exps = calcs[unknown]
    try:
        x = int(exps)
        calcs[unknown] = x
        return x
    except:
        pass
    if "AND" in exps:
        l, r = exps.split(" AND ")
        x = eval(l) & eval(r)
    elif "OR" in exps:
        l, r = exps.split(" OR ")
        x = eval(l) | eval(r)
    elif "LSHIFT" in exps:
        l, r = exps.split(" LSHIFT ")
        x = eval(l) << int(r)
    elif "RSHIFT" in exps:
        l, r = exps.split(" RSHIFT ")
        x = eval(l) >> int(r)
    elif "NOT" in exps:
        l, r = exps.split("NOT ")
        x = 2**16 + ~(eval(r))
    else:
        x = eval(exps)
    calcs[unknown] = x
    return x


answer_1 = eval(to_eval)
calcs = {}
for calc in calcs_copy:
    calcs[calc] = calcs_copy[calc]
calcs[override] = answer_1
answer_2 = eval(to_eval)

print(answer_2)