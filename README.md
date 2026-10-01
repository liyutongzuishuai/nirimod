<div align="center">
  <h1>NiriMod</h1>
  
  **GTK4/libadwaita configuration editor for the [niri](https://github.com/niri-wm/niri) Wayland compositor.**
  
  **面向 [niri](https://github.com/niri-wm/niri) Wayland 合成器的 GTK4/libadwaita 配置编辑器。**

  [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
  [![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white)](https://python.org)
  [![GTK4](https://img.shields.io/badge/GTK-4%20%2B%20libadwaita-4A90D9?logo=gnome&logoColor=white)](https://gtk.org)
  [![Wayland](https://img.shields.io/badge/Wayland-native-orange)](https://wayland.freedesktop.org)
</div>

<br>

![NiriMod Interface](media/1.png)

Niri uses KDL for configuration. Hand-editing works well for basic keys, but managing multi-monitor layouts, easing curves, and complex window rules directly in text is error-prone. NiriMod provides a native graphical interface for these subsystems while preserving existing comments, file structures, and manual edits.

Niri 使用 KDL 作为配置格式。手动编辑适用于基本键值，但直接在文本中管理多显示器布局、缓动曲线和复杂窗口规则容易出错。NiriMod 为这些子系统提供了原生图形界面，同时保留现有注释、文件结构和手动编辑。

## Features / 功能特性

- Drag-and-drop monitor layout arrangement, resolution, refresh rate, variable refresh rate (VRR), and fractional scaling.
- Interactive keyboard heat map and searchable shortcut table with duplicate conflict detection.
- Column widths, gaps, struts, and per-window matching criteria.
- Mouse, touchpad, and trackpoint settings (acceleration profiles, scroll methods, button bindings, left-handed mode).
- Cubic-bezier and spring curve editor with live previews across all compositor transitions.
- Built-in KDL editor with syntax validation and undo/redo history.

- 拖放式显示器布局排列，支持分辨率、刷新率、可变刷新率 (VRR) 和分数缩放设置。
- 交互式键盘热力图和可搜索的快捷键表，支持重复冲突检测。
- 列宽、间隙、边框和逐窗口匹配条件。
- 鼠标、触控板和小红点设置（加速曲线、滚动方式、按键绑定、左手模式）。
- 三次贝塞尔和弹簧曲线编辑器，支持所有合成器过渡的实时预览。
- 内置 KDL 编辑器，支持语法验证和撤销/重做历史。

![Keybinding Management](media/2.png)

## Configuration Safety / 配置安全

- Writes run through `niri validate` before committing to disk. Invalid configurations are blocked and surfaced with compiler diagnostics.
- Config updates are staged in temporary files before replacing targets, preventing half-written files.
- Custom comments, whitespace, and formatting are preserved across round-trips.
- Snapshot and restore alternate configurations on demand.

- 写入前通过 `niri validate` 验证。无效配置会被拦截并显示编译器诊断信息。
- 配置更新先写入临时文件再替换目标，防止半写入文件。
- 自定义注释、空白和格式在往返操作中保持不变。
- 随时快照和恢复备选配置。

### Multi-File and Desktop Shell Setups / 多文件与桌面 Shell 设置

![Multi-File Configurations](media/multiple_configs.png)

Niri configurations frequently use `include` directives to separate concerns across files (such as inputs, outputs, or third-party shells like Dank Material Shell and Noctalia).

NiriMod resolves `include` paths recursively up to five levels deep. When modifying a setting from the interface, NiriMod maps the node back to its originating file and writes only to that file. Unrecognized directives and custom shell blocks remain untouched.

Niri 配置常使用 `include` 指令将关注点分离到不同文件（如输入、输出，或 Dank Material Shell、Noctalia 等第三方 Shell）。

NiriMod 递归解析 `include` 路径，深度达五层。通过界面修改设置时，NiriMod 将节点映射回其源文件，仅写入该文件。未识别的指令和自定义 Shell 块保持不变。

## NixOS and Home Manager / NixOS 与 Home Manager

When managing Niri via Home Manager, point NiriMod directly to your source files by using out-of-store symlinks:

当通过 Home Manager 管理 Niri 时，使用 out-of-store 符号链接将 NiriMod 直接指向您的源文件：

```nix
xdg.configFile."niri/config.kdl".source = config.lib.file.mkOutOfStoreSymlink "${config.home.homeDirectory}/path/to/your/dotfiles/niri/config.kdl";
```

NiriMod resolves symlinks to their underlying target before writing, allowing GUI adjustments to commit directly into your dotfiles repository.

NiriMod 在写入前解析符号链接到其底层目标，使 GUI 调整能直接提交到您的 dotfiles 仓库。

## Installation / 安装

### Arch Linux (AUR)

```bash
yay -S nirimod-git
```

### Installation Script / 安装脚本

```bash
curl -sSL https://raw.githubusercontent.com/srinivasr/nirimod/main/install.sh | bash
```
中文版:
```bash
REPO_URL="https://github.com/liyutongzuishuai/nirimod" bash install.sh --install
```

Use `--install` for non-interactive installs, `--uninstall` to remove, or `--skip-deps` to bypass package manager checks.

使用 `--install` 进行非交互式安装，`--uninstall` 卸载，或 `--skip-deps` 跳过包管理器检查。

## Dependencies / 依赖

- Python 3.12+ and `uv`
- GTK4, libadwaita, PyGObject, and Pycairo
- `niri` compositor binary

**Gentoo** (with [GURU overlay](https://wiki.gentoo.org/wiki/Project:GURU)):

```bash
emerge dev-vcs/git net-misc/curl dev-lang/python gui-libs/gtk gui-libs/libadwaita dev-python/pygobject dev-python/pycairo x11-libs/libxkbcommon x11-misc/xkeyboard-config
curl -sSL https://raw.githubusercontent.com/srinivasr/nirimod/main/install.sh | bash -s -- --install --skip-deps
```

## Contributing / 贡献

Review [CONTRIBUTING.md](CONTRIBUTING.md) for local development setup and style expectations.

请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解本地开发设置和风格规范。

<a href="https://www.star-history.com/?repos=srinivasr%2Fnirimod&type=date&legend=top-left">
 <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=srinivasr/nirimod&type=date&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=srinivasr/nirimod&type=date&legend=top-left" />
    <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=srinivasr/nirimod&type=date&legend=top-left" />
  </picture>
</a>

*NiriMod is an independent project and is not affiliated with the official niri team.*

*NiriMod 是一个独立项目，与官方 niri 团队无关联。*
