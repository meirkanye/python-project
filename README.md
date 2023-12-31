

# FastAPI Coffee Shop API

This is a simple FastAPI application that serves as an API for a coffee shop. It allows clients to view the menu, place orders, and retrieve the list of orders.

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Overview

The code consists of a FastAPI application with three main functionalities:

1. **View Menu (`/menu`):** Retrieve the list of available items on the coffee shop menu.

2. **View Orders (`/order`):** Retrieve the list of placed orders.

3. **Place Order (`/order`):** Submit a new order, specifying the item ID and quantity.

## Setup

1. Install the required dependencies:

    ```bash
    pip install fastapi uvicorn
    ```

2. Run the application:

    ```bash
    python main.py
    ```


## Usage

- Access the [Swagger Documentation](http://127.0.0.1:8000/docs) for detailed information about available endpoints and interact with the API.

- Use [ReDoc](http://127.0.0.1:8000/redoc) for an alternative documentation view.

## Endpoints

- **GET `/menu`:** Retrieve the coffee shop menu.
- **GET `/order`:** Retrieve the list of placed orders.
- **POST `/order`:** Place a new order by providing the item ID and quantity in the request body.

## Dependencies

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast web framework for building APIs with Python 3.7+.
- [uvicorn](https://www.uvicorn.org/): ASGI server for running FastAPI applications.

## Contributing

Feel free to contribute by submitting issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

---


