# Delivery logistic system

## About the project

Simple system to map the orders from the stores to the motorcycle couriers

### Installation and configuration

  - Configure the virtualenv:
    
    ```
    pip install virtualenv
    virtualenv venv
    source venv/bin/activate
    ```
  
  - Install the requirements:
    
    ```
    pip install -r requirements.txt
    ```

## Usage

  - To run the application:
    
    ```
    python app.py
    ```

  - To display the information from a specific motoboy:

    ```
    python app.py --motoboy <id_motoboy>
    ```

  - To run the tests:
    
    ```
    python -m pytest -v
    ```
