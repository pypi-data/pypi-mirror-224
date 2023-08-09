# 安装rust
curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh

# 安装rye
cargo install --git https://github.com/mitsuhiko/rye rye
# 升级rye
rye self update

# 安装python环境
rye pin 3.11
rye run python

# 安装pyhton包
rye add requests
rye add --dev ruff black isort
rye sync

# 快速安装依赖，不写入lock文件
rye sync --no-lock

# 格式化代码
rye run lint

# 运行
rye run serve

# 运行cli
rye shell
cli

# 打包
rye build
# 发布
rye publish



