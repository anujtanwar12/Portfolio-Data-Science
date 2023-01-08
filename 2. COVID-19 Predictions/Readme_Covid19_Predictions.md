
# COVID-19 Predictions India

India has seen an increase in COVID-19 case again during the start of year 2022. A simple google search can tell us that on April 4th, there were only 795 new cases, on Apr 14th there were 949 and in last week count of new cases have been on constant rise and going above 2000 per day now. This trend shows the cases have been rising. As per Ministry of Health and Family Welfare Government of India (https://www.mohfw.gov.in/) there had already been more than half a million documented deaths due to COVID and active cases are on rise. Government of India has also issued new guidelines and restrictions. Referring to the below google graph, we can see that COVID spread had increased in India during the summer months in last 2 years. 2022 summer season has already started in India, so the concerning questions that we have are:
1. Are we going to have another wave of COVID? 
2. If so, then how severe it can be? 
3. When will we see the peak? 
4. How long did the previous waves last?
5. What was the trend in death toll every day?
6. What was the cured trend?

I will use data mining techniques learnt in this course to study the data and make prediction on it.





## Authors

- [@anujtanwar12](https://www.github.com/anujtanwar12)


## Model building and evaluation

•	Model Used: Long short-term memory (LSTM). It is an artificial neural network used in the fields of artificial intelligence and deep learning.

•	I have used sequential model from tensorflow.keras package.

•	Added a long short-term memory layer with 100 memory units

•	Used rectified linear activation function (RELU) which will output the input directly if it is positive, otherwise, it will output zero.

•	Used 20% dropout.

•	Compiled the model with adam optimizer


## Github Link

https://github.com/anujtanwar12/Portfolio-Data-Science/tree/main/2.%20COVID-19%20Predictions


