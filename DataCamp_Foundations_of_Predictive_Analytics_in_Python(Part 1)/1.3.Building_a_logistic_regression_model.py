'''You can build a logistic regression model using the module linear_model from sklearn. 
First, you create a logistic regression model using the LogisticRegression() method:

logreg = linear_model.LogisticRegression()
Next, you need to feed data to the logistic regression model, so that it can be fit. X contains the predictive variables, whereas y has the target.

X = basetable[["predictor_1","predictor_2","predictor_3"]]`
y = basetable[["target"]]
logreg.fit(X,y)
In this exercise you will build your first predictive model using three predictors.'''
#TASK
# Import the methodlinear_model from sklearn.
# The basetable is loaded as basetable. Note that the column "gender" has been transformed to gender_F so that it can be used as a predictor. Construct a dataframe X that contains the predictors age, gender_F and time_since_last_gift.
# Construct a dataframe y that contains the target.
# Create a logistic regression model.
# Fit the logistic regression model on the given basetable.


# Import linear_model from sklearn.
from ____ import ____

# Create a dataframe X that only contains the candidate predictors age, gender_F and time_since_last_gift.
X = ____[[____, ____, ____]]

# Create a dataframe y that contains the target.
y = ____[[____]]

# Create a logistic regression model logreg and fit it to the data.
logreg = ____.____
logreg.____(____, ____)






#SOLUTION
# Import linear_model from sklearn.
from sklearn import linear_model

# Create a dataframe X that only contains the candidate predictors age, gender_F and time_since_last_gift.
X = basetable[['age', 'gender_F', 'time_since_last_gift']]

# Create a dataframe y that contains the target.
y = basetable[['target']]

# Create a logistic regression model logreg and fit it to the data.
logreg = linear_model.LogisticRegression()
logreg.fit(X, y)