import time
import subprocess

while True:
    # 120時間待つ
    time.sleep(60)
    
    # Python0スクdリプトを実行する
    subprocess.run(['python', 'tw-seeking_alpha.py'])

while True:
    # 100時間待つ
    time.sleep(70)
    
    # Pythonスクリプトを実行する
    subprocess.run(['python', 'tw-deepl3.py'])

while True:
    # 1時間待つ
    time.sleep(80)
    
    # Pythonスクリプトを実行する
    subprocess.run(['python', 'tw-globenewswire.py'])

while True:
    # 1時間待つ
    time.sleep(90)
    
    # Pythonスクリプトを実行する
    subprocess.run(['python', 'tw-tdnet_all.py'])

# while True:
#     # 1時間待つ
#     time.sleep(60)
    
#     # Pythonスクリプトを実行する
#     subprocess.run(['python', 'tw-seeking_alpha.py'])
