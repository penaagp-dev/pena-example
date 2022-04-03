from yoyo import step

__depends__ = {}

steps = [
    step("CREATE TABLE users (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(20), PRIMARY KEY (id))",
         "DROP TABLE users"),
]