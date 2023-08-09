# 🌟argai 

Turn your existing code into 🤖 Agents and 📖 Documentation

### Quickstart
`pip install argai`

`export OPENAI_API_KEY="..."`

```python
import openai
openai.api_key = "..."
```

Make your functions intelligent and queried via natural language:
```python
def create_file(filename, text):
    with open(filename,'w') as f:
        f.write(text)
        return {"status" : "success", "filename" : filename}

from argai import ArgFunction

af = ArgFunction(create_file)

result = af.func_call("Create a file called language.csv with all the programming languages available.")
```

Print logs to keep track of the progress:
```
1: 💬: Create a file called language.csv for the top 10 most popular programming languages and its complexity.
    📝 Calling LLM
    🏃 Running function: create_file(filename='language.csv', text='Language,Complexity\nPython,Low\nJavaScript,Medium\nJava,High\nC++,High\nC#,Medium\nRuby,Low\nPHP,Medium\nSwift,Medium\nGo,Medium\nTypeScript,Medium')
    ✔️ Sucessfull, result: {'status': 'success', 'filename': 'language.csv'}
2: 🌟: Ran create_file, result: {'status': 'success', 'filename': 'language.csv'}
    📝 Calling LLM
3: 🤖: I have created a file called `language.csv` with the information of the top 10 most popular programming languages and their complexity.
```

Final output: `result.output`
```
{'status': 'success', 'filename': 'language.csv'}
```



## ❓ What is this?
LLM function calling is the ability to describe functions to LLMs and have the LLMs infer the input of the functions based off natural language query. For example:
- “Email Anya to see if she wants to get coffee next Friday” ->
```python
send_email(to="anya@gmail.com", body="Hey Anya, do you want to get coffee this Friday? Let me know what time works best for you" )
```
- “Who are our highest spending customers” ->
```python
sql_query(query="SELECT customer, spend FROM CUSTOMERS ORDERED BY spend DESC;")
```

This library aims to help you develop function calling capabilities for your functions and build applications that utilizes function calling. For example:

🤖 Agents
- Create autonomous agents that can continuously execute and run your functions based off a goal.

💬 Chatbots with 'Plugins'
- Create chatbots that can execute your function like ChatGPT with Plugins.

✈️ Copilots
- Automatically make your functions callable via natural language for copiloting.

📖 Documentation
- Automatically create guides and documentation for your functions.

## More examples

### 🌟 1. Function Calling

Calling a function with just natural language. Below is an example of a simple function of creating file.
```python
from argai import ArgFunction

def create_file(filename, text):
    with open(filename,'w') as f:
        f.write(text)
        return {"status" : "success", "filename" : filename}

af = ArgFunction(create_file)

result = af.func_call("Create a file called language.csv with all the programming languages available.")
```

<details><summary>Output</summary>

logs:
```
1: 💬: Create a file called language.csv for the top 10 most popular programming languages and its complexity.
    📝 Calling LLM
    🏃 Running function: create_file(filename='language.csv', text='Language,Complexity\nPython,Low\nJavaScript,Medium\nJava,High\nC++,High\nC#,Medium\nRuby,Low\nPHP,Medium\nSwift,Medium\nGo,Medium\nTypeScript,Medium')
    ✔️ Sucessfull, result: {'status': 'success', 'filename': 'language.csv'}
2: 🌟: Ran create_file, result: {'status': 'success', 'filename': 'language.csv'}
    📝 Calling LLM
3: 🤖: I have created a file called `language.csv` with the information of the top 10 most popular programming languages and their complexity.
```

`result.output`
```
{'status': 'success', 'filename': 'language.csv'}
```
</details>


#### ️‍🩹 1.2 Function calling with self-healing

When the LLM hallucinates we can make it self heal/repair. You just add `max_attempts` as a argument to the function and it will be attempting to fix itself till `max_attempts` or a successfull call is made:
```python
af.func_call(
    "Create a python file that builds a linear regression model for a csv called 'data.csv'",
    max_attempts=5,
)
```
The results of a function won't be appended until `max_attempts` is reached to save tokens + context limit.


