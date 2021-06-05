# Football-Analytics

In this repository I have explored some concepts of football analytics using Event data and Tracking data from different sources. This includes:
- Creation of a **Pitch Control Model**, which reflects the probability of the team getting the ball possession at a given filed position
- Explore different **Pitch Control variants**, focused on **Ball Possession Retention**, **Vertical Game**, of **Game by the Flanks**
- Computing the **value of a given action**, using SPADL structure data, based on the probability of a given action will end in goal
- Predicting if a **game action will lead to a goal or not**, using Machine Learning
- **Plots of different game features**, like a game move, shots frame and players passing and shooting accuracy
- Analysing the **importance of features** (like game stats and individual players) in the matches results
- Creation of an **Expected Goal Model**, using only distance to goal as input to a SVM classifier
- **Players Heat Map**, using tracking data
- **Predict a substitute player rating**, based on the game statistics until the moment he enters in the game
- Determination of the **best/most suitable position for a given player** (using FIFA 20 dataset)
- Implementation of a **Genetic Algorithm for finding the best set of players to buy under a given budget**, for given positions, considering different criteria, as, for example, the player age (using FIFA 20 dataset)
- Capture **Player playing style**, using **Non Negative Matrix Factorization**
- Also, a **Tableau dashboard of Manchester City season** 2018/2019 and beginning of 2019/2020 is available at https://public.tableau.com/profile/daniel.azevedo#!/vizhome/Dashboard_ManchesterCity_Analysis/Home_Dashboard. In this dashboard one can see the team performance in terms of results (home and away), scores, game stats, player individual stats, players importance on the game result, and much more
