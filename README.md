# MICROSOFT MOVIE STUDIO

**Author:** Caleb Stanley Ochieng
## Project Overview

Microsoft is exploring the possibility of entering the movie-making industry by establishing their own studio. However, they acknowledge that they lack experience in this field. As a result, they have requested my assistance in identifying trends within the movie industry that could contribute to their success. In order to facilitate the launch, I have examined historical movie data to identify the most favorable genres and release months that offer both high return on investments and low production costs. In line with this, I also identified the impact of star appeal (directors) in the studio's success.

### Business Problem

Microsoft aims to venture into the streaming and movie industry, seeking to compete with well-established platforms such as Netflix, Hulu, Amazon, Apple, and other major streaming services. This decision comes after observing the success achieved by competitors in this domain. The move towards diversifying their portfolio into different industries is seen as a positive step for large businesses. Given the significant size and promising potential for returns, delving into this expansive sector presents an excellent opportunity for Microsoft to generate additional revenue. Moreover, it offers an avenue to reach a broader audience, benefiting other sectors within the organization by attracting potential customers.

To establish the foundation of this new division, we will address the following inquiries:

1. Which movie genre would be most suitable for the initial launch?
2. What would be the optimal release date for the movie?
3. Who would be the ideal director to helm the film?
To achieve this, we will utilize data from reputable sources such as IMDB, Rotten Tomatoes, TheMovieDB, and The Numbers.

We are prioritizing these crucial aspects to identify the most promising genres that allow us to enter the industry with minimal production expenses. Additionally, determining the optimal launch timing will prevent us from getting overshadowed in a highly competitive market. Moreover, selecting a director who has already achieved success in the chosen genre and industry will provide us with a strong foundation to ensure a successful start.

### The Data

For this project, I will utilize data from various sources, including Box Office Mojo, IMDB, Rotten Tomatoes, TheMovieDB, and The Numbers. This data encompasses comprehensive details about movies, such as the key individuals involved in production, reviews, and financial metrics. To achieve our objectives of identifying the best genre, optimal release time, and ideal director, I will focus on crucial financial indicators, including global gross and production budget. Additionally, I will analyze factors like film performance across different release months and the directors behind the most successful films in genres with high potential. By leveraging this information, we aim to establish a robust foundation to enter the cinematic industry successfully.

The primary data of utmost importance revolves around financial metrics. Alongside global gross and production budget, I will examin the return on investment (ROI), represented as a percentage using the formula (profit/production budget)*100. These metrics will provide valuable insights for our analysis and decision-making process.

## Method

The first step involved acquiring the necessary data and organizing it into DataFrames. Although the initial data lacked significant utility on its own, I used SQL to merge the DataFrames and enhance their relevance. Next, I performed data cleaning operations, converting financial values into floats and eliminating duplicated and missing data. To facilitate analysis, I introduced a new column to calculate the ROI. Finally, I visualized the data using matplotlib and seaborn libraries.

## Results
1. Months with the highest movie releases are December, October, April, March, June, August and November respectively.

<img width="548" alt="Number of genres released per month" src="https://github.com/EngCS254/dsc-phase-1-project/assets/139503182/f018735d-a9d4-432d-bca6-aabebe571b20">

2. The first graph shows that the genre drama had the most releases followed by comedy and action while the second graph shows that the most released grouped genres are 'comedy,drama', 'drama,romance', 'comedy,drama, romance' and 'action,crime,drama'.

<img width="726" alt="Number of movies in each exploded genre" src="https://github.com/EngCS254/dsc-phase-1-project/assets/139503182/3eafa4bf-2eb8-43fa-aefb-1419b2b37743">

<img width="548" alt="Number of movies in each top ten genre per month" src="https://github.com/EngCS254/dsc-phase-1-project/assets/139503182/a9a2429c-5d1f-4ced-8eec-a0acea10c16a">

3. The movie production industry is dominated by few directors. These directors produce the most released genres we earlier identified.

<img width="495" alt="Directors of the most released genres" src="https://github.com/EngCS254/dsc-phase-1-project/assets/139503182/3b1dbc4c-a11f-421a-8253-ed97b88cf41c">

4. April had the highest roi followed by July, December, May, November, June and January respectively. Having a closer look at the month of April, I see that despite not being the month with the highest genre releases, with the genre released in that month being a combination of Comedy, Drama and Horror with its director being Graham Wright.

<img width="566" alt="ROI per month" src="https://github.com/EngCS254/dsc-phase-1-project/assets/139503182/9b82141b-24f3-4c66-9e0b-4faa92cec42e">

5. The below line graph reveals that the some of the genres with the highest roi are horror, musical, animation and family. I find this quite strange given that these are not the same genres I find under mostly released genres per month.

<img width="732" alt="Average ROI per genre" src="https://github.com/EngCS254/dsc-phase-1-project/assets/139503182/fb278f25-c082-4f1a-a3e8-b274dc85d4db">

6. The below heat map shows that from a closer look, contrary to the above line graph, the sport genre had the highest ROI. This could be due to the low investment/budget put in this movie genre compared to horror.

<img width="416" alt="Average ROI FO Top 10 exploded genres" src="https://github.com/EngCS254/dsc-phase-1-project/assets/139503182/2b885e8d-43d4-4000-b645-f09083fea5a5">

Looking at the grouped genres, I found that when movies released have combined genres, the ROI is much higher. An instance is where a combination of action, comedy and drama have the highest ROI.

<img width="540" alt="Average ROI for top 10 grouped genres" src="https://github.com/EngCS254/dsc-phase-1-project/assets/139503182/fac2a7d1-12cb-49a3-afd4-9ca619a99951">

7. Top 30 directors with the highest ROI in our dataset directed movies with genres as follows Biography, Documentary, Action, Comedy, Drama, Romance, Horror, Animation, Family, Sport, Fantasy and Musical. Their main release months are January, February, March, October, November and December.

<img width="413" alt="Average ROI for Top 30 Directors" src="https://github.com/EngCS254/dsc-phase-1-project/assets/139503182/027a3a87-9c0c-4510-95a4-3f132af61726">


## CONCLUSION

Venturing into the movie industry would indeed be a profitable venture for Microsoft if some key points as captured in our analysis are met. 

Having ROI as my main money matrix besides the world-wide profit, I observed that having a high budget movie does not necessarily mean high ROI. The genre of the movies being released matters for a high ROI to be achieved. From the analysis done, Producing movies with combined genres offers more potential for successand release then in December, November and October. On the Flip side, they could focus on the animation, horror and/or musical genre which offer high ROI with little budget. 

The company can also consider employing directors like Steven Soderbergh, Steven Spielberg or David Gordon Green who have a lot of experience in their genre areas. They can also engage directors like Sébastien Lifshitz, Sujit Mondal, Adnan A. Shaikh, Karthik Chandan and/or Chad Zuver who are also well experienced in directing their movie genres and have also proven to generate high ROI in their work.

## Repository Structure

README.MD: Readme file for reviewers of the project.

student.ipynb: Jupyter notebook containing the code used to explore, clean, and analyze the data.

student.pdf: PDF version of the notebook

presentation.pdf: Google Slides presentation

Data: Folder containing the data used for the project, including the cleaned versions of the data.

Figures: Includes the figures in the presentation.
