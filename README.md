# 课程管理系统
## 部署
用vercel可以直接部署
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/JerryLiu369/course-management)

或者拉取到服务器上，安装requirements.txt后进行部署

## 部署设置
### vercel
在vercel部署时需要配置环境变量：

`SQLALCHEMY_DATABASE_URI`：sqlalchemy的所需配置，填入数据库信息

`HOST`：数据库地址

`USER`：数据库用户名

`PASSWORD`： 数据库密码

`DB`：所用数据库名称

### 服务器
在服务器配置时也可设置以上环境变量，或在`api/`中放置一个文件名为`.env`的文件，内容如下，将环境变量填入对应位置即可：

```
SQLALCHEMY_DATABASE_URI

HOST

USER

PASSWORD

DB
```


