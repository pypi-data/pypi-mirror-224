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

# 运行
rye run serve

# 打包
rye build
# 发布
rye publish



