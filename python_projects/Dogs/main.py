import numpy as np
import fetchmaker
from scipy.stats import binom_test, f_oneway, chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

rottweiler_tl = fetchmaker.get_tail_length('rottweiler')
# print(rottweiler_tl)
# print(np.std(rottweiler_tl))

whippet_rescue = fetchmaker.is_rescue('whippet')
# print(whippet_rescue)
num_whippet_rescues = np.count_nonzero(whippet_rescue)
# print(num_whippet_rescues)
num_whippets = np.size(whippet_rescue)
# print(num_whippets)
pval_w = binom_test(num_whippet_rescues, num_whippets, 0.08)
# print(pval_w)
whippet, terrier, pitbull = fetchmaker.get_tail_length('whippet'), fetchmaker.get_tail_length('terrier'), fetchmaker.get_tail_length('pitbull')

midsize = f_oneway(whippet, terrier, pitbull)
# print(midsize.pvalue)
midsize_dif = pairwise_tukeyhsd(np.concatenate([whippet, terrier, pitbull]), np.concatenate([['whippet']*len(whippet), ['terrier']*len(whippet),['pitbull']*len(whippet)]))
# print(midsize_dif)

poodle_colors = fetchmaker.get_color('poodle')
shihtzu_colors = fetchmaker.get_color('shihtzu')

color_table = [
  [np.count_nonzero(poodle_colors == "black"), np.count_nonzero(shihtzu_colors == "black")],
  [np.count_nonzero(poodle_colors == "brown"), np.count_nonzero(shihtzu_colors == "brown")],
  [np.count_nonzero(poodle_colors == "gold"), np.count_nonzero(shihtzu_colors == "gold")],
  [np.count_nonzero(poodle_colors == "grey"), np.count_nonzero(shihtzu_colors == "grey")],
  [np.count_nonzero(poodle_colors == "white"), np.count_nonzero(shihtzu_colors == "white")]
  ]

print(color_table)

chi2 = chi2_contingency(color_table)

for elem in chi2:
  print(elem, '\n')











