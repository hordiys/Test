def generate_line_data(x_left_interv, step, points_count, koef):
    k = koef[0]
    b = koef[1]

    x = list()
    y = list()

    for point_number in range(0, points_count):
        point_x = x_left_interv + step * point_number
        point_y = a * point_x ** 2 + b

        x.append(point_x)
        y.append(point_y)
    return {'x_data': x, 'y_data': y}