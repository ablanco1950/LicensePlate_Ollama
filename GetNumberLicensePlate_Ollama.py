#
# https://john-tucker.medium.com/ollama-by-example-part-1-22f01acc1821
# Quickstart - Ollama 
# https://docs.ollama.com/quickstart

dirname="C:\LicensePlate_Ollama\Test1"

# Preguntando a la IA de Bing
# how call ollama from a python program
#  Modified by Alfonso Blanco

import ollama

def query_ollama(model: str, prompt: str) -> str:
    """
    Query an Ollama model and return the generated text.
    """
    try:
        # Send request to Ollama
        response = ollama.chat(model=model, messages=[
            {"role": "user", "content": prompt}
        ])
        
        # Extract and return the model's reply
        return response['message']['content']
    
    except Exception as e:
        return f"Error: {e}"

import os
import re
def loadimages (dirname):

     imgpath = dirname + "\\"
     
     #images = []
     TabLicenses=[]
     TabFilePath=[]
    
     print("Reading imagenes from ",imgpath)
     NumImage=-2
     
     Cont=0
     for root, dirnames, filenames in os.walk(imgpath):
        
         NumImage=NumImage+1
         
         for filename in filenames:
             
             if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
                 
                 
                 filepath = os.path.join(root, filename)
                 License=filename[:len(filename)-4]
                 
                 TabFilePath.append(filepath)
                 TabLicenses.append(License)
                 
                 Cont+=1
     
     return  TabFilePath, TabLicenses
     
# MAIN


TabFilePath, TabLicenses= loadimages (dirname)
    
model_name = "gemma3:4b"  # Change to your installed model # gemma 3:4b recognize images
user_prompt_fix ="what license plate is in "

ContHits=0
ContFailures=0

for i in range(len(TabFilePath)):
    user_prompt=user_prompt_fix + TabFilePath[i]

    print(user_prompt)
    
    result = query_ollama(model_name, user_prompt)
    
    print("Ollama response:\n", result)

    cadena=result
    pos=cadena.find("**")

    if pos== -1:
        cadena=""
    else:    
            cadena=cadena[pos+2:]
            #print(cadena)
            pos=cadena.find("**")
            if pos == -1:
                cadena=""
            else:   
                cadena=cadena[:pos]
                
    #print(cadena)
    if cadena==  TabLicenses [i]:
        print ("HIT the License Plate is " + cadena)
        ContHits=ContHits+1
    else:
        print ("FAILURE the License Plate is " + TabLicenses [i])
        ContFailures=ContFailures+1
    
print ( "HITS=" + str(ContHits))
print("FAILURES=" + str(ContFailures))
