import numpy as np
FUNCTION_MAP = {
    # Aggregate Functions
    "Count": "count",
    "Sum": "sum",
    "Min": "min",
    "Max": "max",
    "Avg": "mean",

    # Interval Functions
    "Interval": "not-implemented",
    "Width": "not-implemented",
    "Collapse": "not-implemented",
    "Expand": "not-implemented",

    # List Functions
    "Length": "len",
    "Head": "not-implemented",
    "Tail": "not-implemented",
    "Last": "not-implemented",
    "IndexOf": "not-implemented",
    "ElementAt": "not-implemented",
    "SubList": "not-implemented",
    "First": "not-implemented",
    "MinValue": "min",
    "MaxValue": "max",
    "Sort": "sort_values",
    "Exists": "not-implemented",
    "Times": "not-implemented",
    "Where": "not-implemented",

    # Logical Functions
    "Coalesce": "fillna",
    "IsNull": "isnull",
    "IfNull": "not-implemented",
    "IsTrue": "not-implemented",
    "IsFalse": "not-implemented",
    "Not": "~",
    "Case": "not-implemented",

    # Mathematical Functions
    "Abs": "abs",
    "Negate": "not-implemented",
    "Round": "round",
    "Floor": "floor",
    "Ceiling": "np.ceil",
    "Truncate": "not-implemented",
    "Exp": "np.exp",
    "Ln": "np.log",
    "Log": "np.log10",
    "Power": "pow",
    "Successor": "not-implemented",
    "Predecessor": "not-implemented",
    "Min": "min",
    "Max": "max",
    "ConformsTo": "not-implemented",

    # String Functions
    "Concatenate": "+",
    "Combine": "not-implemented",
    "Split": "str.split",
    "Length": "str.len",
    "Upper": "str.upper",
    "Lower": "str.lower",
    "Substring": "str.slice",
    "ReplaceMatches": "not-implemented",

    # Temporal Functions
    "DateTime": "pd.to_datetime",
    "Time": "pd.to_datetime",
    "Date": "pd.to_datetime",
    "Today": "pd.Timestamp.today",
    "Now": "pd.Timestamp.now",
    "SameOrBefore": "not-implemented",
    "SameOrAfter": "not-implemented",
    "SameAs": "not-implemented",
    "After": "not-implemented",
    "Before": "not-implemented",

    # Type Conversion Functions
    "ToBoolean": "astype(bool)",
    "ToConcept": "not-implemented",
    "ToDateTime": "pd.to_datetime",
    "ToDate": "pd.to_datetime",
    "ToDecimal": "astype(float)",
    "ToInteger": "astype(int)",
    "ToQuantity": "not-implemented",
    "ToRatio": "not-implemented",
    "ToTime": "pd.to_datetime",
    "ToString": "astype(str)",

    # Miscellaneous Functions
    "Message": "not-implemented",
    "PopulationStdDev": "std",
    "PopulationVariance":"var",
    "StdDev": "std",
    "Variance": "var",
    "AllTrue": "all",
    "AnyTrue": "any",

    # Clinical Request Functions
    "Retrieve": "not-implemented",
}

TYPE_MAP = {
    # CQL Type: Equivalent pandas dtype
    "Boolean": "bool",
    "Integer": "int64",
    "Decimal": "float64",
    "Quantity": "not-implemented",  # No direct equivalent in pandas
    "Ratio": "not-implemented",     # No direct equivalent in pandas
    "String": "object",             # pandas represents strings as object dtype
    "DateTime": "datetime64[ns]",   # Assuming DateTime in CQL is similar to Python's datetime
    "Date": "datetime64[ns]",       # Assuming Date in CQL is similar to Python's datetime.date
    "Time": "not-implemented",      # pandas lacks a dedicated Time type, could be represented as string or datetime
    "Concept": "not-implemented",   # No direct equivalent in pandas
    "List": "object",               # pandas can hold lists in series of object dtype
}

