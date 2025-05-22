import logging

# 出力ログレベルの設定
# ロガー：ログ出力のインターフェイスを提供する
logging.basicConfig(filename='122_test.log',level=logging.INFO)

logging.critical('critical') # プログラムが実行不可となるような重大なエラーが発生した場合
logging.error('error')       # 重大な問題により、機能を実行できない場合
logging.warning('warning')   # 想定外の処理やそれが起こりそうな場合
logging.info('info')         # 想定内の処理が行われた場合
logging.debug('debug')       # 問題探求に必要な詳細な情報を出力したい場合

# 変数を使いロギングを表示
logging.info('info %s %s' ,'test','test2')

# ロガーを使用
# ロガーを使用するときのnameには__name__を指定するのが一般的
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug('debug')
