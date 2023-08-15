#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:skyoceanchen
# project_name:mysite
# py_name :decorator_operation
# software: PyCharm
# datetime:2021/5/17 10:19
import time


# 装饰器方法
# 装饰器
# <editor-fold desc="验证列表的装饰器">
def list_verify(func):
    def wrapper(*args, **kwargs):
        lis = []
        if args:
            lis = [i for i in args if isinstance(i, list)]
            if lis:
                lis = lis[0]
        if not lis:
            if kwargs:
                lis = [i for i in list(kwargs.values()) if isinstance(i, list)]
                if lis:
                    lis = lis[0]
        if not lis or not isinstance(lis, list):
            return lis
        res = func(*args, **kwargs)
        return res

    return wrapper


# </editor-fold>
# Test function execution time
# <editor-fold desc="查看函数执行时间的装饰器">
def timer(func):
    """
    优化代码性能是非常重要的。@timer装饰器可以帮助我们跟踪特定函数的执行时间。
    通过用这个装饰器包装函数，我可以快速识别瓶颈并优化代码的关键部分
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds to execute.")
        return result

    return wrapper


# </editor-fold>
# <editor-fold desc="缓存结果">
def memoize(func):
    """
    在数据科学中，我们经常使用计算成本很高的函数。@memoize装饰器帮助我缓存函数结果，避免了相同输入的冗余计算，显著加快工作流程:
    在递归函数中也可以使用@memoize来优化重复计算
    """
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


# </editor-fold>
# <editor-fold desc="日志输出">
def log_results(func):
    """
    在运行复杂的数据分析时，跟踪每个函数的输出变得至关重要。@log_results装饰器可以帮助我们记录函数的结果，以便于调试和监控.
    将@log_results与日志库结合使用，以获得更高级的日志功能。
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("results.log", "a") as log_file:
            log_file.write(f"{func.__name__} - Result: {result}\n")
        return result

    return wrapper


# </editor-fold>
# <editor-fold desc="错误处理">
def suppress_errors(func):
    """
    数据科学项目经常会遇到意想不到的错误，可能会破坏整个计算流程。@suppress_errors装饰器可以优雅地处理异常并继续执行.
    可以避免隐藏严重错误，还可以进行错误的详细输出，便于调试。
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            return None

    return wrapper


# </editor-fold>
# <editor-fold desc="重试执行">
def retry(max_attempts, delay):
    """
    max_attempts 最大尝试次数
    delay 延迟s
    """
    """# @retry装饰器帮助我在遇到异常时重试函数执行，确保更大的弹性
    使用@retry时应避免过多的重试。
    @retry(max_attempts=3, delay=2)
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempts + 1} failed. Retrying in {delay} seconds.")
                    attempts += 1
                    time.sleep(delay)
            raise Exception("Max retry attempts exceeded.")

        return wrapper

    return decorator


# </editor-fold>
