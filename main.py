import datetime
import random
from datetime import date
import numpy as np
import statistics
import matplotlib.pyplot as plt

# 1. Сам код (основной процесс)
def run_until_done(backlog_size, size_estimate):

    s1 = size_estimate[0]
    s2 = size_estimate[1]
    s3 = size_estimate[2]

    backlog_size = round(backlog_size * random.triangular(s1, s2, s3))  # Округлить согласно данным по варианту
    sprints = []

    while backlog_size > 0:
        new_sprint = random.choice(sprint_samples)
        sprints.append(new_sprint)
        backlog_size -= new_sprint

    return sprints

# 2. Прогнозирование (или итог)
def predict_sprint_count(backlog_size, size_estimate, sim_count=10000):
    samples = []

    for i in range(sim_count):
        sample = len(run_until_done(backlog_size, size_estimate))
        samples.append(sample)

    return samples


if __name__ == '__main__':
    sprint_samples = [5, 11, 8, 7, 6, 8, 11]
    start_date = date(2023, 9, 11)

    counts = predict_sprint_count(100, (1.2, 1.5, 3))  # 1 - backlog_size, 2 - оценки
    count_percentiles = statistics.quantiles(counts)

    count_estimate = np.quantile(count_percentiles, q=0.85)
    finish_date = start_date.toordinal() + (14 * round(count_estimate))
    print("Дата окончания проекта: ", datetime.datetime.fromordinal(finish_date))
    print("Количество необходимых спринтов: ", round(np.mean(counts)))
    plt.hist(counts)
    plt.title("Гистограмма спринтов")
    plt.show()
