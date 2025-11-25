# 访客管理系统

## 项目简介

访客管理系统旨在简化学校外访客的登记、预约和审批流程。该系统为访客提供便捷的预约渠道，同时为大学工作人员提供管理和监控来访者的有效工具。系统确保记录准确、减少人工工作量，并提升校园安全与运营效率。

## 系统架构

### 整体架构
```
Client（客户端） → 通过网络 → Server（服务端） → 数据库（SQLite）

┌──────────────────────────┐
│  Client (Web前端)        │
│  - 用户界面交互           │
│  - 发送 HTTP 请求         │
│  - 展示结果               │
└───────────────▲──────────┘
                │HTTP JSON
            网络通信
                │
┌───────────────▼──────────┐
│   Server (Flask API)      │
│   - 业务逻辑处理          │
│   - 预约审批管理          │
│   - 数据库操作            │
└───────────────▲──────────┘
                │SQL
                │
┌───────────────▼──────────┐
│     SQLite Database      │
│  - Users                 │
│  - Visitor_Info          │
│  - Reservations          │
│  - Admins                │
│  - Admin_Info            │
└──────────────────────────┘
```

## 数据库设计

### 表结构说明

#### 1. Users（用户表）
| 字段名 | 类型 | 说明 |
|--------|------|------|
| user_id | INTEGER | 主键，自增长 |
| username | TEXT | 唯一用户名，非空 |
| password_hash | TEXT | 密码哈希值，非空 |
| created_at | DATETIME | 创建时间，默认当前时间 |

#### 2. Visitor_Info（访客信息表）
| 字段名 | 类型 | 说明 |
|--------|------|------|
| visitor_id | INTEGER | 主键，自增长 |
| user_id | INTEGER | 外键，关联Users表 |
| name | TEXT | 姓名，非空 |
| phone | TEXT | 电话，非空 |
| affiliation | TEXT | 所属单位/机构 |
| updated_at | DATETIME | 更新时间，默认当前时间 |

#### 3. Reservations（预约表）
| 字段名 | 类型 | 说明 |
|--------|------|------|
| reservation_id | INTEGER | 主键，自增长 |
| user_id | INTEGER | 外键，关联Users表 |
| visit_date | DATE | 访问日期，非空 |
| visit_time | TIME | 访问时间，非空 |
| location | TEXT | 访问地点，非空 |
| purpose | TEXT | 访问事由，非空 |
| status | TEXT | 状态：pending/approved/denied |
| admin_id | INTEGER | 审核管理员ID，外键 |
| review_comment | TEXT | 审核评论 |
| created_at | DATETIME | 创建时间 |
| updated_at | DATETIME | 更新时间 |

#### 4. Admins（管理员表）
| 字段名 | 类型 | 说明 |
|--------|------|------|
| admin_id | INTEGER | 主键，自增长 |
| username | TEXT | 唯一用户名，非空 |
| password_hash | TEXT | 密码哈希值，非空 |
| phone | TEXT | 联系电话 |
| created_at | DATETIME | 创建时间 |

#### 5. Admin_Info（管理员信息表）
| 字段名 | 类型 | 说明 |
|--------|------|------|
| admin_id | INTEGER | 主键，自增长 |
| username | TEXT | 唯一用户名，非空 |
| email | TEXT | 邮箱，非空且唯一 |
| phone | TEXT | 电话，非空且唯一 |

## 功能需求

### 访客功能
1. **账户管理**
   - 用户注册（用户名和密码）
   - 账户登录认证
   - 个人信息管理（姓名、电话、所属单位）

2. **预约管理**
   - 创建访问预约（日期、时间、地点、事由）
   - 查看预约状态（待审核、已批准、已拒绝）
   - 修改预约详情（修改后需重新审批）
   - 删除或取消预约
   - 查看预约历史记录

### 管理员功能
1. **账户管理**
   - 管理员登录
   - 修改个人账户信息（邮箱、电话）

2. **预约管理**
   - 查看所有预约记录
   - 按日期、地点或状态筛选预约
   - 实时批准或拒绝访客预约
   - 查看当日已批准访客

3. **数据报表**
   - 显示每日访客数据统计
   - 访客数量分析
   - 热门访问地点统计

## 项目结构

### 后端结构 (/backend)
```
project/
├── admin_routes.py        # 管理员操作路由
├── auth_routes.py         # 认证路由（注册、登录）
├── visitor_routes.py      # 访客操作路由
├── app.py                 # Flask应用主程序
├── db.py                  # 数据库连接
├── model.py               # 数据模型和数据库操作
└── utils.py               # 工具函数（密码验证等）
```

### 前端结构 (/frontend)
```
project/
├── login.html                # 登录页面
├── visitor_home.html         # 访客首页
├── visitor_profile.html      # 访客资料页面
├── reservation_create.html   # 创建预约页面
├── reservation_list.html     # 预约列表页面
└── admin_dashboard.html      # 管理员控制台
```

## 技术栈

### 后端技术
- **框架**: Python + Flask
- **数据库**: SQLite
- **认证**: 密码哈希加密

### 前端技术
- **语言**: HTML, CSS, JavaScript
- **样式**: Tailwind CSS
- **交互**: 原生JavaScript + Fetch API

## 安装和运行

### 环境要求
- Python 3.7+
- 现代浏览器

### 运行步骤

1. **设置虚拟环境**
   ```bash
   python -m venv venv
   
   # Linux/Mac
   source venv/bin/activate
   
   # Windows
   venv\Scripts\activate
   ```

2. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **启动后端服务**
   ```bash
   cd backend
   python app.py
   ```

4. **访问前端页面**
   - 打开浏览器访问 `http://localhost:5000`
   - 或直接打开 frontend 目录中的 HTML 文件

## 系统特性

- **安全性**: 密码哈希存储，权限控制
- **易用性**: 直观的用户界面，简化操作流程
- **实时性**: 即时状态更新和通知
- **可扩展**: 模块化设计，便于功能扩展
- **数据完整性**: 完整的数据验证和约束

## 注意事项

- 修改预约后状态将重置为待审核
- 已批准的预约取消需要重新审核
- 管理员操作有完整的日志记录
- 系统支持并发访问和数据一致性保证转为英文