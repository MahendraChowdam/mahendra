import time

def log_execution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result
    return wrapper


def admin_only(func):
    def wrapper(role, *args, **kwargs):
        if role != "admin":
            print("Access Denied: Admin privileges required")
            return
        return func(role, *args, **kwargs)
    return wrapper


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Execution Time: {time.time()-start:.4f} sec")
        return result
    return wrapper
