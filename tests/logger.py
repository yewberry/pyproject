"""
Test log utility
"""
import sys
sys.path.append('./pyproject')

import zw.logger as logger
logger.get_logger(__name__).debug('haha')
