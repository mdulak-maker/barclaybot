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
                {"role": "user", "content": """Here's a sample of writing I'd like you to based your future writting suggestions on. The author of this content is Pascal Pettinicchio: Technology partnerships will be a critical enabler of our customer intelligence vision. Many of these partners constitute “sources” of customer intelligence, such as feedback (e.g. survey providers, reviews), behavioral data (e.g. CDPs), user information (e.g. sales CRM), and more; though we have already recruited many of these partners, we will generally need to make the case for them to send more data to the appropriate Zendesk endpoints). We will also need to approach downstream partners that can help businesses digest and act on the insights we generate – potentially including reporting / analytics partners, marketing automation providers, and more. If past is prologue, we will need to provide incentives (e.g. extensive co-marketing) to early partners as well as have sufficient partner support resources (e.g. solution architect) to collaborate on the new integration; we may also need to build critical integrations via our Strategic Integrations team or Commissioned Integrations model. Our platform roadmap must continue to advance in support of these partners, and we should continue to leverage the marketplace and app framework so customers are able to quickly “install” partner integrations critical to customer intelligence. In addition to advancing our technology partner ecosystem, we will use our partnership and engagement with AWS to identify services and adoption incentives that can accelerate our customer intelligence product roadmap. We can also collaborate with Product and Engineering to evaluate strategic customer intelligence partnership opportunities (e.g. OEM / resell of VOC capabilities).

                We will continue to scale our joint GTM activities with tech partners across the board in 2022, including a plan of increasing AWS-sourced business by 125%+, as part of the $100M 2021 partners + alliances bookings OKR. Assuming a successful first wave of our technology partner resell motion, we can expand to include other common required integrations. Many of these initiatives will tax our operations teams should we continue business as usual – without investing in automation, we anticipate the incremental growth in the AWS joint GTM will result in three man-years of additional work, while the initial resell model is highly manual and will require a custom SOW and quote for every transaction, additional deal desk and revenue operations scrutiny, and tailored sales compensation, revenue recognition, and customer support processes. Meanwhile, the Alliances team continues to devote a growing proportion of its time to ensuring Salesforce opportunities and accounts appropriately reflect partner involvement. Without incremental technology investment, partner operations requirements will continue to grow in line or above total transaction volume and faster than headcount growth. We do have the opportunity to “future-proof” our joint GTM with AWS through a set of IT/CRM integrations – this will require roughly $450K in consulting spend with dedicated oversight and modest development resources from IT/CRM. 

                Most of the Alliances value proposition to date has been realized indirectly – technology partnerships are critical to winning new customers and growing our existing book of business, but these partnerships largely do not generate Zendesk revenue on their own. Historically, we have philosophically opposed direct technology partner monetization, perceiving taxes like platform fees, forced revenue shares, mandated billing APIs, etc. as antithetical to being an open platform. Frankly, we still do. At the same time, we believe there are significant revenue opportunities we can pursue that are not a blatant tax but do recognize and recoup a small amount of the value Zendesk brings to the partnership. Examples of these opportunities include paid marketing activities, preferred referral partnerships with revenue shares, the reselling initiatives we are piloting, and even optional billing APIs with revenue shares – the key principle being that we offer partners fully optional levers for incremental value creation above and beyond the ordinary course of our partner program, and then we capture part of that incremental value. Partner-influenced product usage - such as WhatsApp fees and incremental SunCo monthly active user fees - also represent future monetization opportunities that we plan to monitor over the course of 2022. While we are still in the early days of direct revenue generation for Technology Alliances, the next few months will include structured exploration and incubation with the aim of bringing findings and recommendations to our 2H E-staff update.
                """},
                
                {"role": "system", "content": f"can you please rewrite {user_input} in the style of Pascal Pettinicchio using the samples previously provided? Feel free to restructure the writing however yous see fit to improve readability. Please keep the length of the response relatively similar to the sample provided"}
            ]
        )
    # Extracting the assistant's reply
    #need to specify based on what's returned what you actually want to see
        assistant_reply = response['choices'][0]['message']['content']
        return assistant_reply

    except Exception as e:
        return str(e)
    
