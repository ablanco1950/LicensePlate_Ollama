# LicensePlate_Ollama
A test to detect car license plates using Ollama.

Installation:

Download the project to a disk folder and extract the Test1.zip file, which contains a set of 12 Roboflow test images.

Download version gemma3:4b (this version provides image processing) from the Ollama downloads page: https://docs.ollama.com/quickstart

Run the downloaded OllamaSetup.exe, which provides a graphical interface for running queries to Ollama.

In the project runtime environment, install the Ollama module:

`pip install ollama`

Adjust line 6 of the GetNumberLicensePlate_Ollama.py program to specify the full path to the Test1 test file.

Run the program:

`python GetNumberLicensePlate_Ollama.py`

Ollama's responses and the evaluation of whether the query was successful will appear in the console. The images are named with the corresponding number car license plate.

Observations:

The results are poor, either due to a lack of parameter adjustment in the query file, the content of the prompt, or because Ollama is still learning. Furthermore, the results differ with each program run. Therefore, this project is expected to be modified in subsequent versions.

The attached file, LOGOllamaTest.docx, contains a console log of a run in which only one out of twelve license plates was correctly recognized.

References:

https://john-tucker.medium.com/ollama-by-example-part-1-22f01acc1821
https://docs.ollama.com/quickstart

Query Bing AI "how to call Ollama from a Python program"
