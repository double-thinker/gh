"""
Este módulo contiene helpers para el preprocesamiento de datos
"""

import numpy as np

def get_numerical_features(df):
    """get_numerical features devuelve una lista
    con el nombre de las columnas que contienen datos
    de tipo numérico

    :param df: dataframe
    :type df: pandas.DataFrame
    :return: lista de nombres de columnas
    :rtype: List[str]

    >>> print(1+1)
    2
    """
    return list(df.select_dtypes(include=[np.number]).columns)

class A:
    """
    asdasd
    """
    def __init__(self):
        """_summary_
        """
        pass

    def jaja(self, a):
        """
        adasd

        :param a: _description_
        :type a: int
        """
        pass