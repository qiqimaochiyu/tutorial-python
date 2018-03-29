"""
The key is 3 states and 5 edges for state transition. 3 states are notHold (stock), hold (stock), and notHold_cooldown. The initial values of the latter two are negative infinity since they are meaningless, i.e. you won’t hold stocks at first and there’s no cooldown at first. The 5 edges:

hold -----do nothing----->hold

hold -----sell----->notHold_cooldown

notHold -----do nothing -----> notHold

notHold -----buy-----> hold

notHold_cooldown -----do nothing----->notHold
"""
def maxProfit(self, prices):
    notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
    for p in prices:
        hold, notHold, notHold_cooldown = max(hold, notHold - p), max(notHold, notHold_cooldown), hold + p
    return max(notHold, notHold_cooldown)
