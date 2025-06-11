def matthews(y_true, y_pred):
    from math import sqrt

    """
            P  = Total number of positives
            N  = Total number of negatives
            Tp = number of true positives
            Fp = number of false positives
        """
    if type(y_true) == pd.Series:
        y_true = y_true.values

    P = len([x for x in y_true if x == 1])
    N = len([x for x in y_true if x == 0])

    Tp, Fp = 0, 0
    for i in range(len(y_true)):
        if y_true[i] == 1 and y_pred[i] == 1:
            Tp += 1
        elif y_true[i] == 0 and y_pred[i] == 1:
            Fp += 1

    Tn = N - Fp
    Fn = P - Tp

    try:
        mcc = (Tp * Tn - Fp * Fn) / sqrt((Tn + Fn) * (Tn + Fp) * (Tp + Fn) * (Tp + Fp))
    except ZeroDivisionError:
        mcc = 0
    return (mcc, f"P: {P:_} Tp: {Tp:_} Fp: {Fp:_} N: {N:_} Tn: {Tn:_} Fn: {Fn:_}")
