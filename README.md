## 白書ダッシュボード

#### アプリケーションの概要
- Streamlitを用い、総務省の情報通信白書等をビジュアライズするためダッシュボード化

#### 使用技術等
- Python
- Streamlit
- Docker
- Git
- GitHub Actions
- Heroku

#### 作成にあたっての概要
- Streamlitで作成したダッシュボードをDockerでコンテナ化し、Herokuにデプロイ。
- Github Actionsを導入し、更新を行った際、GitにPushすると同時に自動でHerokuにデプロイが行われるよう連携。
