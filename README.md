# README
##### MILESTONE A: Aggregation Module - Gather data from Piazza (4 points total) 
- Scrape Piazza to gather data
  - Option 1: Use an unofficial api found here: https://github.com/hfaran/piazza-api (Preferable method)
  - Option 2: Use a web scraper like JSoup
  - Option 3: Contact Piazza to get dumps
  - Option 4: Professor said he would also (if we need) give us a dump of a past CIS121 Piazza feed

##### MILESTONE B: Analyze data to determine similarities (8 points total)
- Determine how similar two documents are
  - Implement TF-IDF (Term Frequency - Inverse Document Frequency) (4 points)
  - Create vector representations of the Piazza posts
  - Compare those vector representations to determine similarity between posts
    - Use machine-learning on the TF-IDF output (which will serve as the base training data) to continuously become more accurate in determining similarity between posts (4 points)
      - Use Scikit-learn
  - Use the above algorithm to determine how similar two documents are on the Piazza data (2 points)
- Judge which posts are most similar or related to a given post

##### MILESTONE C: Use the crowd to determine how accurate these judgements are (3 points total)
- Possible disjoint scenarios that could occur:
  - Crowd judgements are very similar to our algorithm’s judgements
  - Crowd judgements are very different from our algorithm’s judgements
    - Rework our algorithm in determining how similar two Piazza posts are
  - Crowd judgements somewhat agree with our algorithm’s judgements
    - Look for ways to optimize our algorithm for in determining how similar two Piazza posts are
- If the algorithm needs to be updated, update the algorithm and then repeat this section (i.e. use the crowd to determine how accurate these new judgements are)

##### MILESTONE D: Quality control Module (2 points total)
- Create a gold-standard set of related Piazza posts and see how individuals perform on this set and/or a gold-standard set of unrelated Piazza posts and see how individuals perform on this set (2 points)
  - Create these sets such that they meet our definition of similarity (important - if they do not meet our definition of similarity than the results could be very skewed)

##### Bonus: Interface
- As the user is typing a question on Piazza, display related questions
- Implement in Javascript through a chrome extension
