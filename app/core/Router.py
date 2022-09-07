# -*-coding:UTF-8 -*-
"""
@Create_Time: 2022/9/1 18:18
@Author:zhao
@desc:fastapi
"""
from app.api import base_router
from fastapi import APIRouter


router = APIRouter()

@router.get('/')
async def msg():
    return {"欢迎来到fastapi子路由"}

