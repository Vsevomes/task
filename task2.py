slovo = "КРИНЖ"
counter = 0
for x1 in slovo:
    for x2 in slovo:
        for x3 in slovo:
            for x4 in slovo:
                for x5 in slovo:
                    word = x1 + x2 + x3 + x4 + x5
                    if word.count("Ж") == 1 and word.count("РИ") == 0 and word.count("ИР") == 0:
                        counter += 1
print(counter)
