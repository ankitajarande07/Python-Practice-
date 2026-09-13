def emp(id, name, sal, dept):
    data = f'ID:{id}\nNAME:{name}\nSAL:{sal}\nDEPT:{dept}'
    return data


res = emp(101, sal=35000, name='ABC', dept='IT')
print(res)