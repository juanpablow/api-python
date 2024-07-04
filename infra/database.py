import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine, text


logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)


def get_db_engine():
	load_dotenv(dotenv_path=".env.development")

	host = os.getenv("POSTGRES_HOST")
	user = os.getenv("POSTGRES_USER")
	db_name = os.getenv("POSTGRES_DB")
	passwd = os.getenv("POSTGRES_PASSWORD")
	port = os.getenv("POSTGRES_PORT")

	db_url = f"postgresql://{user}:{passwd}@{host}:{port}/{db_name}"

	engine = create_engine(
		db_url, echo=True
	)  # echo=True para ver as queries SQL geradas

	return engine


def execute_query(query):
	engine = get_db_engine()
	try:
		with engine.connect() as connection:
			result = connection.execute(text(query))
			return result.fetchone()[0]

	except Exception as e:
		print(f"Erro ao executar a consulta SQL: {e}")
		return None


if __name__ == "__main__":
	query = "SELECT 1 + 1;"
	print(execute_query(query))
