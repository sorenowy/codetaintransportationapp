import logging
from fastapi import APIRouter
from app.database.config.connection import prisma_connection


event_handler = APIRouter()

@event_handler.on_event("startup")
async def application_started():
    logging.info("App started.")
    await prisma_connection.connect()


@event_handler.on_event("shutdown")
async def application_exit():
    logging.info("App shutdown.")