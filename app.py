import os
from flask import Flask, render_template

# テンプレートと静的ファイルのパスを明示的に指定
app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    """
    トップページを表示。templates/index.htmlをレンダリングします。
    """
    context = {
        "title": "Flask Studio Pro",
        "message": "ノーコードからデプロイまで、すべて準備完了です！",
        "features": ["マルチファイル対応", "Renderデプロイ最適化", "Jinja2テンプレート"]
    }
    return render_template("index.html", **context)

@app.route("/api/status")
def status():
    """
    動作確認用のAPIエンドポイント
    """
    return {"status": "healthy", "server": "Flask"}

if __name__ == "__main__":
    # Renderのポート番号指定に対応、ローカルでは5000番で起動
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
