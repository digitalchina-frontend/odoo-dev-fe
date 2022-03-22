# 开发环境搭建

## 参考文档

- [官方](https://www.odoo.com/documentation/14.0/developer/howtos/rdtraining/02_setup.html#python)
- [Odoo 14 Cookbook 中文版本](https://github.com/iTranslateX/odoo-cookbook/blob/main/1.md)

## 步骤

> 暂时不区分 操作系统版本 （mac 与 windows 通用）

- Python3 安装

- 数据库

  > 基于 docker

  - 执行 `npm run start:db`

- clone 本工程

  - `git clone https://github.com/digitalchina-frontend/odoo-dev-fe.git`

  - `git submodule init`

- 创建 Odoo 虚拟环境

  - `python3 -m venv ~/venv/[你自己指定的名字]`
  - `source ~/[你自己指定的名字]/bin/activate`

- 启动
  - `npm run start`
