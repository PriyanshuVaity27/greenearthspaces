# app/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("+psypostgresqlcopg2://postgres:greenearthspaces27@db.apbkobhfnmcqqzqeeqss.supabase.co:5432/postgres")
engine = create_engine(+psypostgresqlcopg2://postgres:greenearthspaces27@db.apbkobhfnmcqqzqeeqss.supabase.co:5432/postgres)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

