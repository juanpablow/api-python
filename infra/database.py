import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine, text


logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)


def get_url_database() -> str:
	load_dotenv(dotenv_path="../.env.development")

	host = os.getenv("POSTGRES_HOST")
	user = os.getenv("POSTGRES_USER")
	db_name = os.getenv("POSTGRES_DB")
	passwd = os.getenv("POSTGRES_PASSWORD")
	port = os.getenv("POSTGRES_PORT")

	return f"postgresql://{user}:{passwd}@{host}:{port}/{db_name}"


def execute_query(query):
	engine = create_engine(get_url_database(), echo=True)
	try:
		with engine.connect() as connection:
			result = connection.execute(text(query))
			return result.fetchone()[0]

	except Exception as e:
		print(f"Error executing SQL query: {e}")
		return None


if __name__ == "__main__":
	query = "SELECT 1 + 1;"
	print(execute_query(query))
