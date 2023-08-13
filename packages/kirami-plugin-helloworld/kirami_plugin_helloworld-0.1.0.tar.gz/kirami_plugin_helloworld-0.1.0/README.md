<div align="center">

# kirami-plugin-helloworld

_✨ Hello World! ✨_

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/A-kirami/kirami-plugin-helloworld.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/kirami-plugin-helloworld">
    <img src="https://img.shields.io/pypi/v/kirami-plugin-helloworld.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">

</div>

## 📖 介绍

你好，世界

## 💿 安装

<details>
<summary>使用包管理器安装</summary>
在 kiramibot 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install kirami-plugin-helloworld

</details>
<details>
<summary>pdm</summary>

    pdm add kirami-plugin-helloworld

</details>
<details>
<summary>poetry</summary>

    poetry add kirami-plugin-helloworld

</details>
<details>
<summary>conda</summary>

    conda install kirami-plugin-helloworld

</details>

打开 kiramibot 项目根目录下的 `kirami.config.toml` 文件, 在 `[plugin]` 部分追加写入

    plugins = ["kirami_plugin_helloworld"]

</details>

## 🎉 使用

### 指令表

| 指令  | 权限 | 需要@ |   范围    | 说明  |
| :---: | :--: | :---: | :-------: | :---: |
| hello |  无  |  否   | 私聊/群聊 | world |
