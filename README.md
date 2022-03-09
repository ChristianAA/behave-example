# API testing example with Behave

This repository contains the base setup project for testing an API, using Python and Behave.

Spotify API is used as Example

# Requirements

* Python 3.10.X
* pip and setuptools
* [venv](<https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>) (recommended)

# Instalation

1. Download or clone the repository 
2. Open a terminal
3. Go to the project root directory.
4. Create a virtual environment: `py -m venv venv`
5. Activate the virtual environment executing the following script: `.\venv\Scripts\activate`
6. Execute the following command to download the necessary libraries:  `pip install -r requirements.txt`

# Configuration

1. Setup the Spotify OAuth Token in the "token" variable in "/features/steps/request_steps.py" file.

# Test Execution

1. Open a terminal
2. From the project root directory run: `behave -f html -o results/behave-report.html`

# Results

1. A result file (behave-report.html) will be generated in the "/results" folder

# Links
   
   [Behave - Github Repo](<https://github.com/behave/behave>)
   
   