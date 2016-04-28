# README
#### MILESTONE A: Aggregation Module - Gather data from Piazza (4 points total) 
- Scrape Piazza to gather data
  - Option 1: Use an unofficial api found here: https://github.com/hfaran/piazza-api (Preferable method)
  - Option 2: Use a web scraper like JSoup
  - Option 3: Contact Piazza to get dumps
  - Option 4: Professor said he would also (if we need) give us a dump of a past CIS121 Piazza feed

#### MILESTONE B: Analyze data to determine similarities (8 points total)
- Determine how similar two documents are
  - Implement TF-IDF (Term Frequency - Inverse Document Frequency) (4 points)
  - Create vector representations of the Piazza posts
  - Compare those vector representations to determine similarity between posts
    - Use machine-learning on the TF-IDF output (which will serve as the base training data) to continuously become more accurate in determining similarity between posts (4 points)
      - Use Scikit-learn
  - Use the above algorithm to determine how similar two documents are on the Piazza data (2 points)
- Judge which posts are most similar or related to a given post

#### MILESTONE C: Use the crowd to determine how accurate these judgements are (3 points total)
- Possible disjoint scenarios that could occur:
  - Crowd judgements are very similar to our algorithm’s judgements
  - Crowd judgements are very different from our algorithm’s judgements
    - Rework our algorithm in determining how similar two Piazza posts are
    - Possibility that user gives random input, this acts as a QC on the user's input
  - Crowd judgements somewhat agree with our algorithm’s judgements
    - Look for ways to optimize our algorithm for in determining how similar two Piazza posts are
- If the algorithm needs to be updated, update the algorithm and then repeat this section (i.e. use the crowd to determine how accurate these new judgements are)

#### MILESTONE D: Quality control Module (2 points total)
- Create a gold-standard set of related Piazza posts and see how individuals perform on this set and/or a gold-standard set of unrelated Piazza posts and see how individuals perform on this set (2 points)
  - Create these sets such that they meet our definition of similarity (important - if they do not meet our definition of similarity than the results could be very skewed)

#### Bonus: Interface
- As the user is typing a question on Piazza, display related questions
- Implement in Javascript through a chrome extension
- Currently, a command line program is used for a proof of concept

<-----------------------------Everything above is a checklist for what we aim to accomplish in this project--------------------------------->

<-------------------------------------------The following is the recent update of our project----------------------------------------------->

#### Input Data
Our project requires large amounts of Piazza data in order to gather input from the crowd. The Piazza team gave us access to dump files from the last few semesters of CIS 120, 121, and 160. We will then parse this data using Python or Bash in order to get the plaintext questions that have been asked for each course and each assignment in that course. We will upload only the question's text onto the crowdsourcing platorm; no other information from the post will be shared with the crowdworkers.

#### Quality Control and Aggregation
We will use gold standard questions within our HIT to ensure we are getting quality results from the crowdworkers. After the results are collected, we will check each worker's answers to the gold standard questions in order to decide whether or not to trust that worker's judgements. Note that gold standard questions are shown in the internal CrowdFlower platform. Sample code for aggregation and QC are included in the repo. Also, having the option of none of them is similar provides QC to the Piazza user input. 

#### Step by Step Instructions for the User
Our final product involves using a machine learning clustering algorithm to provide similar questions (and their answers) to the question that a student types in on Piazza.
###### The First Crowdsourcing Aspect
When a person types in a question that they want to ask on Piazza, our clustering algorithm will suggest a list of similar questions. The user will then select the questions that they think are indeed similar. This allows us to passively collect input from the crowd. This passive data collection will be handled through a Chrome extension or a third-party website. 
###### The Second Crowdsourcing Aspect
After the user selects the similar questions from the suggested questions, the unselected questions (along with the user's inputted question) will be sent to a crowdworking platform to be evaluated by workers. The workers will decide whether or not the unselected questions are similar to the user's question; for each pair, they will answer either yes or no. Then we wiill compile the results from the the crowdsourcing platform and feed the results back into our clustering algorithm in order to provide better suggested questions for future Piazza users.

#### What the code does?
###### Aggregation
To aggregate the inputted dump of piazza posts along with the user query, we treat the query as an additional post. Then, we tokenize all of the posts and remove stop-words. Next, we compute tf-idf for every term in the body of each respective piazza post. To turn this numerical data (representing each piazza post, or document) into sets of similar posts, we use Scikit Learn to run the K-Means clustering algorithm on the tf-idf data. Finally, we determine which cluster the query is in and give the user the option to choose whether his/her question is similar to the displayed questions from the cluster.
NOTE: The tutorial at http://brandonrose.org/clustering was followed very closely for implementing the tokenizer and K-Means clustering. The code is publicly available and we use code directly from his tutorial to prepare the data for clustering and to perform the clustering.
###### Crowdsourcing
To determine the accuracy of our algorithm and to improve upon said accuracy, we use workers on Crowdflower to validate the results. Each crowdworker is presented with a query question (asked by a user of our system) and a set of five questions from the cluster that the query question part of. Then, the worker determines which question the query question is most similar to (or if the query question is not similar to any of them) and we use this to validate the output of our algorithm. Looking forward, we will feed these inputs into our algorithm to build a semi-supervised crowd-sourced clustering algorithm.
##### Simulation
To simulate large amounts of inputs (queries) to the code, we developed a script that 
- 1. Picks a query string from the list of available queries
- 2. Creates the clusters based on the input data
- 3. Determines which cluster the query appears in
- 4. Records the most relevant results in the cluster to the query (relevance determined by tf-idf)
- 5. Randomly chooses one of the most relevant results to be "selected by the user" as most similar to the query
- 6. Repeats the process until all available queries (or a predetermined number of those queries) have been processed.
The list of available queries will either be all of the questions from the piazza dump or all of the paraphrased questions we received from the crowd.
##### csvToGraphData and donutChart.html
To aggregate the crowd results from crowdflower to crate our donut chart, we read in our results from crowdflower and computed the majority vote answer (0-5) for each HIT where 6 would be returned.  We compiled the frequencies for each value and printed them.  Using these frequences we created a donut chart by filling in the values for each result 0-5 in the GoogleAPI template in our file donutChart.html.  The chart can be found in DonutChart.png.
###### Running the code
To run the code: 
1. Install the dependencies, including json, csv, numpy, pandas, nltk
, sklearn 
2. From the command line run 'python', 'import nltk', 'nltk.download()', and download punkt and stopwords 
3. Run 'python query_cluster.py clean_output.json' from the unix terminal
#### Profit
