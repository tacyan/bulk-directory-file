# bulk-directory-file
一括でフォルダとファイル名を作成してくれるスクリプトです。

## 使い方

1. project_structure.txtを作成します。

下記のようなフォーマットで作成します。
AIが作成したフォルダ構造をベースにしています。

project_structure.txt
```
developer-flet/
├─ app.py
├─ config/
│  ├─ firebase.py
├─ domain/
│  ├─ test/
│  │  ├─ test_canva_template.py
│  │  ├─ test_insight.py
│  ├─ instagram_trend_post.py
│  ├─ performance.py
│  ├─ prompt.py
│  ├─ user.py
│  ├─ user_index.py
├─ infrastructure/
│  ├─ canva_template_repository.py
│  ├─ insight_repository.py
│  ├─ instagram_trend_post_repository.py
│  ├─ performance_repository.py
│  ├─ prompt_repository.py
│  ├─ user_index_repository.py
│  ├─ user_repository.py
├─ utils/
│  ├─ example_prompt.py
│  ├─ firebase_auth.py
│  ├─ scraping_helper.py
├─ type/
│  ├─ custom_types.py
├─ pages/
│  ├─ tools_usage.py
│  ├─ canva_design.py
│  ├─ insight_analysis.py
├─ requirements.txt
├─ README.md
```

2. 下記のコマンドを実行します。

実行したディレクトリにフォルダ構造が作成されます。

```
python create_project_structure.py project_structure.txt
```