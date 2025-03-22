from itertools import permutations, combinations, product

def evaluate_expression(expression):
    """
    Evaluate a mathematical expression safely.
    """
    try:
        return eval(expression)
    except:
        return None

def generate_expressions(digits):
    """
    Generate all valid expressions using the digits and the four arithmetic operations.
    """
    operations = ['+', '-', '*', '/']
    expressions = set()

    # Generate all permutations of the digits
    for nums in permutations(digits):
        # Generate all combinations of operations
        for ops in product(operations, repeat=3):
            # Generate all possible parenthetical groupings
            # Case 1: (a op1 b) op2 (c op3 d)
            expr1 = f"({nums[0]}{ops[0]}{nums[1]}){ops[1]}({nums[2]}{ops[2]}{nums[3]})"
            # Case 2: ((a op1 b) op2 c) op3 d
            expr2 = f"(({nums[0]}{ops[0]}{nums[1]}){ops[1]}{nums[2]}){ops[2]}{nums[3]}"
            # Case 3: (a op1 (b op2 c)) op3 d
            expr3 = f"({nums[0]}{ops[0]}({nums[1]}{ops[1]}{nums[2]})){ops[2]}{nums[3]}"
            # Case 4: a op1 (b op2 (c op3 d))
            expr4 = f"{nums[0]}{ops[0]}({nums[1]}{ops[1]}({nums[2]}{ops[2]}{nums[3]}))"
            # Case 5: a op1 ((b op2 c) op3 d)
            expr5 = f"{nums[0]}{ops[0]}(({nums[1]}{ops[1]}{nums[2]}){ops[2]}{nums[3]})"

            # Evaluate all expressions and add valid results to the set
            for expr in [expr1, expr2, expr3, expr4, expr5]:
                result = evaluate_expression(expr)
                if result is not None and result == int(result) and result > 0:
                    expressions.add(int(result))

    return expressions

def find_optimal_digit_set():
    """
    Find the set of four digits that produces the longest sequence of consecutive integers.
    """
    max_consecutive = 0
    optimal_set = None

    for digits in combinations(range(1, 10), 4):
        expressions = generate_expressions(digits)
        sorted_results = sorted(expressions)

        consecutive = 0
        for i in range(1, len(sorted_results) + 1):
            if i in sorted_results:
                consecutive += 1
            else:
                break

        if consecutive > max_consecutive:
            max_consecutive = consecutive
            optimal_set = digits

    return ''.join(map(str, sorted(optimal_set)))

def main():
    result = find_optimal_digit_set()
    print(f"The optimal set of digits is: {result}")

if __name__ == "__main__":
    main()