# remember that one is throwing away money,
# the other is value at the end of years

years = 30
rent_per_month = 1100
rent_utility = 100
save_per_month = 1000
saved_for_dp = 5000
initial_price = 350000

mor_ins = .01
mor_int = .045
prop_tax = .0079
house_utility = 400
house_ins = 300

# percent income for morgage payment
qualify = .33

month = 0
spent = 0


def getHouseCost(dp):
  remaining = initial_price - dp
  cost = 0
  h_month = 0
  while h_month < years * 12:
    if remaining == 0:
      pass
    h_month += 1
    # roughly equates to monthly payment
    cost += remaining/years/12 + (remaining * mor_int)/12
    # if morg insurance needed
    if remaining > 0:
      if dp/remaining < .2:
        cost += (remaining * mor_ins)/12

      remaining -= remaining/years/12

    # property tax
    cost += (initial_price * prop_tax)/12

    # house utility
    cost += house_utility

    # maintainance
    cost += (initial_price * .01)/12

    # normal insurance
    cost += house_ins

  return cost

# find min in this when done
costs = []
dps = []

while month < years * 12:
  month += 1
  spent += rent_per_month + rent_utility + save_per_month
  saved_for_dp += save_per_month
  dps.append(saved_for_dp)
  costs.append(spent + getHouseCost(saved_for_dp))
print("Months to save: {}".format(costs.index(min(costs)) + 1))
total = min(costs)
print("Including ALL variables, i.e. morgage, taxes, insurance, maint.")
print()
print("min possible: {}".format(total))
print("min monthly expense: {}".format(total/years/12))
print("max possible (worst timing): {}".format(max(costs)))
print("max monthly expense: {}".format(max(costs)/years/12))
print("down payment for best: {}".format(dps[costs.index(total)]))
print()
print("The following is an overestimate (by a little) but a good estimate:")
print()
print("Needed yearly income (best): {}".format(total/years * 3))
print("Needed yearly income (worst): {}".format(max(costs)/years * 3))
