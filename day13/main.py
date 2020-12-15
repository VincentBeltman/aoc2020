def part_1(blob):
    arrival_time, busses_raw = blob.splitlines()
    arrival_time = int(arrival_time)
    busses = [int(bus) for bus in busses_raw.split(",") if bus != "x"]
    smallest_diff = 4294967296
    soonest_bus = 0
    for bus in busses:
        minutes_until_arrival = bus - arrival_time % bus
        if minutes_until_arrival < smallest_diff:
            smallest_diff = minutes_until_arrival
            soonest_bus = bus
    print(smallest_diff, soonest_bus, smallest_diff * soonest_bus)


def part_2(blob):
    busses = [{"index": i, "bus": int(bus)} for i, bus in enumerate(blob.split(",")) if bus != "x"]
    step_size = busses[0]["bus"]
    soonest_timestamp = 0
    for i in range(1, len(busses)):
        while (soonest_timestamp + busses[i]["index"]) % busses[i]["bus"] > 0:
            soonest_timestamp += step_size
        step_size *= busses[i]["bus"]
    print(soonest_timestamp)


if __name__ == '__main__':
    # with open("test2.txt") as file:
        # part_1(file.read())
    part_2("7,13,x,x,59,x,31,19")
    part_2("17,x,13,19")
    part_2("67,7,59,61")
    part_2("67,x,7,59,61")
    part_2("67,7,x,59,61")
    part_2("1789,37,47,1889")
    part_2("19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,743,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,643,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23")
