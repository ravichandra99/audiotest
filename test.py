import time
def foo(bar, baz):
  print('hello {0}'.format(bar))
  return 'foo' + baz

from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=1)

async_result = pool.apply_async(foo, ('world', 'foo')) # tuple of args for foo

# do some other stuff in the main process
time.sleep(10)

return_val = async_result.get()  # get the return value from your function.
print(return_val)