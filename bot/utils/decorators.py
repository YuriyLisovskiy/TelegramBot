import threading


def run_async(func):
	def wrapper(*args, **kwargs):
		thread = threading.Thread(target=func, args=args, kwargs=kwargs, daemon=True)
		thread.start()
	return wrapper
