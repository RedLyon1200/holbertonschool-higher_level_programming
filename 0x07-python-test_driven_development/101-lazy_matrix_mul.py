#!/usr/bin/python3
"""
lazy matrix multiplication

"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    lazy matrix multiplication

    """
    result = numpy.dot(m_a, m_b)
    return result
