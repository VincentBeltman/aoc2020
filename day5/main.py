import math


def get_row_nr(raw_seat):
    upper_limit = 127
    bottom_limit = 0
    for i in range(0, 7):
        diff = upper_limit - bottom_limit
        if raw_seat[i] == "B":
            bottom_limit += math.floor((diff+1) / 2)
        else:
            upper_limit -= math.floor((diff+1) / 2)
    assert(upper_limit == bottom_limit)
    return upper_limit


def get_seat_nr(raw_seat):
    upper_limit = 7
    bottom_limit = 0
    for i in range(0, 3):
        diff = upper_limit - bottom_limit
        if raw_seat[i] == "R":
            bottom_limit += math.floor((diff+1) / 2)
        else:
            upper_limit -= math.floor((diff+1) / 2)
    assert(upper_limit == bottom_limit)
    return upper_limit


def parse_seats(raw_seats):
    result = []
    for raw_seat in raw_seats:
        row_nr = get_row_nr(raw_seat)
        seat_nr = get_seat_nr(raw_seat[-3:])
        result.append({"row": row_nr, "seat": seat_nr, "seat_id": row_nr * 8 + seat_nr})

    return result


def part_1(parsed_seats):
    biggest_seat_id = 0
    for seat in seats:
        biggest_seat_id = max(seat["seat_id"], biggest_seat_id)
    print("Biggest seat ID:", biggest_seat_id)


def part_2(parsed_seats):
    seats_sorted = sorted(parsed_seats, key=lambda k: k["seat_id"])
    seat_ids = [seat["seat_id"] for seat in seats_sorted]
    prev_seat_id = seat_ids[0]
    for seat_id in seat_ids:
        if seat_id - prev_seat_id > 1:
            print(prev_seat_id, seat_id, seat_id - 1)
            # break
        prev_seat_id = seat_id


if __name__ == '__main__':
    with open("test2.txt") as file:
        seats = parse_seats(file.read().splitlines())
        part_1(seats)
        part_2(seats)
