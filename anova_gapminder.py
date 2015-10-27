import numpy
import pandas
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi 

data = pandas.read_csv('/Users/utpl/Documents/DataAnalysusTools/gapminder.csv', low_memory=False)

#SETTING MISSING DATA
data['employrate']=data['employrate'].replace(' ', 0)
data['internetuserate']=data['internetuserate'].replace(' ', 0)


#setting variables you will be working with to numeric
data['employrate'] = pandas.to_numeric(data['employrate']);
data['internetuserate'] = pandas.to_numeric(data['internetuserate']);



model1 = smf.ols(formula='employrate ~ C(internetuserate)', data=data)
results1 = model1.fit()
print (results1.summary())

