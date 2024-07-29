# Web Testing Using Restricted Natural Language #

## Intro ##

This is work is attached alongside the submission entitled "Web Testing Using Restricted Natural Languague" submitted for review for ACCMI 2024


## High Level Structure ##

This repository is divided into three main component. 

- A ReactJs web application to create/run/view tests using natural language
- A Flask backend which is responsible to convert the natural language test into a selenium script
- A Flask socket server to communicate the screenshots between the scripts and the UI to view the results inside the React app.


## Demo ##  
Inside the submission folder you can find a demo of how the application is being used to automate the sign in mechanism of a popular voice/video chatting application called discord.



# Initial Setup #

### Requirements ###
Here's a list of software requirements that you need to have installed before attempting to run the tool:

- Python3.6 or later
- NodeJs - a working version is 19.7.0
- NPM - a working version is 9.5.0
- ChromeDriver installed and on PATH

WARNING :<i>You need to have an OpenAI API key, which you might not have, you can refer to the video demo if you cannot run the application</i>


Additionally you need to install the necessary modules to run the three components.

For the python requirements you can execute the following command:

```bash
    pip install -r requirements.txt
```

For the React application, navigate to the website directory by calling:

```bash
cd website
```

from inside the root directory and then call

```bash
npm install
```
which will download the necessary node modules.


You should be all set from here!

# Running the application #

You can start by running both the python servers.
In two different shells run the following:


```bash
python socketServer.py
```

```bash
python mainserver.py
```

From there you can just run the react application by navigating into the website directory

```bash
cd website
```

And then running:

```bash
npm start
```

The websocket server runs on port 5555 <br>
The main server runs on port 5000<br>
The React app runs on port 3000 <br>

Make sure that you currently do not have any applications running on those ports to avoid probems.


### Using the application ###

- The UI is exteremly simple, if you want to create a test for certain website, you just fill the url along with the test name.

- Then you can start creating sentences like the one described in the paper.

- When you finish creating the test, you can press the Finish button to save the test.

- To see the ceated tests, you can press the Tests button, you will get a list of the tests already created.

- You can execute each one of those tests, by pressing the corresponding Run Test button.


- Similarity scores for each element search are logged into the "scores.txt" file. This file is used to replicate the statistical results that we published in the paper.

- You can run the visualization scripts to see the scores distributions
In case you couldn't run the application, you can still see the results by changing the file in the visualization scripts from "scores.txt" to "scores-backup.txt"

- For your convenience, we have included a couple of tests that we have written.


### 
