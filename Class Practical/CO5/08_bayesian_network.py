"""Tiny Bayesian network: Rain -> WetGrass, Sprinkler -> WetGrass.
Enumerates the joint distribution for the evidence WetGrass=True.
"""
P_RAIN = 0.2
P_SPRINKLER = 0.3
# P(WetGrass=True | Rain, Sprinkler)
P_WET = {
    (True, True): .99, (True, False): .90,
    (False, True): .80, (False, False): .01
}
def joint(rain, sprinkler, wet):
    pr = P_RAIN if rain else 1-P_RAIN
    ps = P_SPRINKLER if sprinkler else 1-P_SPRINKLER
    pw = P_WET[(rain, sprinkler)] if wet else 1-P_WET[(rain, sprinkler)]
    return pr * ps * pw

evidence = sum(joint(r, s, True) for r in (False, True) for s in (False, True))
numerator = sum(joint(True, s, True) for s in (False, True))
print("P(Rain=True | WetGrass=True) =", numerator / evidence)
