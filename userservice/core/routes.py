from fastapi import APIRouter, Depends

from core.db import get_user_info, get_files, get_files_count, get_files_size
from core.schemes import User

router = APIRouter()


async def decode_token():
    pass


@router.get("/user_info")
async def user_info(user: User = Depends(decode_token)):
    db_user = await get_user_info(user.login)

    # TODO: а зачем нам етот метод
    pass


@router.get("/user_files")
async def user_files(user: User = Depends(decode_token)):
    db_user = await get_user_info(user.login)
    files = await get_files(db_user.id)

    return [
        dict(
            name=file.get("name"),
            size=file.get("size"),
            status=file.get("status")
        ) for file in files
    ]


@router.get("/user_files/count")
async def user_files_count(user: User = Depends(decode_token)):
    db_user = await get_user_info(user.login)
    count = await get_files_count(db_user.id)

    return {"files_count": count}


@router.get("/user_files_size")
async def user_files_size(user: User = Depends(decode_token)):
    db_user = await get_user_info(user.login)
    size = await get_files_size(db_user.id)

    return {"files_size": size}


@router.post("/user", status_code=201)
async def create_user(user: User):
    pass


@router.put("/user")
async def update_user(user: User):
    pass
