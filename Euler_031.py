Money = [1, 2, 5, 10, 20, 50, 100, 200]

for onep in range(0, 201):
    for twop in range(0, 101):
        for fivep in range(0, 41):
            for tenp in range(0, 21):
                for twentyp in range(0, 11):
                    for fiftyp in range(0, 5):
                        for hunderdp in range(0, 3):
                            for twohunderdp in range(0, 2):
                                Total = onep * Money[0] + \
                                        twop * Money[1] + \
                                        fivep * Money[2] + \
                                        tenp * Money[3] + \
                                        twentyp * Money[4] + \
                                        fiftyp * Money[5] + \
                                        hunderdp * Money[6] + \
                                        twohunderdp * Money[7]
