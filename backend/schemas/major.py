#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:00
# @Author : 小四先生
# @desc : 专业表模型的数据验证
# 共享属性
from typing import Optional

from pydantic import BaseModel


# 共享属性
class MajorBase(BaseModel):
    # id: Optional[str] = None
    name: Optional[str] = None
    assistant: Optional[str] = None
    phone: Optional[str] = None


# 属性在创建时通过API接收
class MajorCreate(MajorBase):
    pass


# 属性通过API接收更新
class MajorUpdate(MajorBase):
    pass


# 创建数据库
class MajorInDBBase(MajorBase):
    id: str
    department_id: str

    class Config:
        orm_mode = True  # 是否为orm模型


# 通过API返回的附加属性
class Major(MajorInDBBase):
    pass


# 存储在DB中的附加属性
class MajorInDB(MajorInDBBase):
    pass
