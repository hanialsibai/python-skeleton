# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  anwer = 0
  for i in range(len(portfolios)):
      for j in range(len(portfolios)):
        if i == j:
            continue
        else:
            if portfolios[i]^portfolios[j] > answer:
                answer = portfolios[i]^portfolios[j]
  return answer
