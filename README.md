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

## Features
* Login System (User will be able to sign up with a username and login with the username on subsequent visit)
![Screen Shot 2022-04-01 at 3 06 20 PM](https://user-images.githubusercontent.com/57018537/161326245-99b83605-c11e-4071-b06e-12c997b6bf81.png)

* Main Page (When the user refreshes the page it will generate a new movie) 
![Screen Shot 2022-04-01 at 2 58 54 PM](https://user-images.githubusercontent.com/57018537/161325529-3dcb8c22-7097-4f20-b1ce-403a1077a335.png)

* Reviews Section (User is able to leave a review/rating for a particular movie) 
![Screen Shot 2022-04-01 at 2 59 09 PM](https://user-images.githubusercontent.com/57018537/161325675-85309774-62c9-4004-ae48-5e52a58d9092.png)

* Profile (Will display all the reviews a user has left. User is able to edit and delete a review)
![Screen Shot 2022-04-01 at 2 59 25 PM](https://user-images.githubusercontent.com/57018537/161325797-0be42b9a-41b4-4045-bd73-87e6d5025991.png)
