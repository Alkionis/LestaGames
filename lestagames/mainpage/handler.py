# модуль, содержащий описание обработки загруженного файда
import math
import re
from collections import Counter

# разбиение текста на слова и удаление знаков препинания
def tokenize(text):
    text = re.sub(r'[^\w\s]', '', text)
    return text.split()

# вычисление tf-a
def calculate_tf(token):
    token_count = len(token)
    tf_counts = Counter(token)
    tf = {token: count / token_count for token, count in tf_counts.items()}
    return tf


# вычисление idf-a
def calculate_idf(tokens):
    total_documents = len(tokens)
    all_tokens = [token for toc in tokens for token in set(toc)]
    token_document_count = Counter(all_tokens)

    idf = {token: math.log(total_documents / (token_document_count[token] + 1)) for token in token_document_count}
    return idf

# функция обработки файла
def handle_uploaded_file(f):
    result_filtered = []
    str_text = ''
    for line in f:
        str_text = str_text + line.decode()

    tokens = tokenize(str_text)
    tf = calculate_tf(tokens)
    idf = calculate_idf([tokens])

    for word, tf_value in tf.items():
        idf_value = idf.get(word, 0)
        result = {"word": word, "TF": tf_value, "IDF": idf_value}
        result_filtered.append(result)

    result_filtered = sorted(result_filtered, key=lambda x: x["IDF"], reverse=True)
    result_filtered = result_filtered[:50]
    return result_filtered
