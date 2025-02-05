# FastAPI

## 版本

+ `V1.0` FastAPI学习
+ `V2.0` 搭建FastAPI脚手架
+ `V2.1` 创建所需的表
+ `V2.2` 已成功调试Mysql、Sqlite, 未调试Postgresql
+ `V2.3` 初始化表数据(调试)
+ `V2.4` 优化创建表问题
+ `V2.5` 初始化所有表数据
+ `V2.6` 封装日志模块
+ `V2.7` 封装多进程日志模块(线程锁)
+ `V2.8` 优化了目录结构
+ `V2.9` 优化代码&&调试了user表的增删查接口
+ `V3.0` 添加了防止跨域请求代码&&调试了接口
+ `V3.1` 去除了测试表的自增
+ `V3.2` 添加了department表的接口
+ `V3.3` 添加了major表的接口
+ `V3.4` 更新了major表接口的部分代码
+ `V3.5` 更换了日志模块(loguru)&&添加了后端数据验证
+ `V3.5` 添加了teacher表的接口
+ `V3.6` 添加了student表的接口
+ `V3.7` 添加了course表和selectCourse表的接口
+ `V3.8` 更新了所需的包
+ `V3.9` 修改了查询单个信息的数据
+ `V4.0` 删除了获取所有数据以及获取单个数据的方法
+ `V4.1` 修改了校验规则
+ `V4.1.1` 删除了整型和浮点型的正则校验规则
+ `v4.2` 尝试部署中。。。
+ `v4.3` 部署成功,修复了部分bug
+ `v4.4` 测试token
+ `v4.5` 调试token成功(admin, 123)
+ `v4.6` 重构FastAPI

## 安装

1. 配置Python3.9(及以上)的虚拟环境

2. 安装运行所需的包

   ```python
   pip install requirements.txt
   
   # 或者
   pip install fastapi
   pip install uvicorn
   pip install loguru
   pip install SQLAlchemy
   pip install python-jose
   pip install passlib
   pip install bcrypt
   pip install python-multipart
   pip install orjson
   pip install aioredis
   
   # 使用mysql, 请安装下面包
   pip install mysqlclient
   ```


3. 启动服务

    + 进入到 `backend` 项目下
    + 找到 `main.py` 右键运行
    + `core/config` 配置文件(默认使用了SQLite,可以配置MySQL)

   > 接口文档：http://127.0.0.1:8000/docs

## 项目截图

+ 成功运行的图片

  ![](https://gitee.com/zxiaosi/image/raw/master/Project/Vue+FastAPI/image-20211021164103094.png)

+ 接口图

  ![](https://gitee.com/zxiaosi/image/raw/master/Project/Vue+FastAPI/backend-%E6%8E%A5%E5%8F%A3.png)

## 项目目录

```sh
|-- backend
    |-- api					            # 接口文档
        |-- __init__.py	        
        |-- apis                        # api版本1
            |-- __init__.py	       	        
            |-- admin
                |-- __init__.py       	       	        
                |-- admin_api.py        # 管理员api汇总	       	                  
                |-- course.py	        # 课程表接口
                |-- department.py	    # 院系表接口
                |-- major.py	        # 专业表接口
                |-- selectCourse.py	    # 选课表接口
                |-- student.py	        # 学生表接口
                |-- teacher.py	        # 教师表接口
                |-- users.py	        # 用户表接口
            |-- teacher
                |-- __init__.py       	       	        
                |-- teacher_api.py      # 教师api汇总	       	                  
            |-- student
                |-- __init__.py       	       	        
                |-- student_api.py      # 学生api汇总	       	                  
        |-- deps.py	                    # 获取数据库连接对象
        |-- api_router.py	       	    # 接口汇总    
                         
	|-- core					# 核心内容
		|-- __init__.py			    
		|-- config.py			# 配置文件
		|-- security.py		    # 安全配置
		
	|-- crud					# 数据库的增删改查操作
		|-- __init__.py			# 抛出操作表数据文件中的类
		|-- base.py     		# 封装数据库增删改查方法
		|-- crud_course.py	    # 课程表--增删改查方法
		|-- crud_department.py	# 院系表--增删改查方法
		|-- crud_major.py		# 专业表--增删改查方法
		|-- crud_selectCourse.py # 选课表--增删改查方法
		|-- crud_teacher.py		# 教师表--增删改查方法
		|-- crud_user.py		# 用户表--增删改查方法
		|-- crud_student.py		# 学生表--增删改查方法
		
 	|-- db						# 数据库相关
 		|-- __init__.py			# 抛出数据库生成、删除表的方法
		|-- base.py		        # 配置需要创建的表
		|-- base_class.py		# 自动生成 表名
		|-- init_db.py			# 创建和删除base中的表
		|-- session.py			# 创建数据库连接会话
		
	|-- initial_data            # 初始化表数据
    	|-- __init__.py			# 抛出初始化表数据的两种方法
    	|-- data.py		        # 所有数据
    	|-- init_data.py		# 两种初始化表数据的方式
    	
    |-- logs                    # 日志模块(自动生成)
        |-- 2021-10-06_23-46-45.log			    
        |-- 2021-10-06_23-46-47.log			    
        |-- 2021-10-06_23-46-49.log		
        	    
	|-- models                  # ORM模型映射
		|-- __init__.py			# 抛出ORM模型对象
		|-- admin.py			# 管理员表
		|-- course.py			# 课程表
		|-- department.py		# 院系表
		|-- major.py			# 专业表
		|-- selectCourse.py		# 选课表
		|-- student.py			# 学生表
		|-- teacher.py			# 教师表
		|-- user.py				# 调试表
		
	|-- register                # 加载注册中心
	    |-- __init__.py			# 抛出加载注册中心
	    |-- app.py			    # 挂载其他app
	    |-- cors.py			    # 注册跨域请求
	    |-- exception.py		# 注册全局异常
	    |-- middleware.py		# 注册请求响应拦截
	    |-- redis.py		    # 注册Redis
	    |-- router.py		    # 注册路由
	    
	|-- schemas                 # Pydantic数据验证
		|-- __init__.py			# 抛出Pydantic数据验证
		|-- admin.py			# 管理员表数据验证
		|-- course.py			# 课程表数据验证
		|-- department.py		# 院系表数据验证
		|-- major.py			# 专业表数据验证
		|-- selectCourse.py		# 选课表数据验证
		|-- student.py			# 学生表数据验证
		|-- teacher.py			# 教师表数据验证
		|-- user.py				# 调试表数据验证
		
	|-- utils                   # 工具
	    |-- __init__.py		    # 抛出工具类
	    |-- custon_exc.py		# 自定义异常
	    |-- logger.py		    # 日志模块
	    |-- response.py	        # 状态码
	
	|-- __init__.py
	|-- main.py					# 主程序
	|-- Dockerfile              # Dockerfile文件
	|-- README.md               # Readme文件
	|-- requirements.txt		# 所需的包
	|-- sql_app.db              # sqlite数据库
```

