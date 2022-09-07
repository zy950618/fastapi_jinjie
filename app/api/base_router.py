# -*-coding:UTF-8 -*-
"""
@Create_Time: 2022/9/1 18:07
@Author:zhao
@desc:基本子路由
"""

from fastapi import FastAPI, APIRouter

app_01 = APIRouter()


@app_01.get("/")
async def msg():
    return {"欢迎来到fastapi子路由"}
