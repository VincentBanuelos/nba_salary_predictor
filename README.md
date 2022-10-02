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
|logerror|The difference betwen the log of the Zestimate and the log of the sale price|float|
---
| Feature | Definition | Data Type |
| ----- | ----- | ----- |
| county | Name of county property is located in| object |
| yearbuilt |  The Year the principal residence was built| float |
| tax_value |  The total tax assessed value of the parcel | float |
| structuretaxvaluedollarcnt | The assessed value of the built structure on the parcel| float |
| landtaxvaluedollarcnt | The assessed value of the land area of the parcel | float |
| latitude |  Latitude of the middle of the parcel multiplied by 10e6 | float |
| longitude |  Longitude of the middle of the parcel multiplied by 10e6 | float |
| los_angeles| 1 if the house is located within Los Angeles County|int|
| orange| 1 if the house is located within Orange County|int|
| ventura| 1 if the house is located within Ventura County|int|
| house_lotsize_ratio| Gives the percentage of land a house takes up out of the lotsize| float |

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
