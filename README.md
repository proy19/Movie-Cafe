# Movie Cafe

## Set Up: Tools and Technologies
* Installations: Python Flask, Requests, Python-Dotenv, psycopg2-binary,postgresql, Flask-SQLAlchemy, Flask-Login, Node (or npm on WSL), React
* API's: TMDB API (requires authentication), Wikimedia REST API (no authentication)
* Files: .env (contains the TMDB API Key variable: API_KEY, DATABASE_URL, SECRET_KEY)

## How to run the app (type in terminal):
* Navigate to the project directory: cd {directory name}
* Install the node modules: npm ci
* Build the app for production: npm run build
* Run the app: python3 app.py

## Technical Issues 
<ins>Milestone 1</ins>
* The Wikipedia API was difficult to sort through to get the full page url. To solve this, I google searched "how to get a page url from the Wikipedia API". And a StackOverFlow post helped me dynamically fetch the page id and concatenate it to a base url. 

* Kept getting errors when fetching the correct wiki url for the related tmdb movie. To solve this, I used a python dictionary with the tmdb page_id as key and the wiki movie title as the value, in order to connect them. 

* Problem with installing Heroku because my XCode wasn't up to date. I deleted XCode from my computer and that solved the isuue. 

<ins>Milestone 2</ins>
* Flash was giving me an error because I was missing a secret key. I added a secret key to my .env file and that solved the problem. 

* NameError when getting the information from the data fields. I imported request and that solved the issue. 

* Difficulties when querying the Review database by a specific user, because I didn't know the specific line of code. I looked through one of the class lecture and a specfic PPT slide helped me filter specific rows from my database.

<ins>Milestone 3</ins>
* TypeError when trying to map the reviews json data on the profile page. I looked up some useState code examples on stackoverflow, and the error occured because I had initialized my state variable as a string instead of an array. So I changed my useState(" ") to useState([]). And that cleared the error. 

* The input fields on my profile page wasn't reflecting any change when the user is typing into it. I looked up HTML input fields on stackoverflow and they were un-editable because I had set a value attribute to them. I changed the value attribute to devaultValue, and that made the fields editable. 

* Internal Server Error when I linked my profile page into the main page. The error occured because I used url_for to link the page. I changed the href to "./static/react/index.html", and that solved the issue.

## Project Experience: Hardest Part, Valuable Learnings
<ins>Hardest Part</ins>
* The API's were a bit difficult to implement. As different API's have different requirements. There were also a ton of information regarding the APIs, it was difficult to sort through which ones are relevant and which parameters to use. 

* Heroku deployment was frustrating for the second milestone. Because I had to include new info on the requirement.txt as well as change the Database URL

<ins>Valuable Learnings</ins>
* I feel like I finally have the confidence to code a web application from scratch.
I tried to build personal projects in the past, but it felt very frustratiing and directionless. But through this project, I got to learn and actively apply my knowledge of backend and frontend technolgies (such as python flask, databases, APIs, react etc.). I'll be able to use this knowledge in future projects as well as in the industry. 

## Expectations: Implementing v/s Project Planning
* The Flask-Login documentation was kind of overwhelming at first to get through than I had first planned. It seemed like a lot of new information to understand. I looked through a YouTube tutorial on Flask-Login and that helped me break it down in simpler steps to create my login system. 

* The review/rating section was surprisingly easy to implement. I had originally planned to follow how I did HW6, with just more columns in my database. And I had minimal-to-no issues implementing my plan. The only difference was that I had to make more columns. 
