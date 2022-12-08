from tasks import add

result = add.delay(1, 1)

print(result.get(timeout=0))
