import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 1105798394 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y:np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
   pvalue = ttest_ind(x,y,equal_var=False).pvalue
   return True if pvalue < 0.09 else False # Ваш ответ, True или False
