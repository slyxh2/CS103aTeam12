'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'


#the following code creates the home page
@app.route('/')
@app.route('/home')
def about():
    ''' display a link to the general query page '''
    print('processing / or /homeroute')
    return f'''
    <h1> About Our Program </h1>
    <p>This program is a chatGPT webapp on which you can experience <br>
       the AI-powered searchmachine with some specific prompts designed <br>
       by our tech team.</p>
    <a href="{url_for('team')}">Team</a>
    <br>
    <a href="{url_for('index')}">The GPT prompts</a>
    <br>

    '''
    # return f'''
    #     <h1 color="red">GPT Demo</h1>
    #     <a href="{url_for('gptdemo')}">Ask questions to GPT</a>
    # '''


#the following code creates the team page
@app.route('/team')
def team():
    print("on the team page")
    return f'''
    <h1> Here is our tech team</h1>
    <h2>Ge Gao</h2>
    <p>
    I am a first year MS4 student From GSAS of Brandeis University. I come from<br>
    China and am happy to find a large and precoious Chinese community here in Greater <br>
    Boston. I like wathcing movies, exploring restaurants of various cuisine and watching <br>
    pro sports. Teams I support includes Celtics,Arsenal and Ferrari F1.<br>
    <br>
    In this projects I created the basic web structure as the carrier of content. Also I created <br>
    my own page which let ChatGPT analyze if the sports team the user asks for has a chance in <br>
    this year's champion race. To be honst, the result is quite inaccurate as chatGPT mostly reies <br>
    data before 2022.
    </p>
    <h2>Xueyan Huang</h2>
    <p>
    Hi, this is Xueyan. I am currently enrolled in the Master of Computer Science program<br>
    I have a deep interest in Frontend/Full-Stack development.<br><br>
    I created copy the gpy.py and gptwebapp.py and push them in github repository.<br>
    I also built the Food Taster chatGPT query web.<br>
    </p>
    <h2>Ting Xu</h2>
    <p>
    Hi, this is Ting. I am from Ningbo, China and I love swimming and singing. <br>
    As a product manager for Fund Management at my last company, I was instrumental in establishing the firm’s financial accounting system. <br>
    I witnessed tremendous changes brought about by information technology. And it ignites my strong passion to delve into the computer science field.<br>
    <br>
    For this GPT app, I built a query page about travel plan. When people travel, they always worry about local attractions and food. <br>
    If you can make a strategy before traveling, you can save a lot of time and improve the quality of travel.
    </p>
    
    
    <a href="{url_for('about')}">BACK</a>
    '''

# the following code creates the index page which lists the prompts designed by each of us
@app.route("/index")
def index():
    print("on the index page")
    return f'''
    <h1> Here you can try the chatGPT answerMachine by each of us</h1>
    <a href="{url_for('ge_form')}">Ge Gao's sports Champion Predictor</a>
    <br>
    <a href="{url_for('huang_form')}">Xueyan Huang's food taster</a>
    <br>
    <a href="{url_for('ting_form')}">Ting Xu's Travel Helper</a>
    <br>
    <br>
    <a href="{url_for('about')}">BACK</a>

    '''
# the following code creates Ge Gao's form page
@app.route("/ge_form",methods=['GET', 'POST'])
def ge_form():
    if request.method=='POST':
        teamName=request.form['prompt']
        answer=gptAPI.sport_analyst(teamName)
        return f'''
        <h1>The Champion Predictor</h1>
        <pre style="bgcolor:yellow">{teamName}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('ge_form')}> predict another team</a>
        <br>
        <a href="{url_for('index')}">BACK</a>
        '''
    else:
        return f'''
        <h1>The Champion Predictor</h1>
        which team you want to ask about?
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        <br>
        <a href="{url_for('index')}">BACK</a>
        '''
# Xueyan Huang's Form
@app.route('/huang_form', methods=['GET', 'POST'])
def huang_form():
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.food_taster(prompt)
        return f'''
        <h1>Xueyan Huang's food taster</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('huang_form')}> Try another food</a>
        <br>
        <a href="{url_for('index')}">BACK</a>
        '''
    else:
        return '''
        <h1>Xueyan Huang's food taster</h1>
        Please enter the food name
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
 
 # Ting Xu Travel Helper page
@app.route("/ting_form",methods=['GET', 'POST'])
def ting_form():
    if request.method=='POST':
        prompt=request.form['prompt']
        answer=gptAPI.travel_helper(prompt)
        return f'''
        <h1>Your Travel Helper</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        <br>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('ting_form')}> Ask something else! </a>
        <br>
        <a href="{url_for('index')}">BACK</a>
        '''
    else:
        return f'''
        <h1>Your Travel Helper</h1>
        <p>Are you tired of looking for popular spots when you are planning your travels? Are you having trouble finding local delicacies? <br>
        Now, this Travel Helper can help you solve your troubles! <br>
        As long as you enter the destination, it can answer you!
        </p>
        Please enter the destination you want to visit?
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        <br>
        <a href="{url_for('index')}">BACK</a>
        '''
        
        
@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)