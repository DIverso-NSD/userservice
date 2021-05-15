from fastapi import APIRouter, Depends

from userservice.core.db import (
    get_user_info,
    get_files,
    get_files_count,
    get_files_size,
    get_file_status,
)
from userservice.core.schemas import User
from userservice.core.middleware import verify_token

router = APIRouter()


@router.get("/user")
async def get_user(user_id: int):
    db_user = await get_user_info(user_id)

    return {"login": db_user.get("login"), "telegram": db_user.get("telegram")}


@router.get("/user/files")
async def get_user_files(user: User = Depends(verify_token)):
    db_user = await get_user_info(user.id)
    files = await get_files(db_user.get("id"))

    return [
        dict(
            id=file.get("id"),
            name=file.get("name"),
            size=file.get("size"),
            status=file.get("status"),
        )
        for file in files
    ]


@router.get("/file/{file_id}/status")
async def file_status(file_id: str, user: User = Depends(verify_token)):
    status = await get_file_status(file_id)

    return status


@router.get("/user/files/count")
async def get_user_files_count(user: User = Depends(verify_token)):
    db_user = await get_user_info(user.id)
    count = await get_files_count(db_user.get("id"))

    return count


@router.get("/user/files/size")
async def get_user_files_size(user: User = Depends(verify_token)):
    db_user = await get_user_info(user.id)
    size = await get_files_size(db_user.get("id"))

    return size
