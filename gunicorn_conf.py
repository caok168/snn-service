bind = '0.0.0.0:5002'
workers = 1
worker_class = 'gevent'
timeout = 1200

proc_name = 'snn-api'

accesslog = '-'
errorlog = '-'
loglevel = 'info'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(L)s'
