import logging

# 出力ログレベルの設定
# ロギングをログファイルに書き込むときはfilename属性で指定
logging.basicConfig(filename='120_test.log',level=logging.INFO)

logging.critical('critical') # プログラムが実行不可となるような重大なエラーが発生した場合
logging.error('error')       # 重大な問題により、機能を実行できない場合
logging.warning('warning')   # 想定外の処理やそれが起こりそうな場合
logging.info('info')         # 想定内の処理が行われた場合
logging.debug('debug')       # 問題探求に必要な詳細な情報を出力したい場合

# 変数を使いロギングを表示
logging.info('info %s %s' ,'test','test2')
