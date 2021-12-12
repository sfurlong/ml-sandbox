To create or recreate virtual environment
1. virtualenv [my_venv_name] to create a new environment
2. "$ source [my_venv_name]/bin/activate" to activate the new environment
3. "$ pip install -r requirements.txt" to install the requirements in the current environment

#Add the environment to the Jupyter Notebook
python -m ipykernel install --user --name=<my_env_name>
