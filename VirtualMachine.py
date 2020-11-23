from Quadruples import Quadruples
from constants import Operator, Scope, Type
from RuntimeMemory import RuntimeMemory


class VirtualMachine():
    def __init__(self, quadruples, constants):
        self.quadruples = quadruples
        self.constants = constants
        self.quad_pointer = 0
        self.memories = []
        self.g_memory = RuntimeMemory(Scope.GLOBAL, -1)
        self.memories.append(self.g_memory)
        self.return_val = None
        self.calling_function = False

    def get_value_from_address(self, address, from_previous_memory=False):
        if self.is_global_address(address):
            return self.g_memory.get_value_from_address_helper(address)
        elif self.is_local_or_temp_address(address):
            index = -2 if from_previous_memory else -1
            return self.memories[index].get_value_from_address_helper(address)
        elif self.is_pointer(address):
            aux = self.memories[-1].get_value_from_address_helper(-address)
            return self.memories[-1].get_value_from_address_helper(aux)
        else:
            return self.constants[address]

    def set_value_to_address(self, value, address, from_previous_memory=False):
        index = -2 if from_previous_memory else -1
        if self.is_global_address(address):
            self.g_memory.set_value_to_address_helper(value, address)
        elif self.is_local_or_temp_address(address):
            self.memories[index].set_value_to_address_helper(value, address)
        elif self.is_pointer(address):
            aux = self.memories[index].get_value_from_address_helper(-address)
            self.memories[index].set_value_to_address_helper(value, aux)

    def is_global_address(self, address):
        return address >= self.g_memory.g_int_start and address < (self.g_memory.g_string_start + 1000)

    def is_local_or_temp_address(self, address):
        return address >= self.memories[-1].l_int_start and address < (self.memories[-1].t_string_start + 1000)

    def is_pointer(self, address):
        return address < 0

    def refactor_if_string(self, input):
        if input != None and type(input) == str:
            if input[0] == '\"' and input[-1] == '\"':
                if input[1] == ' ' and input[-2] == ' ':
                    return input[2:-2]
                else:
                    return input[1:-1]
        return input

    def get_read_type(self, read_input):
        try:
            read_input = int(read_input)
            return read_input, Type.INT
        except ValueError:
            try:
                read_input = float(read_input)
                return read_input, Type.FLOAT
            except ValueError:
                return read_input, Type.STRING

    def run(self):
        while self.quad_pointer < len(self.quadruples):
            self.process_quad(self.quadruples[self.quad_pointer])
            self.quad_pointer += 1

    def process_quad(self, quad):
        if quad[0] == Operator.POSITIVE_SIGN:
            value = self.get_value_from_address(quad[1])
            value = + value
            self.set_value_to_address(value, quad[3])
            return
        elif quad[0] == Operator.NEGATIVE_SIGN:
            value = self.get_value_from_address(quad[1])
            value = - value
            self.set_value_to_address(value, quad[3])
            return
        elif quad[0] == Operator.NOT:
            value = self.get_value_from_address(quad[1])
            value = int(not value)
            self.set_value_to_address(value, quad[3])
            return
        elif quad[0] == Operator.ASSIGN:
            result = self.get_value_from_address(quad[1])
            self.set_value_to_address(result, quad[3])
            return
        elif quad[0] == Operator.GOTO:
            # Operator.GOTO, None, None, destination.
            self.quad_pointer = quad[3] - 1
            return
        elif quad[0] == Operator.GOTOF:
            # Operator.GOTOF, condition, None, destination.
            condition = self.get_value_from_address(quad[1])
            if condition == 0:
                self.quad_pointer = quad[3] - 1
            return
        elif quad[0] == Operator.ERA:
            self.calling_function = True
            new_memory_instance = RuntimeMemory(Scope.LOCAL, -1)
            self.memories.append(new_memory_instance)
            return
        elif quad[0] == Operator.RETURN:
            # WIP
            if self.memories[-1].scope == Scope.GLOBAL:
                self.quad_pointer = len(self.quadruples) - 1

            self.return_val = self.get_value_from_address(quad[1])
            self.set_value_to_address(self.return_val, quad[2])
            self.quad_pointer = quad[3] - 1
            return
        elif quad[0] == Operator.PRINT:
            address = quad[3]
            if address is None:
                print()
                return
            value_to_print = self.get_value_from_address(quad[3])
            value_to_print = self.refactor_if_string(value_to_print)
            print(value_to_print, '', end='')
            return
        elif quad[0] == Operator.READ:
            operand_type = quad[2]
            address = quad[3]
            read_input = input()
            read_input, read_input_type = self.get_read_type(read_input)
            # Type validation
            if operand_type != read_input_type:
                raise NameError(
                    f'Invalid input type. Expected {operand_type}, got {read_input_type} instead.')
            self.set_value_to_address(read_input, address)
            return
        elif quad[0] == Operator.END:
            self.quad_pointer = len(self.quadruples) - 1
            return
        elif quad[0] == Operator.VER:
            index = self.get_value_from_address(quad[1])
            lim_inf = self.get_value_from_address(quad[2])
            lim_sup = self.get_value_from_address(quad[3])
            # print("lim_inf", lim_inf, " lim_sup", lim_sup)
            # print("index", index)
            if not lim_inf <= index <= lim_sup:
                raise NameError(f'array index out of range')
            return
        elif quad[0] == Operator.GOSUB:
            self.memories[-1].return_quad = self.quad_pointer
            self.quad_pointer = quad[3] - 1
            self.calling_function = False
            return
        elif quad[0] == Operator.PARAM:
            result_val = self.get_value_from_address(
                quad[1], from_previous_memory=self.calling_function)
            self.set_value_to_address(result_val, quad[3])
            return
        elif quad[0] == Operator.ENDFUNC:
            self.quad_pointer = self.memories[-1].return_quad
            self.memories.pop()
            return

        # Expression operands.
        left_operand = self.get_value_from_address(
            quad[1], from_previous_memory=self.calling_function)
        right_operand = self.get_value_from_address(
            quad[2], from_previous_memory=self.calling_function)

        result = None

        if quad[0] == Operator.PLUS:
            result = left_operand + right_operand
        elif quad[0] == Operator.MINUS:
            result = left_operand - right_operand
        elif quad[0] == Operator.TIMES:
            result = left_operand * right_operand
        elif quad[0] == Operator.DIVIDE:
            if right_operand == 0:
                raise NameError(f"Division by zero!")
            result = left_operand / right_operand
        elif quad[0] == Operator.GREATER:
            result = left_operand > right_operand
            result = 1 if result == True else 0
        elif quad[0] == Operator.LESS:
            result = left_operand < right_operand
            result = 1 if result == True else 0
            # print(left_operand, right_operand, result)
        elif quad[0] == Operator.GREATER_EQ:
            result = left_operand >= right_operand
            result = 1 if result == True else 0
        elif quad[0] == Operator.LESS_EQ:
            result = left_operand <= right_operand
            result = 1 if result == True else 0
        elif quad[0] == Operator.EQUALS:
            result = left_operand == right_operand
            result = 1 if result == True else 0
        elif quad[0] == Operator.NOT_EQUAL:
            result = left_operand != right_operand
            result = 1 if result == True else 0
        elif quad[0] == Operator.AND:
            result = 1 if (left_operand and right_operand) else 0
            result = 1 if result == True else 0
        elif quad[0] == Operator.OR:
            result = 1 if (left_operand or right_operand) else 0
            result = 1 if result == True else 0
        else:
            return

        self.set_value_to_address(
            result, quad[3], from_previous_memory=self.calling_function)
