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
  - Crowd judgements somewhat agree with our algorithm’s judgements
    - Look for ways to optimize our algorithm for in determining how similar two Piazza posts are
- If the algorithm needs to be updated, update the algorithm and then repeat this section (i.e. use the crowd to determine how accurate these new judgements are)

#### MILESTONE D: Quality control Module (2 points total)
- Create a gold-standard set of related Piazza posts and see how individuals perform on this set and/or a gold-standard set of unrelated Piazza posts and see how individuals perform on this set (2 points)
  - Create these sets such that they meet our definition of similarity (important - if they do not meet our definition of similarity than the results could be very skewed)

#### Bonus: Interface
- As the user is typing a question on Piazza, display related questions
- Implement in Javascript through a chrome extension

#### Input Data
Our project requires large amounts of Piazza data in order to gather input from the crowd. The Piazza team gave us access to dump files from the last few semesters of CIS 120, 121, and 160. We will then parse this data using Python or Bash in order to get the plaintext questions that have been asked for each course and each assignment in that course. We will upload only the question's text onto the crowdsourcing platorm; no other information from the post will be shared with the crowdworkers.

#### Quality Control and Aggregation
We will use gold standard questions within our HIT to ensure we are getting quality results from the crowdworkers. After the results are collected, we will check each worker's answers to the gold standard questions in order to decide whether or not to trust that worker's judgements. Sample code for aggregation and QC are included in the repo.

#### Step by Step Instructions for the User
Our final product involves using a machine learning clustering algorithm to provide similar questions (and their answers) to the question that a student types in on Piazza.
###### The First Crowdsourcing Aspect
When a person types in a question that they want to ask on Piazza, our clustering algorithm will suggest a list of similar questions. The user will then select the questions that they think are indeed similar. This allows us to passively collect input from the crowd.

###### The Second Crowdsourcing Aspect
After the user selects the similar questions from the suggested questions, the unselected questions (along with the user's inputted question) will be sent to a crowdworking platform to be evaluated by workers. The workers will decide whether or not the unselected questions are similar to the user's question; for each pair, they will answer either yes or no. Then we wiill compile the results from the the crowdsourcing platform and feed the results back into our clustering algorithm in order to provide better suggested questions for future Piazza users.
