# Web3 Product Manager Skills（中文说明）

Agent Skills 套件，用于 Web3 产品：**策略决策 → 确认 memo → PRD 规格**。

- 英文技能正文：`skills/*/SKILL.md`
- 仓库：https://github.com/kimogrant/web3-product-manager-skill
- 版本：见 [VERSION](VERSION)

## 包含三个 Skill

| 命令 | 作用 |
|------|------|
| `/web3-product-manager` | 编排：强制先策略后规格 |
| `/web3-product-strategy` | Go/no-go、调研、策略 memo |
| `/web3-product-specification` | PRD、Gate、代币经济/合规/原型门 |

## 安装

**Windows：**

```powershell
git clone https://github.com/kimogrant/web3-product-manager-skill.git
cd web3-product-manager-skill
.\install.ps1 -Target D:\你的项目路径
```

**Git Bash / macOS / Linux：**

```bash
./skill.sh install /path/to/your/project
```

安装到：`你的项目/.cursor/skills/`（含 `references/` 与 `examples/`）。

重载 Cursor 后使用斜杠命令。

## 全链路用法

Cursor **不会自动串联**子 skill。建议：

1. 安装上述三个 skill；
2. 使用 `/web3-product-manager`；
3. 确认 Agent **读取** `pipeline-summary.md` 与子目录中的 `SKILL.md`。

策略 memo 经你确认后，再进入规格（或在确认后单独 `/web3-product-specification`）。

## 示例

| 文件 | 内容 |
|------|------|
| `examples/strategy-memo-sample.md` | 策略 memo + Source index |
| `examples/prd-story-sample.md` | 带 SRC 的用户故事 |
| `examples/full-prd-outline-sample.md` | 完整 PRD 目录示例（含 Gate 3.5） |

## 测试

```bash
python -m unittest discover -s tests -v
```

## 许可

MIT — [LICENSE](LICENSE)
