# In python, a dictionary is a collection of unordered mutable values and their keys enclosed by {}. In view
# of this you are required to write a python program:
# a) To read a finite number of products, their product codes, names and their corresponding prices
# then store this information in a dictionary
# b) To display all the products in the format: product_ code, name price in tabular form
# c) To display all the values in the dictionary created in a)
# d) To receive product code then display the product code, name and price if the product exist in the
# dictionary otherwise display “product code not found”.
dictProducts = {}

no = eval(input("Enter the number of products: "))
for i in range(no):
    productCode = input("Enter the Product Code : ")
    productName = input("Enter the Product Name : ")
    productPrice = eval(input("Enter the Product Price : "))

    dictProducts[productCode] = {"Product Name" : productName, "Product Price": productPrice}


# b) display the products in table form
print("Product Code\t Product Name\t\t Product Price")
for code, details in dictProducts.items():
    print(f"{code}\t\t{details['Product Name']}\t\t{details['Product Price']}")

# c) display all value
print(dictProducts.values())

# d) 
searchCode = input("Enter a product code to search for: ")
if searchCode in dictProducts:
    details = dictProducts[searchCode]
    print(f"Product Code: {productCode}\nName: {details['Product Name']}\nPrice: {details['Product Price']}")
else:
    print("Product code not found.")