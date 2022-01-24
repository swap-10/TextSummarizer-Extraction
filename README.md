# TextSummarizer-Extraction
Extraction based Text summarizing using NLTK. Can be used as a command line tool.

## Setup
### Clone the repo

```git clone https://github.com/swap-10/TextSummarizer-Extraction```

### Create a python virtual environment (recommended)

```python3 -m venv path/to/new/virtual/env```

On Windows:

```py -m venv path\to\new\virtual\env```


**Activate the Virtual Environment**

```source path/to/virtualenv/bin/activate```
(For bash)

On windows:
```path\to\virtualenv\Scripts\activate.bat```



**Check if the shell shows the virtual environment activated:**

```(name-of-your-venv) shell-prompt$```

The name of the virtual env created should become part of the shell prompt, enclosed within parentheses.

### Enter the cloned repo

```cd path/to/local/repo```

Or if you are in the location the repo was cloned to, simply:

```cd TextSummarizer-Extraction```

Now you should be in the base directory of the repo (with files such as README.md and requirements.txt in current directory)

### Install the required packages

Run:

```pip install -r requirements.txt```

Now you're all set!

<br>
<br>

## Using the summarizer

The summarizer reads text from a text file. Place the text you want summarized in a text file.<br>
Then run the python file ```summarizer.py``` from the terminal

```python3 summarizer.py filename.txt 10```

```py summarizer.py filename.txt 10``` (for Windows)

This will print the top 10 lines extracted from the text file as output on the terminal.
If the number of lines is not provided as an argument, 5 is taken as default.

You can also specify a file for the output to be written to. In this case the output will not be printed on the terminal.

```python3 summarizer.py article.txt 12 summary.txt```

<br>

>*Note: When using the command line argument to print output to a file, the number of lines for summary (here 12), must be specified*

>*Note: If the file specified for output already exists, it's contents will be overwritten*

<br>

*This repo is inspired by: https://github.com/edubey/text-summarizer*

*Sample text taken from BBC article at: https://www.bbc.com/news/uk-60010608 is only for the purpose of demonstration. All credits go to the owners.*

<br>
<br>

This is not intended to be a rigorous or fit-for-purpose tool and is only meant for education/exploratory use, or to have fun.

This repository and my original work within it is licensed under the terms of the MIT License. (Refer the LICENSE file)

## Have fun!