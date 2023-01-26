# Airflow project

#### By [Ruben Giosa](https://github.com/rgiosa10)

#### This repo showcases work with Airflow to leverage a DAG for automation

<br>

## Technologies Used

* Airflow
* Python
* Pandas
* Git
* Markdown
* NumPy
* `.gitignore`
* `requirements.txt`
  
</br>

## Datasets Used

1. [World Happiness Report](https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2019.csv)

</br>

## Description

This repo showcases work with Airflow to leverage a DAG for automation of the below steps:
* Extracts the data from the csv file
* From the World Happiness Report data, creates a Python dictionary that has the country names as keys, and the overall rank for that country as the value.
* Generates three JSON files with a randomly selected country and its rank from the dictionary.
* Then uses the three choices to create three Python operator tasks that run simultaneously. It leverages a python_callable to call a function that prints a string using the country name and its happiness ranking in a sentence.

#### DAG Structure:
<img src="imgs/architecture_diagram.drawio.png" alt="DAG diagram" width="640"/>

<br>

## Setup/Installation Requirements

* Go to https://github.com/rgiosa10/airflow-project-one.git to find the specific repository for this website.
* Then open your terminal. I recommend going to your Desktop directory:
    ```bash
    cd Desktop
    ```
* Then clone the repository by inputting: 
  ```bash
  git clone https://github.com/rgiosa10/airflow-project-one.git
  ```
* Go to the new directory or open the directory folder on your desktop:
  ```bash
  cd airflow-project-one
  ```
* open the directory in VS Code:
  ```bash
  code .
  ```

* Once in the directory you will need to set up a virtual environment in your terminal:
  ```bash
  python3.7 -m venv venv
  ```
* Then activate the environment:
  ```bash
  source venv/bin/activate
  ```
* Install the necessary items with requirements.txt:
  ```bash
    pip install -r requirements.txt
  ```
* Download the necessary csv files listed in the Datasets Used section
* With your virtual environment now enabled with proper requirements, open the directory:
  ```bash
  code .
  ```
* Upon launch please update the Google Cloud client and project details to configure it to load to your project

</br>

## Known Bugs

* No known bugs

<br>

## License

MIT License

Copyright (c) 2022 Ruben Giosa, Reed Carter, Chloe (Yen Chi) Le

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

</br>