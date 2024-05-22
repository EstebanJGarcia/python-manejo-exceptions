import logging
import traceback

logging.basicConfig(
    level=logging.ERROR,
    filename='error.log',
    format="%(asctime)s:%(levelname)s:%(message)s"
)

try:
    10 / 0

except Exception as error:
    exception_info = {
        'message': str(error),
        'detail':  traceback.format_exc()
    }
    logging.error( exception_info)