# GROWING = 1
# SHRINKING = -1
#
#
# def print_rhombus(n: int):
#     def print_line(i: int, direction: int):
#         if i == 0:
#             return
#         line = " " * (n - i) + "* " * i
#         print(line.rstrip())
#         if i == n:
#             direction = SHRINKING
#         print_line(i + direction, direction)
#     print_line(1, GROWING)


#print_rhombus(int(input()))


def print_line(size, stars):
    for line in range(size - stars):
        print(" ", end="")
    for line in range(1, stars):
        print("*", end=" ")
    print("*")


size = int(input())
for star_count in range(1, size):
    print_line(size, star_count)
for star_count in range(size, 0, -1):
    print_line(size, star_count)
