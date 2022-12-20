def cal(n):
    sum = 0
    lv1 = 1678  # 0 to 50kwh
    lv2 = 1734  # 51 to 100kwh
    lv3 = 2014  # 101 to 200kwh
    lv4 = 2536  # 201 to 300kwh
    lv5 = 2834  # 301 to 400kwh
    lv6 = 292  # 401 more
    sum=0
    if n <= 50:
        sum += n * lv1
    elif n <= 101:
        sum += 50 * lv1 + (n - 50) * lv2
    elif n <= 200:
        sum += 50 * lv1 + 50 * lv2 + (n - 100) * lv3
    elif n <= 300:
        sum += 50 * lv1 + 50 * lv2 + 100 * lv3 + (n - 200) * lv4
    elif n <= 400:
        sum += 50 * lv1 + 50 * lv2 + 100 * lv3 + 100 * lv4 + (n - 400) * lv5
    else:
        sum += 50 * lv1 + 50 * lv2 + 100 * lv3 + 100 * lv4 + lv5 * 100 + (n - 400) * lv6
    return sum
student = {"name": "Duc Nam", "age": "23", "adr": "Tuyen Qunang", "ps": 312} #ps: Power consumption (KWH)
n=int(student['ps'])
st = str(cal(n))
student ['tad']= st #Total amount due (VND)
print(student)