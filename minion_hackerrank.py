def minion_game(string):
    lol=["A","E","I","O","U"]
    vo=[k for k in range(len(string)) if string[k] in lol]
    nvo=[j for j in range(len(string)) if string[j] not in lol]
    kev=sum(len(string)-k for k in vo)
    stu=sum(len(string)-k for k in nvo)
    if stu>kev:
        print("Stuart", stu)
    elif kev>stu:
        print("Kevin", kev)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
