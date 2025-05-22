import logging
import logging_handler

# 出力ログレベルの設定
logging.basicConfig(level=logging.INFO)

# 変数を使いロギングを表示
logger = logging.getLogger(__name__)
logging.info('from main')

logging_handler.do_something()

