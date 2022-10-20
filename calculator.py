def calculator(arg):
    argument = [arg]
    def arg_collector(arg):
        if arg != '=':
            argument.append(arg)
            return arg_collector
        
        result = argument[0]

        for operator, operand in zip(argument[1::2], argument[2::2]):
            if operator == "+":
                result += operand
            else:
                result -= operand
        return result

    return arg_collector