#### ️⏭️ 1.3 Consecutive function calling

Sometimes a query will require a function being called not once but multiple times consecutively. In those scenarios set a `max_calls` and it will be called continuously till `max_calls` or an answer is reached.
```python
af.func_call(
    "Create a file called data.csv with top 10 grossing movie of all time. Then create a python file that will create a linear regression model on that csv.",
    max_calls=5,
    max_attempts=5,
)
```

<details><summary>Output</summary>

logs:
```
1: 💬: Create a file called data.csv with top 10 grossing movie of all time. Then create a python file that will create a linear regression model on that csv.
    📝 Calling LLM
    🏃 Running function: create_file(filename='data.csv', text='Movie,Revenue\nAvengers: Endgame,2797800564\nAvatar,2787965087\nTitanic,2187463944\nStar Wars: The Force Awakens,2068223624\nAvengers: Infinity War,2048359754\nJurassic World,1670516444\nThe Lion King,1656962239\nThe Avengers,1518815515\nFurious 7,1515047671\nFrozen II,1450026933')
    ✔️ Sucessfull, result: {'status': 'success', 'filename': 'data.csv'}
2: 🌟: Ran create_file, result: {'status': 'success', 'filename': 'data.csv'}
    📝 Calling LLM
    🏃 Running function: create_file(filename='linear_regression.py', text="import pandas as pd\nfrom sklearn.linear_model import LinearRegression\n\n# Load the CSV file\ndata = pd.read_csv('data.csv')\n\n# Prepare the data\nX = data['Revenue'].values.reshape(-1, 1)\ny = data['Movie'].values\n\n# Create a linear regression model\nmodel = LinearRegression()\n\n# Fit the model\nmodel.fit(X, y)\n\n# Print the coefficients\nprint('Intercept:', model.intercept_)\nprint('Coefficient:', model.coef_)")
    ✔️ Sucessfull, result: {'status': 'success', 'filename': 'linear_regression.py'}
3: 🌟: Ran create_file, result: {'status': 'success', 'filename': 'linear_regression.py'}
    📝 Calling LLM
4: 🤖: I have created a file called "data.csv" with the top 10 grossing movies of all time. I have also created a Python file called "linear_regression.py" that creates a linear regression model on the provided CSV data.
```

`result.output`
```
{'status': 'success', 'filename': 'linear_regression.py'}
```
</details>

### 💾 2. Function Calling from Multiple functions

Calling from a list of functions with just natural language, the LLM will automatically decide which function to use.
```python
from argai import ArgFunctionStorage

def create_file(filename, text):
    """Create a file from raw text"""
    with open(filename,'w') as f:
        f.write(text)
        return {"success":True}

import pandas as pd
def pandas_query(csv_file, query):
    """Run a pandas query on a csv file"""
    df = pd.read_csv(csv_file)
    return df.query(query)

fs = ArgFunctionStorage(verbose=True)

fs.register(create_file)
fs.register(pandas_query)
fs.func_call(
    "Create a file called language.csv with the top 10 most popular programming languages available.", 
)
```
#### ⏭️ 2.2 Consecutive function calling on multiple functions

This will be able choose and run different registered functions till `max_calls` or an answer is reached.
```python
fs.func_call(
    "Create a file called language.csv with the top 10 most popular programming languages available, after that show me only the low complexity languages.", 
    max_calls=10,
)
```
#### 🩹 2.3 Multiple functions with self-healing

Just like single function calling, when a function fails you can repair it with self-healing. 
```python
fs.func_call(
    "Create a file called language.csv with the top 10 most popular programming languages available, after that show me only the low complexity languages.", 
    max_calls=10,
    max_attempts=5
)
```

## 🙌 Contributing
Contributions of all kinds are extremely welcome!

## What is with the 🌟?
Last but not least, the most important question and answer:
```def func(*arg)```
->
```def func(🌟arg) ```