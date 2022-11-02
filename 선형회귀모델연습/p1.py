y_pred = a * x + b
error = y - y_pred

a_diff = (2/n) * sum(-x*(error))
b_diff = (2/n) * sum(-(error))