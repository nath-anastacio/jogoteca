
SECRET_KEY = 'Alura'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'Nath20022512.',
        servidor = 'localhost',
        database = 'jogoteca'
    )