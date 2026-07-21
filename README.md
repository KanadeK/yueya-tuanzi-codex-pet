# 妙脆角小猫 Codex Pet

<p align="center">
  <img src="media/showcase.gif" alt="妙脆角小猫九种 Codex 状态动画" width="240">
</p>

<p align="center">以用户确认的原图做透明抠图和确定性动画的 Codex Desktop 宠物。</p>

<p align="center">
  <a href="https://kanadek.github.io/miaocui-jiao-cat-codex-pet/">动画预览</a> |
  <a href="https://learn.chatgpt.com/docs/pets">Codex Pets 官方说明</a> |
  <a href="NOTICE.md">版权与来源说明</a>
</p>

## 安装

[在 Codex 中安装妙脆角小猫](codex://pets/install?name=%E5%A6%99%E8%84%86%E8%A7%92%E5%B0%8F%E7%8C%AB&imageUrl=https%3A%2F%2Fraw.githubusercontent.com%2FKanadeK%2Fmiaocui-jiao-cat-codex-pet%2Fmain%2Fpet%2Fspritesheet.webp&spriteVersionNumber=2)

如果浏览器不允许打开 `codex://` 链接，可使用下列脚本或手动安装。

### Windows PowerShell

```powershell
irm https://raw.githubusercontent.com/KanadeK/miaocui-jiao-cat-codex-pet/main/scripts/install.ps1 | iex
```

### macOS / Linux

```bash
curl -fsSL https://raw.githubusercontent.com/KanadeK/miaocui-jiao-cat-codex-pet/main/scripts/install.sh | sh
```

安装器会校验 SHA-256。已有同 ID 宠物会先备份到 `~/.codex/pet-backups/`，不会直接删除。

### 手动安装

把 `pet/pet.json` 与 `pet/spritesheet.webp` 放入 `~/.codex/pets/miaocui-jiao-cat/`，然后在 **Settings > Pets** 中刷新并选择 **妙脆角小猫**。

## 九种状态

| Codex 状态 | 动画处理 |
| --- | --- |
| 空闲陪伴 | 原图轻微呼吸 |
| 向右/左移动 | 原图平移与镜像 |
| 唤醒 | 原图轻摆 |
| 任务完成 | 原图小跳 |
| 任务受阻 | 原图摇晃 |
| 等待 | 原图轻摆 |
| 工作中 | 原图节奏位移 |
| 等待验收 | 原图上移回应 |

所有帧都只来自同一张透明原图抠图；不含另一只猫、AI 重绘或外部参考图片。

## 官方格式与验证

- 图集：`1536 × 1872` lossless WebP
- 网格：`8 × 9`，单格：`192 × 208`
- 背景：透明 RGBA；Sprite 版本：`2`
- 文件大小：小于官方 20 MiB 上传限制

```powershell
uv venv .venv
uv pip install --python .venv\Scripts\python.exe -r requirements-dev.txt
.venv\Scripts\python.exe scripts\build_assets.py
.venv\Scripts\python.exe scripts\validate_pet.py
.venv\Scripts\python.exe -m pytest -q
```

## 素材来源与版权

- 仓库所有者确认可为本项目使用其提供的妙脆角小猫参考图。
- 原图不会上传或重新分发；仓库只保存透明处理后的 pet 素材与由其生成的图集。
- 公开搜索仅用于确认梗名和视觉特征，未下载、复制或包含任何外部图片。
- 完整边界见 [NOTICE.md](NOTICE.md)，处理方式见 [artwork/PROMPT.md](artwork/PROMPT.md)。

## 贡献者

本项目由 [KanadeK](https://github.com/KanadeK) 维护；发布前会核查 Git 作者、提交者、短日志、GitHub contributors 和 `Co-authored-by`。

## License

MIT；适用范围见 [NOTICE.md](NOTICE.md)。
