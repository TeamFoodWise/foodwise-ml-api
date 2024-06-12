
# Model Integration with FastAPI
## Root Dir
Root directory should looks like this:
```
root/
  |___ data/
  |     |___ clean_data.csv
  |___ src/
  |     |___ main.py
  |     |___ model.py
  |     |___ recommender.py
  |___ .gitignore
  |___ readme.md
  |___ requirements.txt
```
## Manually add `clean_data.csv` (for now)
Make a `data` directory under root folder and place the `clean_data.csv` inside of it. (still figuring out how to remotely download the dataset)

## To run the server
1. To run the app in your localhost, create a virtual environment
    ```
    python -m venv env
    ```
2. Activate the environment. For windows:
    ```
    env\Scripts\activate
    ```
3. Install dependencies, provided in `requirements.txt`
    ```
    pip install -r requirements.txt
    ```
4. Run the fastAPI server in the root directory using this commmand. The default url and port will be `http://127.0.0.1:8000`
    ```
    uvicorn src.main:app
    ```
## Test with Postman
In your localhost...

![image](https://github.com/GilbertImmanuel/FoodWiseML/assets/89509266/f1399876-8e0d-4ec9-9e05-60b0b1033da7)