from advent.day_1 import fuel_eq, fuel_eq_iterative, load_mass

mass = load_mass('data/day_1/data.txt')
fuel = fuel_eq(mass)
print(fuel.sum())
fuel_iter = fuel_eq_iterative(mass)
print(fuel_iter.sum())
