from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()


class User(Base):
	__tablename__ = "users"
	id = Column(
		SQLAlchemyUUID(as_uuid=True), primary_key=True, default=uuid.uuid4
	)
	name = Column(String, nullable=False)
	# email = Column(String, nullable=False, unique=True)
	# password = Column(String, nullable=False)