def convert_to_pandas_type(cql_type):
    pandas_type = TYPE_MAP.get(cql_type)

    if pandas_type == "not-implemented":
        raise NotImplementedError(f"Conversion for CQL type {cql_type} is not implemented.")
    else:
        return pandas_type
    
class CqlToPandasVisitor(CqlParserVisitor):
    def visitExpression(self, ctx):
        if ctx.getChildCount() == 1:
            # if this is a terminal node (no more children), just return its text
            return ctx.getText()
        else:
            # if this is a binary expression, process the left and right operands and the operator
            left = self.visit(ctx.getChild(0))
            operator = self.visit(ctx.getChild(1))
            right = self.visit(ctx.getChild(2))

            # map the CQL operator to the equivalent pandas operator
            operator_map = {
                'and': '&',
                'or': '|',
                '=': '==',
                '<>': '!=',
                # add more operator mappings as needed...
            }
            pandas_operator = operator_map.get(operator.lower(), operator)

            return f"({left} {pandas_operator} {right})"

    # ...

    def visitOperator(self, ctx):
        return ctx.getText()

    def visitFunctionInvocation(self, ctx):
        # Map CQL functions to pandas functions
        func_name = ctx.functionName().getText()
        if func_name in FUNCTION_MAP:
            pandas_func = FUNCTION_MAP[func_name]
            args = [self.visit(arg) for arg in ctx.argumentList().expression()]
            return f"{pandas_func}({', '.join(args)})"
        else:
            raise ValueError(f"Unsupported function: {func_name}")
        
    def convert_cql_parameters_to_pandas(func_name, *args):
        # Ensure the function name is in our map before we start
        if func_name not in FUNCTION_MAP:
            raise ValueError(f"Unknown function {func_name}")

        if func_name == "Substring":
            if len(args) != 3:
                raise ValueError("Substring function expects 3 arguments")

            string, start, length = args
            start -= 1
            stop = start + length

            return (string, start, stop)

        elif func_name in ["Count", "Sum", "Min", "Max", "Avg"]:
            if len(args) != 1:
                raise ValueError(f"{func_name} function expects 1 argument")

            return args

        elif func_name == "Concatenate":
            if len(args) < 2:
                raise ValueError("Concatenate function expects at least 2 arguments")

            return args

        elif func_name in ["ToBoolean", "ToInteger", "ToDecimal", "ToString", "ToDate", "ToDateTime"]:
            if len(args) != 1:
                raise ValueError(f"{func_name} function expects 1 argument")

            return args

        elif func_name in ["Now", "DateTime", "Time", "DateFrom", "TimeFrom", 
                        "YearFrom", "MonthFrom", "DayFrom", "HourFrom", 
                        "MinuteFrom", "SecondFrom", "MillisecondFrom"]:
            if len(args) != 1:
                raise ValueError(f"{func_name} function expects 1 argument")

            return args

        elif func_name in ["Abs", "Negate", "Add", "Subtract", "Multiply", "Divide", "Modulo", 
                        "Ceiling", "Floor", "Truncate", "Ln", "Log", "Exp", "Power", 
                        "Sqrt", "Length", "Round"]:
            return args

        elif func_name in ["List_Length", "List_Min", "List_Max", "List_Avg", "List_Sum", "List_AllTrue", "List_AnyTrue", "List_Count"]:
            if len(args) != 1:
                raise ValueError(f"{func_name} function expects 1 argument")

            return args

        elif func_name in ["Interval", "Width", "Start", "End", "Contains", "ProperContains", "In", 
                        "ProperIn", "Overlaps", "OverlapsBefore", "OverlapsAfter", "Meets", 
                        "MeetsBefore", "MeetsAfter"]:
            # These functions could take one or more arguments based on the operation
            return args

        else:
            raise NotImplementedError(f"Parameter conversion for function {func_name} is not implemented")

