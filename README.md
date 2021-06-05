# Football-Analytics

In this repository I have explored some concepts of football analytics using Event data and Tracking data from different sources. This includes:
- Creation of a **[Pitch Control Model](https://github.com/danielazevedo/Football-Analytics/tree/master/pitch_control_variants)** (baseline), which reflects the probability of the team getting the ball possession at a given filed position
- Explore different **[Pitch Control variants](https://github.com/danielazevedo/Football-Analytics/tree/master/pitch_control_variants)**, focused on **Ball Possession Retention**, **Vertical Game**, of **Game by the Flanks**
- Computing the **[value of a given action](https://github.com/danielazevedo/Football-Analytics/tree/master/actions_value)**, using SPADL structure data, based on the probability of a given action will end in goal
- Predicting if a **[game action will lead to a goal or not](https://github.com/danielazevedo/Football-Analytics/tree/master/actions_value)**, using Machine Learning
- **[Plots of different game features](https://github.com/danielazevedo/Football-Analytics/tree/master/game_moves_analysis)**, like a game move, shots frame and players passing and shooting accuracy
- Analysing the **[importance of features](https://github.com/danielazevedo/Football-Analytics/tree/master/features_importance)** (like game stats and individual players) in the matches results
- Creation of an **[Expected Goal Model](https://github.com/danielazevedo/Football-Analytics/tree/master/expected_goals)**, using only distance to goal as input to a SVM classifier
- **[Players Heat Map](https://github.com/danielazevedo/Football-Analytics/tree/master/broadcast_tracking_data)**, using tracking data
- **[Predict a substitute player rating](https://github.com/danielazevedo/Football-Analytics/tree/master/substitutions_impact)**, based on the game statistics until the moment he enters in the game
- Determination of the **[best/most suitable position for a given player](https://github.com/danielazevedo/Football-Analytics/tree/master/FIFA_20_analysis)** (using FIFA 20 dataset)
- Implementation of a **[Genetic Algorithm for finding the best set of players to buy under a given budget](https://github.com/danielazevedo/Football-Analytics/tree/master/genetic_algorithms__Player_scouting)**, for given positions, considering different criteria, as, for example, the player age (using FIFA 20 dataset)
- Capture **[Player playing style](https://github.com/danielazevedo/Football-Analytics/tree/master/playing_style)**, using **Non Negative Matrix Factorization**
- Also, a **[Tableau dashboard of Manchester City season](https://public.tableau.com/profile/daniel.azevedo#!/vizhome/Dashboard_ManchesterCity_Analysis/Home_Dashboard)** 2018/2019 and beginning of 2019/2020. In this dashboard one can see the team performance in terms of results (home and away), scores, game stats, player individual stats, players importance on the game result, and much more
