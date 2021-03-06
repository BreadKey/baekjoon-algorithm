from linear_data_structure import trapping_rain_water

assert(trapping_rain_water.calculate(
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6)

assert(trapping_rain_water.calculate([2, 1, 0, 1]) == 1)
assert(trapping_rain_water.calculate([1, 0, 1, 2]) == 1)
assert(trapping_rain_water.calculate([3, 2, 1, 0, 1, 2]) == 4)
assert(trapping_rain_water.calculate([3, 2, 1, 0, 2, 2]) == 3)
assert(trapping_rain_water.calculate([2, 1, 0]) == 0)
assert(trapping_rain_water.calculate([0, 1, 2]) == 0)