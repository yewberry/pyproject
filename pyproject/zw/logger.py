import logging
import logging.config

def get_logger(name=__name__):
	'''Get logger with name'''
	logger = logging.getLogger(name)
	logging.config.dictConfig({
		'version': 1,
		'disable_existing_loggers': False,  # this fixes the problem
		'formatters': {
			'simple': {
				'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
			},
		},
		'handlers': {
			'console': {
				'class': 'logging.StreamHandler',
				'formatter': 'simple',
				'level': logging.DEBUG,
			},
			'logfile': {
				'class': 'logging.handlers.RotatingFileHandler',
				'formatter': 'simple',
				'filename': "logs/app.log",
				'maxBytes': 10485760,
				'backupCount': 20,
				'encoding': 'utf8',
				'level': logging.DEBUG,
			}
		},
		'loggers': {
			'': {
				'handlers': ['console', 'logfile'],
				'level': logging.DEBUG,
				'propagate': True
			}
		}
	})
	return logger
