# NYCU-Intro-to-Database-System-HW3

<b>Build an application with a database management system and AWS!</b>

In this semester, you’ve learned about database management systems. Now it’s time to build an application and take advantage of it. 

The application can be for any purpose, such as (but not limited to):
- COVID-19 antigen rapid test hunter
- Outbreak near me
- Course selection guide
- Stock price prediction or buying/selling notification
- Social network systems monitoring
- NBA or FIFA World Cup championship prediction
- … and others

You might notice that you need “data” to establish the foundation of your application. You can use any method to gather the data you need, such as (but not limited to):
- Open data from the government 
  - For example, https://data.gov.tw/
  - with API or CSV files
- Web scraping 
  - For example, https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/
- Social network systems API
- … and others

The topics and data sources listed above are just examples. Please try to solve issues in your daily life!

<b>HW3 requests:</b>

The DBMS should be on the AWS service, but the application can be either on your local environment or AWS (you will receive bonus points if you build your application on AWS). You can use any programming language to build your application with DBMS, and you can use any DBMS, including PostgreSQL and others.
Please submit a document in either Mandarin or English, codes for the application and/or data import, and a demo video (less than 3 mins) to the E3 system by 2022/6/25 23:59 (no late work will be accepted), the contents should include:
1. Motivations
2. Application description
3. Data sources and how you collect and import the data (manually or automatically)
4. Database schema (you can use the visualization tool in DBMS directly, and list constraints that are not in the figure)
5. The application's functions and the related SQL queries used for the function.
6. A demo video (less than 3 mins) with an introduction 

The scoring criteria:
- Database design (40%)
  - It should be in “good” design
  - The completeness of constraints
  - Index
  - Normalization vs. performance trade-off, explain your choice
- Integration between data and database (30%)
  - Database import methods and strategies
  - Database update strategies
- Integration between the database and your application (20%)
  - Does the application really need a database?
  - Queries or related codes
- Completeness of the document/introduction/application (10%)
- Creativity and others (10%)
