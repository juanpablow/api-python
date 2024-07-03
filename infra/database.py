import os
from dotenv import load_dotenv
import psycopg2


def query(queryObj):
	load_dotenv(dotenv_path=".env.development")

	host = os.getenv("POSTGRES_HOST")
	user = os.getenv("POSTGRES_USER")
	db_name = os.getenv("POSTGRES_DB")
	passwd = os.getenv("POSTGRES_PASSWORD")
	port = os.getenv("POSTGRES_PORT")

	try:
		client = psycopg2.connect(
			dbname=db_name, user=user, host=host, password=passwd, port=port
		)

		cursor = client.cursor()
		cursor.execute(queryObj)

		query = cursor.fetchone()[0]

		return query

	except (Exception, psycopg2.Error) as error:
		print(f"Error while connecting to PostgreSQL: {error}")
	finally:
		client.close()
