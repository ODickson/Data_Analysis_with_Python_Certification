import numpy as np

def calculate(list):
    if len(list) == 9:
        matrix = np.array([list[0:3],
                           list[3:6],
                           list[6:]])
    
        calculations = {
          
            'mean': [np.mean(matrix,axis=0).tolist(), np.mean(matrix,axis=1).tolist(), np.mean(matrix).tolist()],
          
            'variance': [np.var(matrix,axis=0).tolist(), np.var(matrix,axis=1).tolist(), np.var(matrix).tolist()],
          
            'standard deviation': [np.std(matrix,axis=0).tolist(), np.std(matrix,axis=1).tolist(), np.std(matrix).tolist()],
          
            'max': [np.max(matrix,axis=0).tolist(), np.max(matrix,axis=1).tolist(), np.max(matrix).tolist()],
          
            'min': [np.min(matrix,axis=0).tolist(), np.min(matrix,axis=1).tolist(), np.min(matrix).tolist()],
          
            'sum': [np.sum(matrix,axis=0).tolist(), np.sum(matrix,axis=1).tolist(), np.sum(matrix).tolist()]  
        }
        
        return calculations 
    else:
        raise ValueError("List must contain nine numbers.")