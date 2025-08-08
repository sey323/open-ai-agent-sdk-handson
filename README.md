# Open AI Agent Sample

Open AI Agent のサンプル実装です

## インストール

本プロジェクトは uv で管理されています。以下のコマンドで依存関係をインストールしてください。

```bash
uv sync
```

## 実行方法

### Quick Start

Quick Start エージェントを起動します。

```bash
uv run -m open_ai_agent_sample.agents.quick_start.main
```

### Tool Agents

Web 検索をするエージェントを起動します。

```bash
uv run -m open_ai_agent_sample.agents.tools.main
```
