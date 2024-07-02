from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()


@app.get("/")
async def read_main():
	return {"msg": "Hello World"}


def custom_openapi():
	if app.openapi_schema:
		return app.openapi_schema
	openapi_schema = get_openapi(
		title="TaskAPI",
		version="1.0.0",
		description="Project to add tasks",
		routes=app.routes,
	)
	app.openapi_schema = openapi_schema
	return app.openapi_schema


app.openapi = custom_openapi
