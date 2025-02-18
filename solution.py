import pandas as pd
import numpy as np

from scipy.stats import expon


chat_id = 959806937 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
#    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return 2*loc / (59*59) + expon.ppf((1 + alpha) / 2), \
            2*loc / (59*59) + expon.ppf((1 - alpha) / 2)
