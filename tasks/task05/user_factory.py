def create_user(name: str = "", surname: str = "", age: int = 42, **kwargs):
    extra = {}

    for key in kwargs:
        extra[key] = kwargs[key]

    return {
        "name": name,
        "surname": surname,
        "age": age,
        "extra": extra
    }


assert create_user("John", "Doe") == {
    "name": "John",
    "surname": "Doe",
    "age": 42,
    "extra": {}
}


assert create_user("Bill", "Gates", age=65) == {
    "name": "Bill",
    "surname": "Gates",
    "age": 65,
    "extra": {}
}


assert create_user("Marie", "Curie", age=66, occupation="physicist", won_nobel=True) == {
    "name": "Marie",
    "surname": "Curie",
    "age": 66,
    "extra": {
        "occupation": "physicist",
        "won_nobel": True
    }
}


print("Tests passed")
