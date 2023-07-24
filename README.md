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




### Key Points

* **Your analysis should yield three concrete business recommendations.** The ultimate purpose of exploratory analysis is not just to learn about the data, but to help an organization perform better. Explicitly relate your findings to business needs by recommending actions that you think the business (Microsoft) should take.

* **Communicating about your work well is extremely important.** Your ability to provide value to an organization - or to land a job there - is directly reliant on your ability to communicate with them about what you have done and why it is valuable. Create a storyline your audience (the head of Microsoft's new movie studio) can follow by walking them through the steps of your process, highlighting the most important points and skipping over the rest.

* **Use plenty of visualizations.** Visualizations are invaluable for exploring your data and making your findings accessible to a non-technical audience. Spotlight visuals in your presentation, but only ones that relate directly to your recommendations. Simple visuals are usually best (e.g. bar charts and line graphs), and don't forget to format them well (e.g. labels, titles).

## Getting Started

Please start by reviewing this assignment, the rubric at the bottom of it, and the "Project Submission & Review" page. If you have any questions, please ask your instructor ASAP.

Next, we recommend you check out [the Phase 1 Project Templates and Examples repo](https://github.com/learn-co-curriculum/dsc-project-template) and use the MVP template for your project.

Alternatively, you can fork [the Phase 1 Project Repository](https://github.com/learn-co-curriculum/dsc-phase-1-project), clone it locally, and work in the `student.ipynb` file. Make sure to also add and commit a PDF of your presentation to your repository with a file name of `presentation.pdf`.

## Project Submission and Review

Review the "Project Submission & Review" page in the "Milestones Instructions" topic to learn how to submit your project and how it will be reviewed. Your project must pass review for you to progress to the next Phase.

## Summary

This project will give you a valuable opportunity to develop your data science skills using real-world data. The end-of-phase projects are a critical part of the program because they give you a chance to bring together all the skills you've learned, apply them to realistic projects for a business stakeholder, practice communication skills, and get feedback to help you improve. You've got this!
