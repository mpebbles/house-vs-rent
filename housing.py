# remember that one is throwing away money,
# the other is value at the end of years

years = 30
rent_per_month = 1500
rent_utility = 100
save_per_month = 1000
saved_for_dp = 5000
initial_price = 300000

# add closing cost to overall price
closing_cost = .05
initial_price += initial_price * closing_cost


mor_ins = .01
mor_int = .045
prop_tax = .0079
house_utility = 400
hoa = 300
house_ins = 300


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
    # if mortg insurance needed
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

    # HOA fee
    cost += hoa

  return cost

# find min in this when done
costs = []
dps = []
hcs = []

while month < years * 12:
  month += 1
  spent += rent_per_month + rent_utility + save_per_month
  saved_for_dp += save_per_month
  dps.append(saved_for_dp)
  hc = getHouseCost(saved_for_dp)
  costs.append(spent + hc)
  hcs.append(hc)

print("***********************************************************")
print("Months to save: {}".format(costs.index(min(costs)) + 1))
print("Including ALL variables, i.e. mortgage, taxes, insurance, maint.")
print()
print("min $ spent possible to pay off house: {}".format(min(costs)))
idx_min = costs.index(min(costs))
print("min monthly expense of house: {}".format(min(hcs)/years/12))
idx_max = costs.index(max(costs))
print("max $ spent possible to pay off house: {}".format(costs[idx_max]))
print("max monthly expense of house: {}".format(max(hcs)/years/12))
print("down payment for best: {}".format(dps[idx_min]))
print()
print("Assuming monthly income must be 3x the mortgage payment:")
year = 0
price_and_mort = initial_price - dps[idx_min]
while year < years:
  price_and_mort += (initial_price - dps[idx_min]) * mor_int
  year += 1
print("min yearly income needed (best time to buy): {}".format(price_and_mort/years * 3))

year = 0
price_and_mort = initial_price
while year < years:
  price_and_mort += initial_price * mor_int
  year += 1
print("max yearly income needed (worse time to buy): {}".format(price_and_mort/years * 3))
