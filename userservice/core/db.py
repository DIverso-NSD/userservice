from contextlib import asynccontextmanager

import asyncpg

from core.settings import settings


@asynccontextmanager
async def db_connect():
    conn = await asyncpg.connect(settings.psql_url)
    try:
        yield conn
    finally:
        await conn.close()


async def get_user_info(login: str):
    async with db_connect() as conn:
        return await conn.fetch(f"select * from users where login={login}")


async def get_files_count(user_id: int):
    async with db_connect() as conn:
        return await conn.fetch(f"select count(*) from files where user_id={user_id}")


async def get_files_size(user_id: int):
    async with db_connect() as conn:
        return await conn.fetch(f"select sum(size) from files where user_id={user_id}")


async def get_files(user_id: int):
    async with db_connect() as conn:
        return await conn.fetch(f"select * from files where user_id={user_id}")
