import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# function name: least_sq
# inputs: file_name- name of the csv file 
# output: m(slope), b(y-intercept) (IN THAT EXACT ORDER!!!)
        # LITERALLY! return m, b (both rounded 4 decimal places)
        # YOU HAVE BEEN WARNED! YOU WILL GET IT WRONG IF YOU DO NOT RETURN THE CORRECT THINGS IN THE CORRECT ORDER!!!!
# assumptions: The csv file will always have headers in the order of: x, y
def least_sq(file_name):
    df_xy = pd.read_csv(file_name)
    np_x = df_xy['x'].to_numpy()
    np_y = df_xy['y'].to_numpy()
    x_square = np_x**2
    xy =  np_x * np_y
    x_sum = np.sum(np_x)
    y_sum = np.sum(np_y)
    x_square_sum = np.sum(x_square)
    xy_sum = np.sum (xy)
    n = len(np_x)
    
    slop = ((n*xy_sum) - (x_sum * y_sum))  /  ((n * x_square_sum) - (x_sum**2))
    
    y_int = (y_sum - (slop * x_sum)) / n
    
    m = round(slop, 4)  
    b = round(y_int, 4) 

    return m, b

# function name: mat_least_sq
# inputs: file_name- name of the csv file 
# output: m (slope), b(y-intercept) (IN THAT EXACT ORDER!!!)
        # LITERALLY! return m, b (both rounded 4 decimal places)
        # YOU HAVE BEEN WARNED! YOU WILL GET IT WRONG IF YOU DO NOT RETURN THE CORRECT THINGS IN THE CORRECT ORDER!
# assumptions: The csv file will always have headers in the order of: x, y
def mat_least_sq(file_name):
    df_xy = pd.read_csv(file_name)
    np_x = df_xy['x'].to_numpy()
    np_y = df_xy['y'].to_numpy()
    n = len(np_x)
    

    one_vec = np.ones((n))
    # matrix X
    mat_x = np.array(np.column_stack((np_x, one_vec)))
    
    #matrix X transpose
    mat_X_tranpose = mat_x.transpose()
    
    # x_transpose * x
    X_t_x = np.dot(mat_X_tranpose, mat_x)
    
    #inverse of (x_transpose * x)
    inv = np.linalg.inv(X_t_x)
    
    #x_transpose * y
    X_t_y = np.dot(mat_X_tranpose, np_y)
    
    #inverse of (x_transpose * x) * Y
    [m,b]= np.dot(inv, X_t_y)
    
    m = round(m, 4) 
    b = round(b, 4) 
    

    return m,b
    


# function name: plot_reg
# inputs: mat - file_name- name of the csv file
        # using_matrix: True if you are plotting the linear equation from mat_least_Sq
        #                 False if you are plotting the linear equation from least_sq
# output: NA
# task: given file_name, compute the linear equation using least_sq or mat_least_sq and graph results
    #    your graph should have the following: labeled x and y axes, title, legend
# assumptions: The csv file will always have headers in the order of: x, y
def plot_reg(file_name, using_matrix):
    df_xy = pd.read_csv(file_name)
    np_x = df_xy['x'].to_numpy()
    np_y = df_xy['y'].to_numpy()
    
    if using_matrix == False:
        m,b = least_sq(file_name)
        
        y = [m * x + b for x in np_x]
        
        plot1 = plt.figure(1)
        plot1 = plt.plot(np_x, y, 'b')
        plot1 = plt.scatter (np_x, np_y)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Using Algebra Least Squares")
    
        plt.legend(["y = "+str(m)+ "x + "+ str(b), "Data Point"])
        
    if using_matrix == True:
        m,b = mat_least_sq(file_name)

        y = [m * x + b for x in np_x]
        
        plot2 = plt.figure(2)
        plot2 = plt.plot(np_x, y, 'b')
        plot2 = plt.scatter (np_x, np_y)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Using Matrix Least Squares") 
        plt.legend(["y = "+str(m)+ "x + "+ str(b), "Data Point"])
        

