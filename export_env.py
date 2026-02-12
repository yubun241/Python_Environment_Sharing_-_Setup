import sys
import subprocess
import platform
from datetime import datetime

def export_environment():
    # 出力ファイル名
    output_file = "python_environment_report.txt"
    pip_file = "requirements.txt"

    # 1. 詳細なレポートを作成
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=== Python Environment Report ===\n")
        f.write(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        # Python本体の情報
        f.write("[Python Information]\n")
        f.write(f"Version    : {sys.version}\n")
        f.write(f"Executable : {sys.executable}\n")
        f.write(f"Platform   : {platform.platform()}\n\n")

        # ライブラリ一覧 (pip freeze)
        f.write("[Installed Libraries]\n")
        try:
            # pip freeze を実行して結果を取得
            libraries = subprocess.check_output([sys.executable, "-m", "pip", "freeze"]).decode("utf-8")
            f.write(libraries)
            
            # 別ファイルとして requirements.txt も生成（復元用）
            with open(pip_file, "w", encoding="utf-8") as pf:
                pf.write(libraries)
                
            print(f"Success!")
            print(f"- Detailed report: {output_file}")
            print(f"- Dependencies list: {pip_file}")
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    export_environment()
