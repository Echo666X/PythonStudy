days = int(input())

up_skill = 1.0
for _ in range(days):
    up_skill *= 1.005

down_skill = 1.0
for _ in range(days):
    down_skill *= 0.999

diff = round(up_skill - down_skill, 2)

print("{:.2f} - {:.2f} = {:.2f}".format(up_skill, down_skill, diff))
