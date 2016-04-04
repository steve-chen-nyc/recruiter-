# Bootcamp Recruiter 
###[Link to app on Heroku](http://bcrecruiter.herokuapp.com/)
![image](https://cloud.githubusercontent.com/assets/14185282/13909378/374e40f8-eee8-11e5-8167-de52c0023ee6.png)

### Overview 
Bootcamp Recruiter helps students graduating from the General Assembly WDI program connect with companies that have hired graduates in the past.  This is accomplished by allowing users to filter companies by the industry of interest, see key  profile information and provides a way for them to communicate in real time via Twitter. 

### Tools and Technology Used 
* Python 
* Django 
* PostgreSQL 
* Handlebars.js 
* jQuery 
* Django Rest Framework 
* Python Twitter 
* Python Social Auth 
* Twitter API 
* Giphy API 

### User Stories 
* All users are able to: 
  * Login using their Twitter Account 
  * Filter companies by industry 
  * View selected company profile which includes information such as: 
    * description 
    * website URL 
    * # of grads hired etc 
* Authenticated users are able to: 
  * View selected company Twitter profile page: 
    * View current timeline - 20 results with links 
    * #SAYHELLO by posting a tweet  
      * tweets that include certain keywords will be caught and users will be re-directed to a try again page which include          rotating giphies(from API) that communicates the error
      * built in counter which will prevent users from exceeding 140 character limit. Once limit has been reached counter            will hit zero and the text area will turn red
  * Unlock Hustlers feature which renders the most favorited & re-tweeted tweet once a day from an influencer with different backgrounds. Tweets are filtered so that only tweets from the past 7 days are eligible. Schedule as follows: 
    * Monday - Jack Dorsey 
    * Tuesday - Kobe Bryant 
    * Wednesday - Rick Ross 
    * Thursday - Dwayne "The Rock" Johnson 
    * Friday - Sophia Amoruso
    * Saturday - Shonda Rhimes 
    * Sunday - Barack Obama 

# Future Plans 
  * Connecting students and graduates with working alumni and GA outcome coaches via Twitter. 
    *An example could be a live Q&A via a Twitter chat or broadcasted live via Periscope
  * Implementing additional frontend features such as follow buttons etc.
  




