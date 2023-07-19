slovo = "012345"
counter = 0
for x1 in slovo:
    for x2 in slovo:
        for x3 in slovo:
            for x4 in slovo:
                for x5 in slovo:
                    for x6 in slovo:
                        word = x1 + x2 + x3 + x4 + x5 + x6
                        if (int(x2) + int(x4) + int(x6)) > (int(x1) + int(x3) + int(x5)):
                            counter += 1
print(counter)
