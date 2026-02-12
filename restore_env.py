import sys
import subprocess
import os

def restore_env():
    req_file = "requirements.txt"

    # ファイルの存在確認
    if not os.path.exists(req_file):
        print(f"Error: {req_file} が見つかりません。先に書き出しを行ってください。")
        return

    print(f"--- Restoring Environment ---")
    print(f"Reading from: {req_file}")

    try:
        # pip install を実行
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_file])
        print("\nSuccessfully restored all libraries.")
    except Exception as e:
        print(f"\nRestore failed: {e}")

if __name__ == "__main__":
    restore_env()
