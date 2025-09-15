#Purpose:

#Prerequisites:

Python 3.20 (min.)
Make

Note:  There is no need to install Marimo locally. The makefile uses a venv command to build a disposable Python environment (and Marimo is part of that build process).

#Steps to Run the Marimo Notebook

1. Add a .env file with the following keys and their respective Salesforce environment values:
   a. SF_SANDBOX_USERNAME=
   b. SF_SANDBOX_CRED=
   c. SF_SANDBOX_SECTOKEN=
   
  
3. From the source directory, run:
   
   make setup-python

4. After the above command completes, run"

    make run-marimo


That's it!  Marimo should then be running on your local environment.




#References:

[https://www.salesforceben.com/](https://www.salesforceben.com/how-to-identify-unused-salesforce-fields-with-python-a-step-by-step-guide/)

   
