def get_th(raw, th):
    initial = raw.split(",")
    history = {int(a): i for i, a in enumerate(initial)}
    last_num = initial[-1]
    last_k = len(initial) - 1
    for k in range(len(history), th):
        if last_num in history:
            new_num = last_k - history[last_num]
        else:
            new_num = 0
        history[last_num] = k-1
        last_num = new_num
        last_k = k
        if k % 300000 == 0:
            print(k)
    return last_num


if __name__ == '__main__':
    print("436=", get_th("0,3,6", 2020))
    print("1=", get_th("1,3,2", 2020))
    print("10=", get_th("2,1,3", 2020))
    print("27=", get_th("1,2,3", 2020))
    print("78=", get_th("2,3,1", 2020))
    print("438=", get_th("3,2,1", 2020))
    print("1836=", get_th("3,1,2", 2020))
    print("?(2020)=", get_th("14,8,16,0,1,17", 2020))
    print("?(30000000)=", get_th("14,8,16,0,1,17", 30000000))
