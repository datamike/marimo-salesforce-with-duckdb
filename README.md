## Purpose:

Use the marimo Python notebook in combination with the simple-salesforce, pandas, and duckdb libraries to connect to a Salesforce org, run SOQL queries, visualize results, and more. 

### Prerequisites:

- Tested with Windows 10, but should also work fine with Mac and Linux.  The code also works with adjustments on molab.mario.io
- Python 3.20 (min.) 
- Make

Note:  There is no need to install Marimo locally. The makefile uses a venv command to build a disposable Python environment (and Marimo is part of that build process).

## Steps to Run the Marimo Notebook

1. Add a .env file with the following keys and their respective Salesforce environment values:
   
      A. SF_SANDBOX_USERNAME=

      B. SF_SANDBOX_CRED=

      C. SF_SANDBOX_SECTOKEN=
  
2. From the source directory, run:
   
   make setup-python

3. After the above command completes, run:

   make run-marimo


<br>

---

<br>

That's it!  Marimo should then be running on your local environment and the editor UI will open up in a browser window.

<br> 

---


### References:

[https://www.salesforceben.com/ - How to identify Unused Salesforce Fields With Python](https://www.salesforceben.com/how-to-identify-unused-salesforce-fields-with-python-a-step-by-step-guide/)


   
