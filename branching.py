def classify_num(n: int) -> str:
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    if n > 0:
        return "positive"

for n in range(-30, 30):
    print(classify_num(n))




assert classify_num(-2) == "negative"
assert classify_num(0) == "zero"
assert classify_num(3) == "positive"
print("OK: classify_num")