s = 'В кабинете Варьете находились двое: сам Римский и админимтратор Варенуха'
lower_ = list(filter(lambda x: x.islower(),list(s)))
upper_ = list(filter(lambda x: x.isupper(),list(s)))
print('Количество символов в верхнем регистре:', len(upper_))
print('Количество символов в нижнем регистре:', len(lower_))