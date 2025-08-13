#!/bin/bash
# sync_submodules.sh
# 自动同步主仓库和子模块到远程最新版本

# 配置：子模块路径和分支
SUBMODULE_PATH="src/MDP_Planner"
BRANCH="master"

echo "=== 更新子模块 $SUBMODULE_PATH ==="
cd "$SUBMODULE_PATH" || { echo "子模块路径不存在"; exit 1; }

# 拉取远程最新分支
git fetch origin "$BRANCH"
git checkout "$BRANCH"
git pull origin "$BRANCH"

# 检查是否有改动（包括 untracked）
if [[ -n $(git status --porcelain) ]]; then
    echo "子模块有改动，提交并推送"
    git add .
    git commit -m "Update submodule to latest $BRANCH"
    git push origin "$BRANCH"
else
    echo "子模块已经是最新"
fi

cd - || exit 1

# 回到主仓库
echo "=== 提交主仓库更新的子模块指针 ==="
git add "$SUBMODULE_PATH"
if [[ -n $(git status --porcelain) ]]; then
    git commit -m "Update submodule $SUBMODULE_PATH to latest $BRANCH"
    git push
else
    echo "主仓库子模块指针已经是最新"
fi

echo "=== 同步完成 ==="

