import marimo

__generated_with = "0.15.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from simple_salesforce import Salesforce

    import duckdb
    import pandas as pd
    return Salesforce, mo, pd


@app.cell
def _(Salesforce, pd):
    import dotenv

    dotenv.load_dotenv(dotenv_path=dotenv.find_dotenv(usecwd=True))

    #authvars = dotenv.dotenv_values
    uname = dotenv.get_key(dotenv_path=".env", key_to_get="SF_SANDBOX_USERNAME")
    pw = dotenv.get_key(dotenv_path=".env", key_to_get="SF_SANDBOX_CRED")
    sectoken = dotenv.get_key(dotenv_path=".env", key_to_get="SF_SANDBOX_SECTOKEN")

    #print(uname)
    #print(pw)
    #print(sectoken)

    sf = Salesforce(username=uname, password=pw, security_token=sectoken)

    data = sf.query("SELECT Id, Amount, Account.Name, CloseDate, StageName, CreatedDate, FiscalYear, IsClosed, IsWon, NextStep, Probability, Type FROM Opportunity LIMIT 50")

    pandas_df = pd.DataFrame(data)
    return pandas_df, sf


@app.cell
def _(mo, pandas_df):
    table_df = mo.sql(
        f"""
        SELECT UNNEST(records, recursive:=true) FROM pandas_df
        """
    )
    return (table_df,)


@app.cell
def _(table_df):
    import altair as alt
    # replace _df with your data source
    _chart = (
        alt.Chart(table_df)
        .mark_bar()
        .encode(
            x=alt.X(field='StageName', type='nominal', sort='descending'),
            y=alt.Y(field='Amount', type='quantitative', stack=False, aggregate='sum'),
            color=alt.Color(field='IsWon', type='nominal'),
            tooltip=[
                alt.Tooltip(field='StageName'),
                alt.Tooltip(field='Amount', aggregate='sum', format=',.2f'),
                alt.Tooltip(field='IsWon')
            ]
        )
        .properties(
            height=290,
            width='container',
            config={
                'axis': {
                    'grid': False
                }
            }
        )
    )
    _chart
    return


@app.cell
def _(mo):
    num_yrs_history = mo.ui.dropdown(
        options={1, 2, 3, 4, 5, 6, 7, 8},
        label="Select number of years past to use as query filter"
    )
    num_yrs_history
    return (num_yrs_history,)


@app.cell
def _(num_yrs_history, pd, sf):
    from datetime import datetime

    year_paramvalue = datetime.now().year - num_yrs_history.value

    report_querystr = "SELECT Id,Name,DeveloperName,FolderName,CreatedDate,LastViewedDate,LastRunDate FROM Report WHERE CALENDAR_YEAR(LastRunDate)<" + str(year_paramvalue) + " OR CALENDAR_YEAR(CreatedDate)<" + str(year_paramvalue) + " OR CALENDAR_YEAR(LastViewedDate)<" + str(year_paramvalue) +  " OR LastRunDate=null OR LastViewedDate=null" 

    print("generated query: ", report_querystr)

    reports = sf.query(report_querystr)

    reports_df = pd.DataFrame(reports)
    return (reports_df,)


@app.cell
def _():
    return


@app.cell
def _(mo, reports_df):
    mo.ui.table(reports_df)
    return


@app.cell
def _(mo, reports_df):
    reports_table_df = mo.sql(
        f"""
        SELECT UNNEST(records, recursive:=true) FROM reports_df
        """
    )
    return


if __name__ == "__main__":
    app.run()
