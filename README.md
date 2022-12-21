# Movie Industry Exploratory Data Analysis

**Author:** Hazal Aydin
***

## Overview

I have been tasked with assisting Microsoft in their new movie studio initative. My goal was to explore what type of movies are currently doing the best at the box office and provide actionable insights based on this exploratory study. My analysis of the movie industry consisted of exploring IMDB and BOM data and utilising descriptive statistics and visualizations. The time period of the analysis was from 2010 to 2018. The results of the analysis showed that the Sci-Fi genre has the highest potential of the box office success. On the other hand, its distribution of total gross also suggests that the movies' success vary and there are risks involved. The other genres with high success potential are Animation and Adventure. The data also shows the movies that have a runtime between 125 minutes and 180 minutes are highly likely to succeed. Finally, there was no significant correlation between the average IMDB rating and the total gross. However, the results showed that the movies obtained a rating 8 and above had higher mean of total gross. Microsoft can use this report to brief wider exploratory studies and making decisions on the genres and movie lengths.

***

## Business Problem

Microsoft sees an opportunity to branch out to the multi-billion dollar movie-making industry. They decided to open a Microsoft Movie Studio but the challenge is they don't have the know-how in the industry. To assist them with this initiative, I explored what type of movies bring the highest worldwide gross.

I picked three variables to explore:

* Genre: Which genres have a higher chance of success? I picked this variable to explore because it can give a general direction of where this initiative is going.
* Movie Length: There is a trend of making longer movies in Holywood. I wanted to see if the longer movies have higher box office success - and if there is a limit to the movie length.
* Average Rating: The main question I explored if there is a correlation between the IMDB ratings and the worldwide total gross.

***

## Data

I used three datasets from two different data sources.

***
* IMDB Title Basics: It comes from the IMDB website where the information of the movies is stored.
* IMDB Title Ratings: It comes from the IMDB website as well but it includes the average ratings that are derived from votes submitted by IMDb users, not movie critics.
* BOM Movie Gross: It contains the domestic and foreign gross figures.

***

## Methods

I used data from provided files. First, I removed columns and rows that were not part of the study. I either filled the null values or drop the rows that consist of them. I merged all the datasets together as my Master DataFrame and saved the cleaned version of this DataFrame in my repository. While analysing each variable, I created a new copy of the master DataFrame so that my calculations won't modify the original object and won't raise a SettingWithCopyWarning.

***

## Results

![graph1](./images/total gross by genre.png)

The highest-grossing genre was Sci-Fi.

![graph2](./images/total gross by movie length.png)

The highest-grossing movie length was long format.

![graph3](./images/Average rating vs total gross.png)

There was a weak positive correlation between the average rating and the total gross figure and the association between them was negligible.

![graph4](./images/total gross by rating type.png)

The highest-grossing ratings were 8 and above.


## Conclusions

The insights of I derived from the study are:

* Microsoft should invest in Sci-Fi, Animation, or Adventure genres.
* The long-format movies that have a runtime of 125-180 minutes have higher box office success. However, when the runtime goes beyond 180 minutes, the total gross starts to decline. Therefore, Microsoft should produce a movie in a long format but shouldn't exceed 180 minutes mark.
* There is no significant correlation between average movie ratings and box office revenue. Being said that, I observed the higher rating movies tend to perform well at the box office. The recommended action here is not to focus on the ratings purely and use the high-rating movies as a benchmark purely.

In this study, I worked with constraints. The most important constraint was the delivery time of the analysis results. To derive some actionable insights, I had to limit the data I worked with and only selected three datasets. However, it became clear that more data was needed to explore the business problem. 

Moving forward, I highly recommend considering the followings:

* The production cost and the return on investment should be part of the following studies. We know the total gross but we don't know the cost of making a high-gross movie and how profitable it could be.
* I explored the genres separately but it would provide great value if the combination of these genres are explored as well.
* There is more variable that wasn't a part of this study but could potentially give actionable insights such as release dates, creative types, and production methods.
* Finally, this study only consists of movies released between 2010 and 2018. It doesn't answer how the most recent movies performed and if the global pandemic affected the overall trends. There is value to explore these questions in a separate study before making decisions.

***


## For More Information

Please review our full analysis in [my Jupyter Notebook](./dsc-phase1-project-template.ipynb) or my [presentation](./DS_Project_Presentation.pdf).

For any additional questions, please contact **Hazal Aydin** at **h.aydinhazal@gmail.com**

## Repository Structure

```
├── README.md                                        <- The top-level README for reviewers of this project
├── Movie Industry Exploratory Data Analysis.ipynb   <- Narrative documentation of analysis in Jupyter notebook
├── Microsoft_Project_Presentation.pdf               <- PDF version of project presentation
├── data                                             <- Both sourced externally and generated from code
└── images                                           <- Both sourced externally and generated from code
```
