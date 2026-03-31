Text Preprocessing in NLP

About This Project
This project is a basic implementation of text preprocessing in Natural Language Processing (NLP). The idea is to take raw text and clean it so that it becomes easier to analyze or use in further applications like machine learning.
Instead of working with messy text, we process it step by step to make it structured and meaningful.

What This Project Does
The program performs the following operations on a given text:
	•	Converts all text to lowercase
	•	Removes punctuation marks
	•	Breaks the text into words (tokenization)
	•	Removes common words (stopwords) like is, the, and

How It Works
The input text is taken from a file, processed using Python and NLTK, and the final cleaned output is stored in another file.

Example
Input
Hello! This is a simple example, showing how text preprocessing works.
Output
['hello', 'simple', 'example', 'showing', 'text', 'preprocessing', 'works']

Functions Used in Preprocessing
Below is a step-by-step transformation of a single sentence to demonstrate each preprocessing stage.
Input Sentence
Hello! This is an example, showing how preprocessing works.

1. Convert to Lowercase
Function Used:
text.lower()
Output:
hello! this is an example, showing how preprocessing works.

2. Remove Punctuation
Function Used:
text.translate(str.maketrans('', '', string.punctuation))
Output:
hello this is an example showing how preprocessing works

3. Tokenization
Function Used:
word_tokenize(text)
Output:
['hello', 'this', 'is', 'an', 'example', 'showing', 'how', 'preprocessing', 'works']

4. Stopword Removal
Function Used:
[word for word in tokens if word not in stopwords.words('english')]
Output:
['hello', 'example', 'showing', 'preprocessing', 'works']

This clearly shows how raw text is gradually cleaned and converted into meaningful tokens.

Files in This Project
	•	main.py → Runs the program
	•	preprocessing.py → Contains the preprocessing logic
	•	sample_input.txt → Input text file
	•	output.txt → Output after processing
	•	requirements.txt → Required libraries.

How to Run
	1	Install the required library: pip install -r requirements.txt
	2	Run the program: python main.py
	3	Check the output in output.txt

What I Learned
Through this project, I understood:
	•	How raw text is cleaned before processing
	•	The importance of tokenization
	•	Why stopwords are removed
	•	Basic use of the NLTK library


Author
Rudrakshi Bedi



