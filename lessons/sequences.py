"""Notes and examples of tuple and range sequence types."""

#Declaring a type alias that "invents" the Point2D type.
Point2D = tuple[float, float]

start_position: Point2D = (5.0, 10.0)
start_position = (start_position[0] + 5.0, start_position[1] + 10.0)
end_position: Point2D = (99.0, 99.0)
print(start_position)

#tuples, because they are a sequence, are 0 - indexed.
print(start_position[0])

for item in end_position:
    print(item)

print(len(end_position))


#examples of range
a_range: range = range(0, 10, 1)
#access its items
print(a_range[0])
print(a_range[1])
print(len(a_range))

for i in a_range:
    print(i)