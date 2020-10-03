# Auto Google Form Filler
Here's a python script that'll automatically fill out a google form with the google account and credentials that you give it. Running the script will take approx. 5 seconds to complete.

## Prerequisites:
* Python 3
* Follow instructions from steps 1.2 - 1.4 in the [Python Selenium Docs](https://selenium-python.readthedocs.io/installation.html)
* Find your google form link and look at `example.json` for further instruction

## How it works:
 1. The script looks for a `creds.json` file in the same directory as it is in. The `json` file should match the format of `example.json` (__If the format doesn't match, unexpected behavior _WILL_ happen.__)
 2. It fires up a webdriver of your choice with selenium.
 3. It submits your form with the entries you have on your `json` file