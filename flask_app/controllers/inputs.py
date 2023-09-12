from flask_app import app
from flask import render_template, request
import os
import openai
from dotenv import load_dotenv

load_dotenv()


# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/

import boto3
from botocore.exceptions import ClientError


OPENAI_KEY = os.environ.get("OPENAI_API_KEY")
print("OPENAI API KEY:", OPENAI_KEY)
openai.api_key = OPENAI_KEY

@app.route ('/', methods = ['GET', 'POST'] )
def index():
    
    return render_template('form.html')



@app.route('/openai', methods=['POST'])
def submission():
    #define input submitted from form to be used. It's the conent that will be changed to sound more like Ben wrote it
    user_input = request.form['input']

    #added try 
    try:
    #uses a built in function form openai installed in python
        response = openai.ChatCompletion.create(
            #setting the model to be used
            model="gpt-3.5-turbo",
            #argument that the API takes. You need to use a combination of role (system or user) and content to show the API what you want OpenAI to do
            messages=[
                {"role": "system", "content": "You are a helpful writing assistant."},
                {"role": "user", "content": """Here's a sample of writing I'd like to rewrtie in the toine and style of author Ben Barclay: Today Zendesk uses multiple companies to power our AI products. We currently use an open source version of Google BERT to power our NLP/sentiment analysis capabilities and OpenAI for LLMs to provide Generative AI (GenAI) capabilities. 
            Product is committed to working with OpenAI to see if they can meet our needs as an LLM provider but there may be challenges to working with them at scale that would push us towards working with other LLM vendors. While we’re attempting to go deep with OpenAI, in 2023 Zendesk has held meetings with Adept, Ai21 Labs, Cohere.ai, Stability, Anthropic and AWS Bedrock. We’re currently planning additional conversations with Anthropic, Google and AWS to learn more about their capabilities. 
                To date we’ve identified two main blockers with OpenAI: Data Locality and OpenAI’s Zero Data Retention policy restricting what use cases we can offer. We’re planning an Executive Briefing Center (EBC) meeting with OpenAI on September 8th to learn more about how they plan to address our needs. The goal of the meeting is to deepen our understanding of their business, their focus, and whether or not they’re committed to addressing issues that would prevent us from up-scaling our partnership.
                There’s still work to be done to clearly understand all of the capabilities, strengths and weaknesses of each provider. Tech Alliances will be supporting Zendesk Product with our ongoing evaluation of these partners, and the strategic partnership agreements that product decides to put in place to support the AI roadmap going forward."""},
                {"role": "assistant", "content": """Well, the landscape of our AI partnerships has certainly evolved since the last time I penned an update. The anticipation is palpable, and the stakes have never been higher. Just like the conversations I've had with fellow Zendeskians, the nuances of our AI journey have been a recurring theme. So, let's dive into the intricacies of our partnership with OpenAI.

                All insights shared here are based on our current understanding and ongoing evaluations.
                Over the past few months, Zendesk's AI landscape has been a mosaic of collaborations. While our NLP/sentiment analysis capabilities are powered by the open-source version of Google BERT, OpenAI's LLMs have been instrumental in driving our Generative AI (GenAI) capabilities. Our commitment to OpenAI is unwavering, but the road ahead is paved with challenges that might necessitate exploring other LLM vendors. In 2023 alone, our discussions have spanned across industry stalwarts like Adept, Ai21 Labs, Cohere.ai, Stability, Anthropic, and AWS Bedrock. And the conversations are far from over, with Anthropic, Google, and AWS waiting in the wings.

                Two primary roadblocks with OpenAI have emerged: Data Locality and their stringent Zero Data Retention policy. These challenges have put a damper on the range of use cases we can roll out. Our upcoming Executive Briefing Center (EBC) rendezvous with OpenAI on September 8th aims to shed light on their roadmap and whether they're poised to address our concerns. This meeting isn't just about problem-solving; it's about understanding their vision, their priorities, and gauging their commitment to our growing partnership.)"""},
                {"role": "system", "content": f"can you please rewrite {user_input} in the style of Ben Barclay using the samples previously provided? Feel free to restructure the writing however yous see fit to improve readability"}
            ]
        )
    # Extracting the assistant's reply
    #need to specify based on what's returned what you actually want to see
        assistant_reply = response['choices'][0]['message']['content']
        return assistant_reply

    except Exception as e:
        return str(e)
    
