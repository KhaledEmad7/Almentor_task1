
# About the app

This app start a python server using **Flask** Then it sets a link to make **POST request** on it.\
The post request should have the [input.csv](/input.csv) file in it.\
Then it will return a JSON response in specific and more clean format .

# Quick start 
- ## Installation
    First install **python3** from [here](https://www.python.org/downloads/)\
   Then run the following to install **flask**:\
    `pip install flask`

- ## Running the app
   First you need to start the app server by running:\
   `python3 app.js`\
   Or you can simply use a python IDE and run the **app.js** file from it\
   <br>
   The app will run automaticaly on:\
   `http://192.168.1.13:5000`\
   <br>
   Now make POST request to the following link:\
   `http://192.168.1.13:5000/answers`\
   [Postman](https://www.postman.com/) can be used to make this request.\
   <br>
   In body check `form-data` then make `KEY = input`\
   Then add the [input.csv](https://github.com/KhaledEmad7/Almentor_task1/blob/main/input.csv) in the **VALUE** part\
   <br>
   Then press **Send** and JSON output should appear in response
