
AB = float(input("Enter the length of side AB: "))
BC = float(input("Enter the length of side BC: "))
CD = float(input("Enter the length of side CD: "))
DA = float(input("Enter the length of side DA: "))
I = float(input("Enter the measure of the internal angle I: "))


if AB == BC == CD == DA:
    if I == 90:
        shape = "square"
    else:
        shape = "rhombus"
elif AB == CD and BC == DA:
    if I == 90:
        shape = "rectangle"
    else:
        shape = "parallelogram"
else:
    shape = "irregular quadrilateral"

print("The quadrilateral is a", shape)

