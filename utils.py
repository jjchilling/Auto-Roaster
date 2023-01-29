import os
import openai
import config
import replicate

openai.api_key = config.OPENAI_API_KEY

model = replicate.models.get("methexis-inc/img2prompt")
version = model.versions.get("50adaf2d3ad20a6f911a8a9e3ccf777b263b8596fbd2c8fc26e8888f8a0edbb5")

def roast(query):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Provide a Good Roast about {}".format(query),
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0)
    
    return response["choices"][0]["text"]

def compliment(query):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Provide a Nice Compliment about {}".format(query),
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0)
    
    return response["choices"][0]["text"]

def caption(impath):
    inputs = {
        'image' : open(impath, 'rb')
    }
    output = version.predict(**inputs)
    newOutput = output.split(",")[0]
    
    return newOutput

def finalRoast(impath):
    file = open("cachedText/roasts.txt", "a")
    r_string = roast(caption(impath))
    print(r_string)
    file.write("\n" + impath + " // " + r_string + "\n\n")

def finalCompliment(impath):
    file = open("cachedText/compliments.txt", "a")
    c_string = compliment(caption(impath))
    print(c_string)
    file.write("\n" + impath + " // " + c_string + "\n\n")
    