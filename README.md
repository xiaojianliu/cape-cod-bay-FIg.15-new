# backtrack turtle 

# '2012ux.np' creates files ( '2012windu.npy'/'2012numu.npy'/'2012xxu.npy'/'2012yyu.npy').
 After the temperature below 10 degC, I calculate the number of strandings every 3 days and save as '2012numu.npy'( stranding in 'Outer Cape' towns) and '2012numv.npy'( stranding in 'Mid Cape' towns), and I also calculate the sum of wind stress every 3 days (the time is consistent with the stranding time ) save as '2012windu.npy' (wind stress in the east-west direction) and '2012windv.npy'  (wind stress in the south-north direction).
   Next I calculate their correlation coefficient and perform a linear fit. "2012xxu.npy"（in the east-west direction） and '2012xxv.npy'（in the south-north direction） save the fitted x-axis data. "2012yyu.npy"（in the east-west direction） and '2012yyv.npy'（in the south-north direction） save the fitted y-axis data.
# 'pltx.np' draw a picture about linear fit
