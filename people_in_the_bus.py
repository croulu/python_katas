def people_in_the_bus(bus_stops):
    index = 0
    sum_final = 0

    while index < len(bus_stops):
        sum_final += pay_stop(bus_stops[index])
        index += 1

    return sum_final


def pay_stop(in_out):
    people_in = in_out[0]
    people_out = in_out[1]

    return people_in - people_out
