'''
Demo code for interacting with GPT-3 in Python.

To run this you need to 
* first visit openai.com and get an APIkey, 
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY="......."  # in bash
% python3 gpt.py

On Windows:
% pip install openai
% $env:APIKEY="....." # in powershell
% python gpt.py
'''
import openai


class GPT():
    ''' make queries to gpt from a given API '''
    def __init__(self,apikey):
        ''' store the apikey in an instance variable '''
        self.apikey=apikey
        # Set up the OpenAI API client
        openai.api_key = apikey #os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"

    def getResponse(self,prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response

    '''
    this method asks chatGPT if the following team can win the champion this year
    (any sports including soccer,basketball,F1 etc) and provide explanation
    '''
    def sport_analyst(self,teamName):
        prompt="Can this team win the champion of this year? please explain"
        res=self.getResponse(prompt+teamName)
        print(res)
        return res
    '''
    this method tell you how the food taste like
    '''
    def food_taster(self,foodName):
        prompt="Tell me how the follow food taste."
        res=self.getResponse(prompt+foodName)
        print(res)
        return res
    
    ''' ask GPT about the destination's popular tourist attraction and local foods '''
    def travel_helper(self,destination):
        prompt="Help me find the top10 famous scenic spots and popular restaurants in the following places, and express them in lists."
        res=self.getResponse(prompt+destination)
        print(res)
        return res
    

if __name__=='__main__':
    '''
    '''
    import os
    g = GPT(os.environ.get("APIKEY"))
    print(g.getResponse("what does openai's GPT stand for?"))
    g.sport_analyst()