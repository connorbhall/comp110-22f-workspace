"""A tracing challenge question."""



i: int = 0
s: str = ""

while i <= 6:
    if i % 2 == 0:
        s = s + "h"
    else: 
        if i % 3 == 0:
            s = s + "!"
        else:
            s = s + "e"
    i = i + 1

print(s)