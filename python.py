import math

vectors = [[-10, 20, -10, -18],
           [-10, 20, 0, 3],
           [0, 3, 8, 7],
           [8, 17, 10, -16],
           [16, -16, -10, -18]]

for i, vector in enumerate(vectors):
    length = math.sqrt(sum([x**2 for x in vector]))
    if vector[0] == 0:
        slope = 'NA'
    else:
        slope = (vector[1] - vector[0]) / length
    print(f"Vector{i+1} length={length:.1f} slop={slope}")

y_values = [x[1] for x in vectors]
y_max = max(y_values)
y_min = min(y_values)
print(f"Y max={y_max} Y min={y_min}")




