# pre-commit配置
# 在根目录执行如下命令，生成一个默认的配置，python版本
pre-commit sample-config > .pre-commit-config.yaml
# 直接执行此命令，设置git hooks钩子脚本
pre-commit install
# 手动对所有的文件执行hooks，新增hook的时候可以执行，使得代码均符合规范。直接执行该指令则无需等到pre-commit阶段再触发hooks
pre-commit run --all-files
# 执行特定hooks
pre-commit run <hook_id>
# 将所有的hook更新到最新的版本/tag
pre-commit autoupdate
# 指定更新repo
pre-commit autoupdate --repo https://github.com/DoneSpeak/gromithooks
# 卸载
pre-commit uninstall