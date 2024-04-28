length, breath, height = map(int, input("Enter length, breath, and height separated by spaces: ").split())

lateral_surface_area = 2 * (length + breath) * height  

total_surface_area = 2 * (length * breath + breath * height + length * height) 

print("Lateral Surface Area:", lateral_surface_area)
print("Total Surface Area:", total_surface_area)

