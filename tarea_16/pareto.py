"""
@author: Jesus Rivera
CDMX
find the pareto front using own methods, pareto and my_pareto
and methods described here
https://stackoverflow.com/questions/32791911/fast-calculation-of-pareto-front-in-python.
"""
import csv
import timeit
import numpy as np


# Very slow for many datapoints.  Fastest for many costs, most readable
def is_pareto_efficient_dumb(costs):
    """
    Find the pareto-efficient points
    :param costs: An (n_points, n_costs) array
    :return: A (n_points, ) boolean array, indicating whether each point is Pareto efficient
    """
    is_efficient = np.ones(costs.shape[0], dtype=bool)
    for i, c in enumerate(costs):
        is_efficient[i] = np.all(np.any(costs[:i] > c, axis=1)) \
                          and np.all(np.any(costs[i + 1:] > c, axis=1))
    return is_efficient


# Fairly fast for many datapoints, less fast for many costs, somewhat readable
def is_pareto_efficient_simple(costs):
    """
    Find the pareto-efficient points
    :param costs: An (n_points, n_costs) array
    :return: A (n_points, ) boolean array, indicating whether each point is Pareto efficient
    """
    is_efficient = np.ones(costs.shape[0], dtype=bool)
    for i, c in enumerate(costs):
        if is_efficient[i]:
            # Keep any point with a lower cost
            is_efficient[is_efficient] = np.any(costs[is_efficient] < c, axis=1)
            is_efficient[i] = True  # And keep self
    return is_efficient


# Faster than is_pareto_efficient_simple, but less readable.
def is_pareto_efficient(costs, return_mask=True):
    """
    Find the pareto-efficient points
    :param costs: An (n_points, n_costs) array
    :param return_mask: True to return a mask
    :return: An array of indices of pareto-efficient points.
        If return_mask is True, this will be an (n_points, ) boolean array
        Otherwise it will be a (n_efficient_points, ) integer array of indices.
    """
    is_efficient = np.arange(costs.shape[0])
    n_points = costs.shape[0]
    next_point_index = 0  # Next index in the is_efficient array to search for
    while next_point_index < len(costs):
        nondominated_point_mask = np.any(costs < costs[next_point_index], axis=1)
        nondominated_point_mask[next_point_index] = True
        is_efficient = is_efficient[nondominated_point_mask]  # Remove dominated points
        costs = costs[nondominated_point_mask]
        next_point_index = np.sum(nondominated_point_mask[:next_point_index]) + 1
    if return_mask:
        is_efficient_mask = np.zeros(n_points, dtype=bool)
        is_efficient_mask[is_efficient] = True
        return is_efficient_mask
    return is_efficient


def dominates(row, row_candidate):
    """
    check if row dominates row_candidate
    :param row:
    :param row_candidate:
    :return:
    """
    return all(r >= rc for r, rc in zip(row, row_candidate))


def get_data(filename):
    """
        reads data from filename
    :param filename: name of the file
    :return: data as dict with (symb1,symb2) as keys
    """
    result = {}
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            symb1, symb2, *values = row
            values = [float(elto) for elto in values]
            result[(symb1, symb2)] = values
    return result


def get_data2(filename):
    """
        reads data from filename
    :param filename: name of the file
    :return: data as list withoun symbs
    """
    result = []
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            _, _, *values = row
            values = [float(elto) for elto in values]
            result.append(values)
    return result


def pareto_front(data):
    """
        find the pareto front
    :param data: dict with points to find the pareto front
    :return: pareto front
    """
    pareto = []
    remaining = data
    while remaining:
        keys = list(remaining.keys())
        aux_key = keys.pop()
        candidate = remaining.pop(aux_key)
        dom = False
        for key in keys:
            to_test = remaining[key]
            if dominates(candidate, to_test):
                del remaining[key]
            elif dominates(to_test, candidate):
                dom = True
                break
        if not dom:
            pareto.append((aux_key, candidate))
    return pareto


def my_pareto(costs):
    """
    Find the pareto-efficient points
    :param costs: An (n_points, n_costs) array
    :return: A (n_points, ) boolean array, indicating whether each point is Pareto efficient
    """
    #    is_efficient = array.array('B', [True]*len(costs))
    is_efficient = [True] * len(costs)
    for i, c in enumerate(costs):
        if is_efficient[i]:
            for j, c1 in enumerate(costs):
                if i != j and is_efficient[j]:
                    #                    print(f"{i}-{j}")
                    if dominates(c, c1):
                        is_efficient[j] = False
                    #                        print(f"{i} dominates {j}")
                    elif dominates(c1, c):
                        #                        print(f"{j} dominates {i}")
                        is_efficient[i] = False
                        break
    return is_efficient
"""
    with open('results.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Symbol 1", "Symbol 2", "APR", "SHARPE", "price"])
        for x, y in pareto:
            s1, s2 = x
            row = [s1, s2] + y
            writer.writerow(row)"""


