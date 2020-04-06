# Understanding the effect of Dropout layers
Dropout simulates a sparse activation from a given layer, which interestingly, in turn, encourages the network to actually learn a sparse representation as a side-effect. As such, it may be used as an alternative to activity regularization for encouraging sparse representations in autoencoder models.

# Files and Models
The model in "square.py" has overfitting problem and gives much deviation in expected results. In "dr-square.py", we added a drop out layer which reduced the deviation in expected results.

# Using a saved model
We saved the trained model from "dr-square.py" as "dr-square-model.h5" and we used the saved model to make predictions using "load-dr-square-model.py"

# Results
The square of 7 in the model without dropout gave result as [67] 
The square of 7 in the model with dropout gave result as [50]

You can see the difference by seeing predictions for your values as well.
