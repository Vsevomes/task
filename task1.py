slovo = "КЕФТМ"
k = 0
for x1 in slovo:
    for x2 in slovo:
        for x3 in slovo:
            for x4 in slovo:
                for x5 in slovo:
                    for x6 in slovo:
                        for x7 in slovo:
                            name = x1 + x2 + x3 + x4 + x5 + x6 + x7
                            k += 1
                            if name == "КЕФТЕМЕ":
                                print(k)
                                exit()
