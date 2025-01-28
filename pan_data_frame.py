import pandas as pd
pan_data = {
    'cars': ['BMW', 'VOLVO', 'FORD' ],
    'models': [25, 26, 27]
}
pan_data_frame = pd.DataFrame(pan_data)
print(pan_data_frame)