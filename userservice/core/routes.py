from fastapi import APIRouter, Depends

from core.db import get_user_info, get_files, get_files_count, get_files_size, get_file_status
from core.schemes import User

router = APIRouter()


async def decode_token():
    pass


@router.get("/user-info")
async def user_info(user: User = Depends(decode_token)):
    db_user = await get_user_info(user.login)

    return {"login": db_user.get("login"),
            "telegram": db_user.get("telegram")}


@router.get("/user-files")
async def user_files(user: User = Depends(decode_token)):
    db_user = await get_user_info(user.login)
    files = await get_files(db_user.id)

    return [
        dict(
            id=file.get("id"),
            name=file.get("name"),
            size=file.get("size"),
            status=file.get("status")
        ) for file in files
    ]


@router.get("/file-status/{file_id}")
async def file_status(file_id: int, user: User = Depends(decode_token)):
    status = await get_file_status(file_id)

    return {"status": status}


@router.get("/user-files/count")
async def user_files_count(user: User = Depends(decode_token)):
    db_user = await get_user_info(user.login)
    count = await get_files_count(db_user.id)

    return {"files_count": count}


@router.get("/user-files/size")
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
