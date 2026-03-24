orders = ["Vivek", "Satyajeet","Vivek","Rutuj","Vivek"]
unique_Cust = set(orders)
print(unique_Cust)
print("-------------------------------------------------------")

electronics = {"Vivek","Rutuj","Sagar"}
clothing = {"Vivek","Rutuj","Satyajeet"} 


common_cust = electronics & clothing
print(common_cust)