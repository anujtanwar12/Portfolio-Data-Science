
# Movie Recommendation System

Recommendation Systems play a crucial and important role in this “era of abundance”. For any product,
there are thousands of options.Recommendation systems help to personalize a platform and help the user
find something they might like. Online streaming services such as Netflix, Disney, YouTube, Amazon, etc
use these recommendation systems to make the right recommendations about the movies and shows can
have drastic impact on the customer base and the overall business. If customers are satisfied with the
recommendations, they will spend more time using the service and would not look for other streaming
services options which leads to customer retention and growth in sales and profit. Various sources say that
as much as 35–40% of tech giants’ revenue comes from recommendations alone.
The Netflix offered a Prize of 1 million dollar and hosted an open competition for the best recommendation
algorithm to predict user ratings for films, based on previous ratings without any other information about
the users or films, i.e. without the users or the films being identified except by numbers assigned for the
contest.



## Authors

- [@anujtanwar12](https://www.github.com/anujtanwar12)


## Modeling and Analysis

I am using Netfilx data and MovieLense data to demonstrate my approach to address the problem.
Below are the steps involved with Netflix data:
1. Download the datasets
2. Read the dataset files in different dataframes
3. Clean the data
4. Transform the data to have customer and movies related data along with Ratings given to the movies.
5. Now we can use this dataframe to do the regression and predictions

## Github Link

https://github.com/anujtanwar12/Portfolio-Data-Science/tree/main/3.%20Movie%20Recommendation%20System

## Implications

1. At best, recommendation systems serve both service providers and consumers alike. Consumers saves
effort and time from going browsing through vast variety of products. Sellers drive sales and build
loyality. However, recommendation systems also have unintended consequences.Recommendation Systems
can result in biases. As consumers gets a humongous variety of options, they must pay great
attention in evaluating potential products. Moreover, along with invested time lost, consumers can not
unlist, unread or unwatch goods that turn out to be a poor fit.
2. “Do I like this?”, “Should I like this?”: Surprisingly, recommendation systems alter how much consumers
are willing to pay for a product that they just saw. Consumers don’t just prefer what they
have experienced; they prefer what the system said they would like. This is surprising as consumers
shouldn’t need a system to tell them how much they enjoyed a product they just saw.
Limitations
1. Cold start problem: When building a new system, there would be no user data to start with. Only
approach to be used in that situation is to first use content-based filtering first and then move on to
collaborative filtering approach.
2. Scalability: As the number of users grow, the algorithms suffer scalability issues. If you have 10 million
customers and 100,000 movies, you would have to create a sparse matrix with one trillion elements.
3. Lack of right data


## Concluding Remarks
Recommendation systems provide recommendations by taking what other people recommend as well as our
selections into account.
Although recommendation systems help both buyers and sellers greatly, they are not perfect and have certain
limitations and implications.
Collaborative Filtering is a widely used and very effective solution for recommendation systems.

## References
1. https://data-flair.training/blogs/data-science-projects-code/
2. https://rpubs.com/vsi/movielens
3. https://towardsdatascience.com/brief-on-recommender-systems-b86a1068a4dd
4. https://www.mygreatlearning.com/blog/masterclass-on-movie-recommendation-system/
5. https://subscription.packtpub.com/book/big_data_and_business_intelligence/9781785884696/8/ch08lvl1sec62/limitations-of-a-recommendation-system


