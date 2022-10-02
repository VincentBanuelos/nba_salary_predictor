# <a name="top"></a>Predicting NBA Salaries using Regression
![]()

by: Vincent Banuelos

***
[[Project Description/Goals](#project_description_goals)]
[[Initial Questions](#initial_questions)]
[[Planning](#planning)]
[[Data Dictionary](#dictionary)]
[[Reproduction Requirements](#reproduce)]
[[Pipeline Takeaways](#pipeline)]
[[Conclusion](#conclusion)]

___

## <a name="project_description_goals"></a>Project Description/Goals:
- Using both basic stats and advanced stats can I predict an NBA player's salary as well as what which stat(s) are the biggest driver's of an NBA players Salary.

- This project runs through the entire Data Science Pipeline using regression models to attmept to predict NBA PLayers' salaries.

[[Back to top](#top)]


## <a name="initial_questions"></a>Initial Questions:

- Does the county a property is located in affect it's log error?
- Does the tax variables of a house affect the logerror?
- Does the ratio of home sqft to lot sqft affect logerror?
- Does the year a house was built affect logerror?

[[Back to top](#top)]


## <a name="planning"></a>Planning:

- Create README.md with data dictionary, project goals, and come up with initial hypotheses.
- Acquire data from the Basketball Reference website, turn into a CSV and create a function to automate this process. 
- Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process. 
- Store the acquisition and preparation functions in a wrangle.py module function, and prepare data in Final Report Notebook by importing and using the function.
- Clearly define at least two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- Establish a baseline accuracy and document well.
- Train at least 3 different regression models.
- Evaluate models on train and validate datasets.
- Choose the model that performs the best and evaluate that single model on the test dataset.
- Document conclusions, takeaways, and next steps in the Final Report Notebook.

[[Back to top](#top)]

## <a name="dictionary"></a>Data Dictionary  

| Target Attribute | Definition | Data Type |
| ----- | ----- | ----- |
|salary|The NBA Player's salary for the 2017-2018 season|float|
---
| Feature | Definition | Data Type |
| ----- | ----- | ----- |
| age | Player's Age on Feb 1 of the season| float |
| gp |  Games Played in 2017-2018 season| float |
| gs |  Games Started in 2017-2018 season| float |
| mp |  Minutes Played in 2017-2018 season| float |
| fg |  Number of Field Goals made in 2017-2018 season| float |
| fga |  Number of Field Goals attempted in 2017-2018 season| float |
| 2p |  Number of 2-pointers made in 2017-2018 season| float |
| 2pa |  Number of 2-pointers attempted in 2017-2018 season| float |
| 3p |  Number of 3-pointers made in 2017-2018 season| float |
| 3pa |  Number of 3-pointers attempted in 2017-2018 season| float |
| ft |  Number of Freethrows made in 2017-2018 season| float |
| fta |  Number of Freethrows attempted in 2017-2018 season| float |
| orb | Offensive rebounds per game | float |
| drb | Defensive rebounds per game | float |
| trb | Total rebounds per game | float |
| ast| Asists per game|float|
| stl| Steals per game|float|
| blk| Blocks per game|float|
| tov| Turnovers per game|float|
| pf| Personal Fouls per game|float|
| ppg| Points per game|float|
| fg_pct| Field Goal Percentage|float|
| 2p_pct| 2 Point Field Goal Percentage|float|
| 3p_pct| 3 Point Field Goal Percentage|float|
| ft_pct| Freethrow Percentage|float|
| ts_pct| True Shooting Percentage, True shooting percentage is a measure of shooting efficiency that takes into account field goals, 3-point field goals, and free throws.|float|
| efg_pct| Effective Field Goal Percentage, This statistic adjusts for the fact that a 3-point field goal is worth one more point than a 2-point field goal|float|
| pos |  Player's position|object|
| ws | Win Shares; an estimate of the number of wins contributed by a player. | float |
| ortg | Offensive Rating for players it is points produced per 100 posessions| float |
| drtg |Defensive Rating for players it is points allowed per 100 posessions.| float |
| ows| Offensive Win Shares | float |
| dws| Defensive Win Shares | float |
| bpm| Box Plus/Minus a box score estimate of the points per 100 possessions that a player contributed above a league-average player, translated to an average team. | float |
| obpm |  Offensive Box Plus/Minus | float |
| dbpm |  Offensive Box Plus/Minus | float |
| vorp|  Value Over Replacement Player; a box score estimate of the points per 100 TEAM possessions that a player contributed above a replacement-level (-2.0) player, translated to an average team and prorated to an 82-game season.|float|
|per| Player Efficiency Rating; PER sums up all a player's positive accomplishments, subtracts the negative accomplishments, and returns a per-minute rating of a player's performance.|float|
|orb_pct| An estimate of the percentage of available offensive rebounds a player grabbed while they were on the floor| float |
|drb_pct| An estimate of the percentage of available defensive rebounds a player grabbed while they were on the floor| float |
|trb_pct| An estimate of the percentage of available rebounds a player grabbed while they were on the floor| float |
|ast_pct| Assist percentage is an estimate of the percentage of teammate field goals a player assisted while he was on the floor.| float |
|stl_pct| Steal Percentage is an estimate of the percentage of opponent possessions that end with a steal by the player while he was on the floor.| float |
|blk_pct| Block percentage is an estimate of the percentage of opponent two-point field goal attempts blocked by the player while he was on the floor.| float |
|tov_pct| Turnover percentage is an estimate of turnovers per 100 plays.| float|
|usg_pct| Usage percentage is an estimate of the percentage of team plays used by a player while he was on the floor.|float|
|above_avg_scorer| 1 if a player is above the league average in scoring. 0 if not above average.|float|
|above_avg_3ball| 1 if a player is above the league average in 3pt %. 0 if not above average.|float|
|above_avg_ft| 1 if a player is above the league average in Freethrow %. 0 if not above average.|float|
|above_avg_usg_pct| 1 if a player is above the league average in Usage %. 0 if not above average.|float|
|C| 1 if a player is a Center. 0 if not.|float|
|F| 1 if a player is a Forward. 0 if not.|float|
|G| 1 if a player is a Guard. 0 if not.|float|


---

## <a name="reproduce"></a>Reproduction Requirements:

You will need your own env.py file with database credentials then follow the steps below:

  - Download the csv files, allplayers_wrangle.py, model.py, explore.py, and final_report.ipynb files
  - Run the final_report.ipynb notebook

[[Back to top](#top)]


## <a name="pipeline"></a>Pipeline Conclusions and Takeaways:

###  Wrangling Takeaways
- Using data from basketball reference we pulled in players' statistical and salary data from the 2017-2018 NBA Season. 
- Following the Data Acquisition the following preparation work was done to the acquired data:
    - Removed any players who did have complete statistical lines or salaries from the dataset.
    - Created features that compare and find players who are above average in a few commonly used stats.
    - Following data prepartion, we were left with a dataframe consisting of 415 observations and 55 statistical columns.
    - Split data into 3 datasets, train, validate and test

### Exploration Summary

- Players with an above avg TS% and PPG DO earn a significantly different salary than then the rest of the league.

- Players with an above avg USG % DO earn a significantly different salary than then the rest of the league.

- Players with an above avg VORP DO earn a significantly different salary than then the rest of the league.

- We saw that a position that a player pays does have a impact on their salary.

## Modeling takeaways

- The Tweedie Regressor model did the most consistent out of all the models tested and did not overfit. 

- With the model for all three data sets roughly falling 4-5 million dollars off of a players actual salary.

[[Back to top](#top)]


## <a name="conclusion"></a>Conclusion, and Next Steps:

- Although this number seems far off without context it must be remembered that there are factors at play that simply cannot be measured by statistics alone.

- Factors such as player popularity in the team's fanbase, a player's potential to improve, the market value of a player with similar skillsets, whether a player is willing to take a pay cut for a better chance at winning, personal achievements by a player such as MVP, ALL-NBA, ALL-DEFENSE, All-Star selections, whether a player has been injured, etc.

- For the next steps after this project I would like to incorporate a player's personal achievements into consideration and see how much those achievements affect players' salaries.

- As well as pulling in shot chart data that shows a player's shot distribution, seeing as how certain players may perform best in certain roles, such as a spot-up shooter, pick and roll maestro or rollman, etc.

- With the NBA being an everchanging league, certain players will fill roles that are seen as better contributors to winning, and thus salaries will continue to fluctuate for players outside or the elite of the elite players.

- In conclusion, I believe my models provided a good starting point for giving a player an initial offer based solely on statistics alone.  
    
[[Back to top](#top)]
