import pandas as pd
from bayesnet import BayesNet, BayesNode

def makeCancerNet():
	df = pd.read_csv('Cancer_data.csv')


	bn = BayesNet()

	total = len(df)

	# P(Age)
	# Add a BayesNode associated with Age to bn following P(Genes) example below
	# calculate P(Age > 55)
	condition = df['Age'] > 55

	subsize = len(df[condition])

	
	subsize_probability = subsize / total
	bn.add(BayesNode('Age',None,(True,False),{'':{True:subsize_probability,False:1-subsize_probability}}))

	# P(Genes)

	gen_r = df['Genes'] == 'T'

	gensize = len(df[gen_r])

	
	gen_probability = gensize / total
	bn.add(BayesNode('Genes',None,(True,False),{'':{True:gen_probability,False:1-gen_probability}}))

	# P(Cancer| Age, Genes)
	# Add a BayesNode associated with Cancer given Age and Genes to bn
	# calculate P(Cancer | Age, Genes)
	# calculate P(Cancer | Age, ¬Genes)
	# calculate P(Cancer | ¬Age, Genes)
	# calculate P(Cancer | ¬Age, ¬Genes)

	### Add your code here

	both_r = (df['Genes'] == 'F') & (df['Age'] <= 55)
	both_df = df[both_r]
	both_size = len(both_df)

	cancer_rule = both_df['Cancer'] == 'T'
	cancer = len(both_df[cancer_rule])
	cancer_tff = cancer / both_size



	both_r = (df['Genes'] == 'F') & (df['Age'] > 55)
	both_df = df[both_r]
	both_size = len(both_df)

	cancer_rule = both_df['Cancer'] == 'T'
	cancer = len(both_df[cancer_rule])
	cancer_ttf = cancer / both_size


	both_r = (df['Genes'] == 'T') & (df['Age'] > 55)
	both_df = df[both_r]
	both_size = len(both_df)

	cancer_rule = both_df['Cancer'] == 'T'
	cancer = len(both_df[cancer_rule])
	cancer_ttt = cancer/both_size

	

	both_r = (df['Genes'] == 'T') & (df['Age'] <= 55)
	both_df = df[both_r]
	both_size = len(both_df)

	cancer_rule = both_df['Cancer'] == 'T'
	cancer = len(both_df[cancer_rule])
	cancer_tft = cancer / both_size

	


	bn.add(BayesNode('Cancer', ['Age', 'Genes'], (True, False), 
	{
		(False, False): {True:cancer_tff, False:1-cancer_tff},

		(True, False): {True:cancer_ttf, False:1-cancer_ttf},
		(False, True): {True:cancer_tft, False:1-cancer_tft},
		
		(True,True):{True:cancer_ttt,False:1-cancer_ttt},
	}
	))




	# P(Test | Cancer)
	# Add a BayesNode associated with Test given Cancer to bn
	# calculate P(Test | Cancer)
	# calculate P(Test | ¬Cancer)


	### Add your code here
	can_r = df['Cancer'] == 'T'
	can_df = df[can_r]
	can_size = len(can_df)

	te_rule = can_df['Test'] == 'P'
	te_size = len(can_df[te_rule])
	t_t = te_size/can_size

	can_r = df['Cancer'] == 'F'
	can_df = df[can_r]
	can_size = len(can_df)

	te_rule = can_df['Test'] == 'P'
	te_size = len(can_df[te_rule])
	t_f = te_size/can_size


	bn.add(BayesNode('Test',['Cancer'],('Positive','Negative'),
	{
		True:{'Positive':t_t,'Negative':1-t_t},
		False:{'Positive':t_f,'Negative':1-t_f}
	}))



	# P(Treatment | Test)
	test_rule = df['Test'] == 'P'
	df_test = df[test_rule]
	test = len(df_test)
	trtmt_rule = df_test['Treatment'] == 'T'
	trtmt = len(df_test[trtmt_rule])
	trtmt_p = trtmt / test

	test_rule = df['Test'] == 'N'
	df_test = df[test_rule]
	test = len(df_test)
	trtmt_rule = df_test['Treatment'] == 'T'
	trtmt = len(df_test[trtmt_rule])
	trtmt_n = trtmt / test

	bn.add(BayesNode('Treatment',['Test'], (True,False), 
	{
		'Positive':{True:trtmt_p,False:1-trtmt_p},
		'Negative':{True:trtmt_n,False:1-trtmt_n}
		
	}))

	# P(Prognosis | Age, Test, Treatment)
	# Add a BayesNode associated with Prognosis given Age, Test, and Treatment to bn
	# calculate P(Prognosis == 1 | Age, Test, Treatment)
	# calculate P(Prognosis == 1 | Age, Test, ~Treatment)
	# calculate P(Prognosis == 1 | Age, ~Test, Treatment)
	# calculate P(Prognosis == 1 | Age, ~Test, ~Treatment)
	# calculate P(Prognosis == 1 | ~Age, Test, Treatment)
	# calculate P(Prognosis == 1 | ~Age, Test, ~Treatment)
	# calculate P(Prognosis == 1 | ~Age, ~Test, Treatment)
	# calculate P(Prognosis == 1 | ~Age, ~Test, ~Treatment)
	# calculate P(Prognosis == 3 | Age, Test, Treatment)
	# calculate P(Prognosis == 3 | Age, Test, ~Treatment)
	# calculate P(Prognosis == 3 | Age, ~Test, Treatment)
	# calculate P(Prognosis == 3 | Age, ~Test, ~Treatment)
	# calculate P(Prognosis == 3 | ~Age, Test, Treatment)
	# calculate P(Prognosis == 3 | ~Age, Test, ~Treatment)
	# calculate P(Prognosis == 3 | ~Age, ~Test, Treatment)
	# calculate P(Prognosis == 3 | ~Age, ~Test, ~Treatment)
	# calculate P(Prognosis == 5 | Age, Test, Treatment)
	# calculate P(Prognosis == 5 | Age, Test, ~Treatment)
	# calculate P(Prognosis == 5 | Age, ~Test, Treatment)
	# calculate P(Prognosis == 5 | Age, ~Test, ~Treatment)
	# calculate P(Prognosis == 5 | ~Age, Test, Treatment)
	# calculate P(Prognosis == 5 | ~Age, Test, ~Treatment)
	# calculate P(Prognosis == 5 | ~Age, ~Test, Treatment)
	# calculate P(Prognosis == 5 | ~Age, ~Test, ~Treatment)
	### Add your code here

	#Prog1

	att_r = (df['Age'] > 55) & (df['Test'] == 'N') & (df['Treatment'] == 'T')
	att_df = df[att_r]
	att_size= len(att_df)

	prog_r = att_df['Prognosis'] == 1
	prognosis_size  = len(att_df[prog_r])
	prog1_tft = prognosis_size  / att_size




	att_r = (df['Age'] > 55) & (df['Test'] == 'P') & (df['Treatment'] == 'F')
	att_df = df[att_r]
	att_size= len(att_df)

	prog_r = att_df['Prognosis'] == 1
	prognosis_size  = len(att_df[prog_r])
	prog1_ttf = prognosis_size  / att_size


	
	att_r = (df['Age'] <= 55) & (df['Test'] == 'P') & (df['Treatment'] == 'F')
	att_df = df[att_r]
	att_size = len(att_df)

	prog_r = att_df['Prognosis'] == 1
	prognosis_size  = len(att_df[prog_r])
	prog1_ftf = prognosis_size  / att_size



	att_r = (df['Age'] <= 55) & (df['Test'] == 'N') & (df['Treatment'] == 'T')
	att_df = df[att_r]
	att_size = len(att_df)

	prog_r = att_df['Prognosis'] == 1
	prognosis_size  = len(att_df[prog_r])
	prog1_fft = prognosis_size  / att_size

	att_r = (df['Age'] <= 55) & (df['Test'] == 'N') & (df['Treatment'] == 'F')
	att_df = df[att_r]
	att_size = len(att_df)

	prog_r = att_df['Prognosis'] == 1
	prognosis_size  = len(att_df[prog_r])
	prog1_fff = prognosis_size  / att_size

	
	att_r = (df['Age'] <= 55) & (df['Test'] == 'P') & (df['Treatment'] == 'T')
	att_df = df[att_r]
	att_size = len(att_df)

	prog_r = att_df['Prognosis'] == 1
	prognosis_size  = len(att_df[prog_r])
	prog1_ftt = prognosis_size  / att_size



	att_r = (df['Age'] > 55) & (df['Test'] == 'N') & (df['Treatment'] == 'F')
	att_df = df[att_r]
	att_size = len(att_df)

	prog_r = att_df['Prognosis'] == 1
	prognosis_size = len(att_df[prog_r])
	prog1_tff = prognosis_size  / att_size


	att_r = (df['Age'] > 55) & (df['Test'] == 'P') & (df['Treatment'] == 'T')
	att_df = df[att_r]
	att_size= len(att_df)

	prog_r = att_df['Prognosis'] == 1
	prognosis_size  = len(att_df[prog_r])
	prog1_ttt = prognosis_size  / att_size


	#Prog3


	att_r = (df['Age'] <= 55) & (df['Test'] == 'N') & (df['Treatment'] == 'F')
	att_df = df[att_r]
	att_size = len(att_df)

	prog_r = att_df['Prognosis'] == 3
	prognosis_size  = len(att_df[prog_r])
	prog3_fff = prognosis_size  / att_size


	att_r = (df['Age'] > 55) & (df['Test'] == 'P') & (df['Treatment'] == 'F')
	att_df = df[att_r]
	att_size = len(att_df)

	prog_r = att_df['Prognosis'] == 3
	prognosis_size  = len(att_df[prog_r])
	prog3_ttf = prognosis_size  / att_size
	

	att_r = (df['Age'] > 55) & (df['Test'] == 'N') & (df['Treatment'] == 'T')
	att_df = df[att_r]
	att_size = len(att_df)

	prog_r = att_df['Prognosis'] == 3
	prognosis_size  = len(att_df[prog_r])
	prog3_tft = prognosis_size  / att_size
	


	att_r = (df['Age'] <= 55) & (df['Test'] == 'P') & (df['Treatment'] == 'T')
	att_df = df[att_r]
	att_size = len(att_df)

	prog_r = att_df['Prognosis'] == 3
	prognosis_size  = len(att_df[prog_r])
	prog3_ftt = prognosis_size  / att_size
	
	att_r = (df['Age'] > 55) & (df['Test'] == 'P') & (df['Treatment'] == 'T')
	att_df = df[att_r]
	att_size = len(att_df)

	prog_r = att_df['Prognosis'] == 3
	prognosis_size  = len(att_df[prog_r])
	prog3_ttt = prognosis_size  / att_size


	att_r = (df['Age'] <= 55) & (df['Test'] == 'N') & (df['Treatment'] == 'T')
	att_df = df[att_r]
	att_size = len(att_df)

	prog_r = att_df['Prognosis'] == 3
	prognosis_size  = len(att_df[prog_r])
	prog3_fft = prognosis_size  / att_size

	att_r = (df['Age'] <= 55) & (df['Test'] == 'P') & (df['Treatment'] == 'F')
	att_df = df[att_r]
	att_size = len(att_df)

	prog_r = att_df['Prognosis'] == 3
	prognosis_size  = len(att_df[prog_r])
	prog3_ftf = prognosis_size  / att_size


	att_r = (df['Age'] > 55) & (df['Test'] == 'N') & (df['Treatment'] == 'F')
	att_df = df[att_r]
	att_size = len(att_df)

	prog_r = att_df['Prognosis'] == 3
	prognosis_size  = len(att_df[prog_r])
	prog3_tff = prognosis_size  / att_size

	#Prog5
	att_r = (df['Age'] > 55) & (df['Test'] == 'N') & (df['Treatment'] == 'F')
	att_df = df[att_r]
	att_size = len(att_df)

	prog_r = att_df['Prognosis'] == 5
	prognosis_size  = len(att_df[prog_r])
	prog5_tff = prognosis_size  / att_size

	att_r = (df['Age'] > 55) & (df['Test'] == 'P') & (df['Treatment'] == 'F')
	att_df = df[att_r]
	att_size = len(att_df)

	prog_r = att_df['Prognosis'] == 5
	prognosis_size  = len(att_df[prog_r])
	prog5_ttf = prognosis_size  / att_size

	att_r = (df['Age'] <= 55) & (df['Test'] == 'P') & (df['Treatment'] == 'T')
	att_df = df[att_r]
	att_size = len(att_df)
	prog_r = att_df['Prognosis'] == 5
	prognosis_size  = len(att_df[prog_r])
	prog5_ftt = prognosis_size  / att_size

	att_r = (df['Age'] <= 55) & (df['Test'] == 'P') & (df['Treatment'] == 'F')
	att_df = df[att_r]
	att_size = len(att_df)

	prog_r = att_df['Prognosis'] == 5
	prognosis_size  = len(att_df[prog_r])
	prog5_ftf = prognosis_size  / att_size

	att_r = (df['Age'] > 55) & (df['Test'] == 'N') & (df['Treatment'] == 'T')
	att_df = df[att_r]
	att_size = len(att_df)

	prog_r = att_df['Prognosis'] == 5
	prognosis_size  = len(att_df[prog_r])
	prog5_tft = prognosis_size  / att_size

	att_r = (df['Age'] > 55) & (df['Test'] == 'P') & (df['Treatment'] == 'T')
	att_df = df[att_r]
	att_size = len(att_df)

	prog_r = att_df['Prognosis'] == 5
	prognosis_size  = len(att_df[prog_r])
	prog5_ttt = prognosis_size  / att_size



	att_r = (df['Age'] <= 55) & (df['Test'] == 'N') & (df['Treatment'] == 'T')
	att_df = df[att_r]
	att_size = len(att_df)

	prog_r = att_df['Prognosis'] == 5
	prognosis_size  = len(att_df[prog_r])
	prog5_fft = prognosis_size  / att_size

	att_r = (df['Age'] <= 55) & (df['Test'] == 'N') & (df['Treatment'] == 'F')
	att_df = df[att_r]
	att_size = len(att_df)

	prog_r = att_df['Prognosis'] == 5
	prognosis_size  = len(att_df[prog_r])
	prog5_fff = prognosis_size  / att_size


	bn.add(BayesNode('Prognosis',['Age','Test','Treatment'],(1,3,5),
	{	
		
		(True,'Positive',False):{1:prog1_ttf,3:prog3_ttf,5:prog5_ttf},
		(True,'Positive',True):{1:prog1_ttt,3:prog3_ttt,5:prog5_ttt},

		(True,'Negative',False):{1:prog1_tff,3:prog3_tff,5:prog5_tff},
	
		(False,'Negative',True):{1:prog1_fft,3:prog3_fft,5:prog5_fft},
		(True,'Negative',True):{1:prog1_tft,3:prog3_tft,5:prog5_tft},

		(False,'Positive',True):{1:prog1_ftt,3:prog3_ftt,5:prog5_ftt},

		(False,'Positive',False):{1:prog1_ftf,3:prog3_ftf,5:prog5_ftf},
		

		(False,'Negative',False):{1:prog1_fff,3:prog3_fff,5:prog5_fff}
	}))

	return bn


def ask(var, value, evidence, bn):
	### Add your code here
	# Use joint probability chain ruling
	
	
	
	def helper_func(vars, e):
		if not vars:
			return 1.0
		var1 = vars[0]
		x = bn.get_var(var1)
		vallist = []
		if not x.parents:
			probkey = ''
		elif len(x.parents) == 1:
			probkey = e[x.parents[0]]
		else:
			for i in x.parents:
				vallist.append(e[i])
			probkey = tuple(vallist)
		if var1 not in e:
			return sum(x.cpt[probkey][m] * helper_func(vars[1:], e | {var1: m}) for m in x.cpt[probkey])
		else:
			return x.cpt[probkey][e[var1]] * helper_func(vars[1:], e)
	sum_r = 0

	for val1 in bn.get_var(var).space:
		# evidence[var] = val
		evid_var = evidence
		evid_var[var] = val1
		if val1 == value:
			num = helper_func(bn.variable_names, evid_var)
		sum_r += helper_func(bn.variable_names, evid_var)
	return num / sum_r


		
if __name__ == '__main__':
	net = makeCancerNet()
	print(net)
