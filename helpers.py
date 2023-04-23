import matplotlib.pyplot as plt 

def plot_results(df_results):
    # Total debt over time. 
    plt.figure()
    plt.title('Total debt over time')
    plt.xlabel('Month Number')
    plt.ylabel('Amount')
    plt.grid(True)
    plt.plot(df_results['month'], df_results['total_debt'], label='total debt')
    plt.plot([0, num_months], [df_results['total_limit'][0], df_results['total_limit'][num_months - 1]], color='red', label='Total available credit limit')
    plt.ylim([0, max(df_results['total_limit'])*1.01])
    plt.legend()
    
    # Total monthly interest due 
    plt.figure() 
    plt.title('Total monthly interest due per month')
    plt.xlabel('Month number')
    plt.ylabel('Monthly interest cost')
    plt.grid(True)
    plt.plot(df_results['month'], df_results['total_annual_interest_due']/12)
    
    # Total credit utilization 
    plt.figure() 
    plt.title('Percent credit utilization per month')
    plt.xlabel('Month number')
    plt.ylabel('\% Credit Utilization')
    plt.grid(True)
    plt.plot(df_results['month'], df_results['total_credit_utilization'], label='\% credit utilization')
    plt.plot([0,num_months], [1,1], color='red', label='credit_limit')
    plt.ylim([0,1.1])
    
    # Total Minimum Payments over time 
    plt.figure()
    plt.title('Minimum payments per month')
    plt.xlabel('Month number')
    plt.ylabel('Minimum repayment amount')
    plt.grid(True)
    plt.plot(df_results['month'], df_results['total_min_payments'])