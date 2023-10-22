from dotenv import dotenv_values

IS_DEV = False if dotenv_values(".env").get("IS_DEV") is None else True

PREPOPULATED_ITEMS = [
    {
        "name": "Coke Zero",
        "quantity": 100,
        "price": 1.80,
        "description": "A healthier alternative to regular coke",
    },
    {
        "name": "Coke Regular",
        "quantity": 20,
        "price": 1.60,
        "description": "An unhealthier alternative to coke zero",
    },
    {
        "name": "Twisties",
        "quantity": 38,
        "price": 1.00,
        "description": "A tasty corn-based snack!",
    },
    {
        "name": "Liquorice",
        "quantity": 22,
        "price": 1.20,
        "description": "Just why.....",
    },
    {
        "name": "Top 10",
        "quantity": 8,
        "price": 1.50,
        "description": "The poor man's Mangum ice cream. Tastes just as great!",
    },
]
