TOKEN = '7834043258:AAGQ6YGfIe-Eet7MRCIhybU5qRzjxJYZCqw'

curr_dict = {'Евро':'EUR', 'Доллар':'USD', 'Рубль':'RUB'}
formatted_dict = '\n'.join([f'{i+1}. {curr}' for i, curr in enumerate(curr_dict.keys())])