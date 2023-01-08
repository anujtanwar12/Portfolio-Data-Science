
# Temperature Prediction - Data Science Project

Weather is one that is not just close to us but is essential for our survival. Lot of businesses rely on weather, farmers rely on weather, bad weather can devastate the food on the fields. Sudden change in surface temperature can be harmful for our health as well. Research shows that abnormal weather disrupts the operating and financial performance of 70% of businesses worldwide. Every year, weather variability is estimated to cost $630 billion for the U.S. alone, or 3.5% of GDP. It becomes important to forecast weather in an accurate and timely fashion so that we can take the necessary precautions to minimize weather-associated risks. In the project I am predicting surface temperature using Long-Short Term Network (LSTM)-based model on more than 100 years of surface temperature recorded data from Kaggle.

Model prompts user to enter the city and search historical data of the city for current date of the month of each historical year. Then, it will clean the dataset and plot various graphs to understand the dataset. I will calculate mean, median, mode, Standard Deviation and Population Variance. I will use linear regression to predict future temperature.
## Authors

- [@anujtanwar12](https://www.github.com/anujtanwar12)



## Building and Evaluating Model

•	Before building the predictive model, I prepped train and test datasets by using min max scaler that shrinks the data within the given range, usually of 0 to 1 and reshaping the datasets.

•	Then I build a LSTM sequential predictive model with 4 neurons and 100 epochs. The mean squared error is being used as the loss function. Additionally, the adam optimizer is used, with training done over 100 epochs.

•	Predictions were made on test data using model. Predict function to check the accuracy of the data.

## Assumptions

Weather forecasting is a huge challenge, we are trying to predict something which is inherently unpredictable. Atmosphere is a chaotic system, a small change in its state at a location can have huge impact elsewhere, this is called Butterfly affect. A small error in prediction can rapidly grow and cause errors on a larger scale. And since many assumptions must be made when modelling the atmosphere, it becomes clear how easily forecast errors can develop. For a perfect forecast, we would need to remove every single error which is practically not possible. For the project, we are assuming there are no other factors that can influence the prediction and there could be some scope of error between prediction and actual values.

## Github Link

https://github.com/anujtanwar12/Portfolio-Data-Science/tree/main/1.%20Temperature%20Prediction