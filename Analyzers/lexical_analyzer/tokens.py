from enum import Enum

class TokenType(Enum):
    #Reserved Words
    # Data Types
    FEINT = "Feint"       # Equivalent to int
    CHANT = "Chant"       # Equivalent to str
    FLOATER = "Floater"   # Equivalent to float
    STAT = "Stat"         # Equivalent to bool

    # Inout/Output Statements
    INBOUND = "Inbound"   # Equivalent to input
    ANNOUNCE = "Announce" # Equivalent to print

    # Control Statements
    DRIBBLE = "Dribble"   # Equivalent to if
    SHOOT = "Shoot"       # Equivalent to else
    PASS = "Pass"         # Equivalent to elif

    # Loop Statements
    FORWARD = "Forward"     # Equivalent to for
    PLAY = "Play"           # Equivalent to while
    TIMEOUT = "Timeout"     # Equivalent to break
    RESUME = "Resume"       # Equivalent to continue

    # Others/Functions
    REBOUND = "Rebound"   # Equivalent to return
    WIN = "Win"           # Equivalent to True
    LOSS = "Loss"         # Equivalent to False
    TEAM = "Team"         # Equivalent to Main
    DUNK = "Dunk"         # Equivalent to Void

    # Reserved Symbols
    # Assignment Operators
    ASSIGN = "="          # Assignment: Assigns a value to a variable
    ADD_ASSIGN = "+="     # Add and Assign: Adds and assigns the result to a variable
    SUB_ASSIGN = "-="     # Subtract and Assign: Subtracts and assigns the result to a variable
    MUL_ASSIGN = "*="     # Multiply and Assign: Multiplies and assigns the result to a variable
    DIV_ASSIGN = "/="     # Divide and Assign: Divides and assigns the result to a variable
    MOD_ASSIGN = "%="     # Modulus and Assign: Finds modulus and assigns the result to a variable

    # Arithmetic Operators
    ADD = "+"             # Addition: Adds two values together
    SUB = "-"             # Subtraction: Finds the difference between two values
    NEG = "!"
    MUL = "*"             # Multiplication: Multiplies two values
    DIV = "/"             # Division: Divides one value by another
    MOD = "%"             # Modulus: Finds the remainder after division

    # Relational Operators
    EQUAL = "=="          # Equal to: Checks if two values are equal
    NOT_EQUAL = "!="      # Not equal to: Checks if two values are not equal
    LESS_THAN = "<"       # Less than: Checks if one value is smaller than another
    GREATER_THAN = ">"    # Greater than: Checks if one value is larger than another
    LESS_EQUAL = "<="     # Less than or equal to: Checks if one value is smaller or equal to another
    GREATER_EQUAL = ">="  # Greater than or equal to: Checks if one value is larger or equal to another

    # Logical Operators
    AND_OP = "AND"        # Logical AND: Returns True if the value of both operands are True
    OR_OP = "OR"          # Logical OR: Returns True if at least one operand is True
    NOT_OP = "NOT"        # Logical NOT: Returns the opposite Boolean value of the operand

    # Other Operators
    CHANT_CONCAT = "&"         # Chant Concatenation: Concatenates Chant together when working with Chant data types
    ARRAY_INDEX_LEFT = "["     # Array Size/Index: Used to specify the size or index of an array
    ARRAY_INDEX_RIGHT = "]"    # Array Size/Index: Used to specify the size or index of an array
    CODE_BLOCK_LEFT = "{"      # Code Blocks: Used to define the start and end points of a programming structure
    CODE_BLOCK_RIGHT = "}"     # Code Blocks: Used to define the start and end points of a programming structure
    LEFT_PAREN = "("           # Grouping: Used to group values or expressions
    RIGHT_PAREN = ")"          # Grouping: Used to group values or expressions
    NEGATIVE = "~"             # Negative: Negates the numerical values, making positive negative and vice versa
    VAR_INIT = "@"             # Variable Initialization: Every identifier must start with an "@" sign
    SPACE = "space"            # Space: Used to separate tokens
    COMMA = ","                # Comma: Used to separate values in a list
    COLON = ":"                # Colon: Used to separate key-value pairs in a dictionary
    SEMICOLON = ";"            # Semicolon: Used to terminate statements
    COMMENT = "#"              # Comment: Used to add comments in the code
    MULTI_COMMENT = "||"       # Multi-line Comment: Used to add multi-line comments in the code
    TAB = "tab"                # Tab: Used to separate tokens
    NEWLINE = "\N"             # New Line: Used to separate tokens
    NEWLINE_TAB = "\T"         # New Line and Tab: Used to separate tokens
    DOT = "."                  # Dot: Used to access attributes or methods of an object
    UNDERSCORE = "_"           # Underscore: Used to separate words in identifiers
    BACKSLASH = "\\"           # Backslash: Used to escape special characters
    QUOTE = "\""               # Quote: Used to define string literals
    BACKSLASH_AND = "\&"
    BACKSLASH__AT = "\@"

class Token:
    """
    Represents a single token in the basketball-themed programming language.
    Each token consists of a type (from TokenType) and an optional value.
    """

    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        """
        Returns a readable string representation of the token.
        If the token has a value, it includes the value in the representation.
        """
        return f"Token({self.token_type}, {self.value})" if self.value else f"Token({self.token_type})"
