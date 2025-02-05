#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/14 17:00
# @Author : zxiaosi
# @desc : 封装数据库增删改查方法
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import func, distinct
from sqlalchemy.orm import Session

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD对象的默认方法去 增 查 改 删 (CRUD).

        参数 :

        * `model`: ORM模型类
        * `schema`: 数据验证模型类
        """
        self.model = model

    def get(self, db: Session, *, id: Any) -> Optional[ModelType]:
        """
        通过 ID 获取对象

        :param db: Session
        :param id: ID
        :return: 查询到的orm模型对象
        """
        # table_name = self.model.__tablename__
        # table_id = table_name + '_id'
        # print(table_id) # 表名_字段名
        # return db.execute(f'select * from {table_name} where {table_id} = {id}').first()

        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session, *, pageIndex: int = 1, pageSize: int = 10) -> dict[str, List[ModelType]]:
        """
        获取 skip-limit 的对象集

        :param db: Session
        :param pageIndex: 页码 (默认值1)
        :param pageSize: 页码 (默认10)
        :return: 查询到的orm模型对象集
        """
        data = db.query(self.model).offset((pageIndex - 1) * pageSize).limit(pageSize).all()
        count: int = db.query(func.count(distinct(self.model.id))).scalar()
        return {'count': count, 'dataList': data}

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        """
        添加对象

        :param db: Session
        :param obj_in: 创建模型
        :return: orm模型对象
        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, *, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        """
        更新对象

        :param db: Session
        :param db_obj: orm模型对象
        :param obj_in: 更新模型 或者 字典数据
        :return: orm模型对象
        """
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int) -> ModelType:
        """
        通过 ID 删除对象

        :param db: Session
        :param id: ID
        :return: orm模型对象
        """
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
