#subtraction function 
def minus(left, right):
    return left - right #bilangan operator kiri dikurangi kanan

#multiplication function
def mult(left, right):
    return left * right #bilangan operator kiri dikali kanan

#distribution function
def div(left, right):
    if right != 0:
        return left / right #bilangan tidak boleh dibagi dengan = 0 karena hasil tidak terdefinisi
    else:
        return print("Error Message: bilangan tidak boleh dibagi dengan 0")

def tree(expression):
    if isinstance(expression, tuple):
        left, operator, right = expression
        if operator == '+':
            return tree(left) + tree(right)
        elif operator == '-':
            return minus(tree(left), tree(right))
        elif operator == '*':
            return mult(tree(left), tree(right))
        elif operator == '/':
            return div(tree(left), tree(right))
    else:
        return expression
    
#contoh Pohon ekspresi : (2 + 3) * (5 - 1)
expression_tree = ((2, '+', 3), '*', (5, '-', 1))
result1 = tree(expression_tree)

#Evaluasi pohon ekspresi dengan fungsi pada paradigma fungsional
print("Hasil Evaluasi Pohon Ekspresi:",result1)

#crosscheck
expression_tree = ((5, '+', 3), '/', (6, '-', 2))
result2 = tree(expression_tree)
print("Hasil Evaluasi Pohon Ekspresi:",result2)
casting = int (result2)
print("Hasil casting ke int: ", casting)
print(type(casting))
