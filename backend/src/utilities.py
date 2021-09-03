def get_db_string_connection() -> str:
    return "sqlite://database.db"


def get_models_list() -> list:
    with open('models.list', 'r') as f:
        return list(map(lambda x: x.rstrip(), f.readlines()))
