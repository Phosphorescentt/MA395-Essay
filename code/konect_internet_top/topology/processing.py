with open("out.topology", "r") as f:
    lines = f.readlines()

with open("out2.topology", "w") as f:
    for line in lines:
        data = line.split(" ")
        if int(data[3]) > 1267900000:
            f.write(f"{data[0]} {data[1]} \n")
