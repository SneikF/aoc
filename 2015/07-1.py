from dataclasses import dataclass
from enum import auto, Enum

x = 123
y = 456

class Operator(Enum):
   And = auto()
   Or = auto()
   LShift = auto()
   RShift = auto()

@dataclass(frozen=True, slots=True)
class BinaryOperation:
   lhs: str
   rhs: str
   operator: Operator

@dataclass(frozen=True, slots=True)
class Negation:
   input: str

@dataclass(frozen=True, slots=True)
class Instruction:
   assigned: str
   assignment: Negation | BinaryOperation

def do_operation(x: int, y: int, operator: Operator) -> int:
   match operator:
      case Operator.And:
         return x & y
      case Operator.Or:
         return x | y
      case Operator.LShift:
         return x << y
      case Operator.RShift:
         return do_operation(x >> y, 2**16 - 1, Operator.And)

def value(symbol: str, instructions: dict) -> int:
   if symbol == 'x': return 123
   if symbol == 'y': return 456
   try:
      return int(symbol, 10)
   except:
      match instructions.get(symbol):
         case BinaryOperation(lhs, rhs, operator):
            return do_operation(value(lhs, instructions), value(rhs, instructions), operator)
         case Negation(symbol):
            return ~value(symbol, instructions)
         case None:
            print(f'Couldn\'t compute the value of {symbol}')
            return 0
            # raise Exception('This is obviously impossible')

def parse_operator(operator_str: str) -> Operator:
   operator_dict = {
      'AND': Operator.And,
      'OR': Operator.Or,
      'LSHIFT': Operator.LShift,
      'RSHIFT': Operator.RShift,
   }

   if res := operator_dict.get(operator_str):
      return res
   raise ValueError(f'Invalid operator: {operator_str}')

def parse_operation(operation_str: str) -> Negation | BinaryOperation:
   separated = operation_str.split()
   if len(separated) == 2:
      return Negation(separated[1])
   if len(separated) == 3:
      return BinaryOperation(
         lhs=separated[0],
         rhs=separated[2],
         operator=parse_operator(separated[1]),
      )
   raise ValueError(f'Bad operation: {operation_str}')

def parse_instruction(line: str) -> Instruction:
   assignment_str, assigned = line.split(' -> ')
   res = Instruction(
      assigned=assigned,
      assignment=parse_operation(assignment_str)
   )
   print(res)
   return res

if __name__ == '__main__':
   instructions = {}
   with open('07.in', 'r') as f:
      for line in f:
         inst = parse_instruction(line[:-1])
         instructions[inst.assigned] = inst.assignment
   print(f'Value of a: {value("a", instructions)}')
