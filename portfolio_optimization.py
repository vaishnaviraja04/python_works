
import numpy as np
import tkinter as tk
from tkinter import ttk
from scipy.optimize import minimize
class PortfolioOptimizerApp:
    """A tkinter-based application for portfolio optimization."""
    def __init__(self,root):
        self.root = root
        self.root.title("Portfolio Optimizer")

        self.Label1 = ttk.Label(root, text="expected returns (comma-seperated):")
        self.Label1.pack()
        self.returns_entry = ttk.Entry(root)
        self.returns_entry.pack()

        self.Label2 = ttk.Label(root, text="Covariance Matrix (rows seperated by semicolon, values comma - seperated):")
        self.Label2.pack()
        self.cov_matrix_entry = ttk.Entry(root)
        self.cov_matrix_entry.pack()

        self.Label3 = ttk.Label(root, text="Risk-free Rate :")
        self.Label3.pack()
        self.risk_free_entry = ttk.Entry(root)
        self.risk_free_entry.pack()

        self.calculate_button = ttk.Button(root, text = "calculate",command=self.calculate_optimization)
        self.calculate_button.pack()

        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack()

    def calculate_optimization(self):
        expected_returns = [float(x.strip()) for x in self.returns_entry.get().split(',')]

        covariance_values = self.cov_matrix_entry.get().split(';')
        covariance_matrix = []
        for row in covariance_values:
            covariance_matrix.append([float(x.strip()) for x in row.split(',')])
        risk_free_rate = float(self.risk_free_entry.get())

        optimal_weights = self.portfolio_optimization(expected_returns, covariance_matrix, risk_free_rate)
        
        self.result_text.delete(1.0,tk.END)
        self.result_text.insert(tk.END,"optimized portfolio weights: \n")
        for i, weight in enumerate(optimal_weights):
            self.result_text.insert(tk.END,f"Asset {i+1}:{weight:0.4f}\n")

    def portfolio_optimization(self, expected_returns, covariance_matrix, risk_free_rate):
        num_assets = len(expected_returns)

        def objective(weights):
            portfolio_return = np.sum(weights * expected_returns)
            portfolio_stddev = np.sqrt(np.dot(weights.T, np.dot(covariance_matrix, weights)))
            sharpe_ratio = (portfolio_return - risk_free_rate)/ portfolio_stddev
            return -sharpe_ratio
        constraints = ({'type':'eq','fun': lambda weights: np.sum(weights)-1})
        bounds = tuple((0,1) for asset in range(num_assets))
        initial_weights = np.array(num_assets * [1./num_assets])

        optimal_weights = minimize(objective, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)
        return optimal_weights.x

if __name__ =="__main__":
    root = tk.Tk()
    app = PortfolioOptimizerApp(root)
    root.mainloop()






     

