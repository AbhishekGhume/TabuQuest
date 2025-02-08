import pandas as pd
import difflib
import re

class QueryExecutor:
    def __init__(self, df):
        self.df = df.copy()
        self.original_columns = df.columns.tolist()
        self.allowed_namespace = {
            'pd': pd,
            'df': self.df,
            'sum': sum,
            'mean': pd.Series.mean,
            'max': pd.Series.max,
            'min': pd.Series.min
        }

    def _get_closest_column(self, column_name):
        """Fuzzy match for column names"""
        matches = difflib.get_close_matches(
            column_name.lower(),
            [col.lower() for col in self.original_columns],
            n=1,
            cutoff=0.7
        )
        return self.original_columns[[col.lower() for col in self.original_columns].index(matches[0])] if matches else None

    def execute(self, code):
        """Enhanced execution with error handling"""
        try:
            self.allowed_namespace['result'] = None
            exec(code, {"__builtins__": {}}, self.allowed_namespace)
            result = self.allowed_namespace.get('result')
            
            if result is None:
                raise ValueError("No result variable created. Check your code syntax.")
                
            if isinstance(result, pd.core.generic.NDFrame):
                return result.reset_index() if hasattr(result, 'index') else result
                
            raise TypeError("Result must be a DataFrame or Series")
            
        except KeyError as e:
            missing_col = re.findall(r"'([^']*)'", str(e))[0]
            closest = self._get_closest_column(missing_col)
            if closest:
                raise RuntimeError(f"Column '{missing_col}' not found. Did you mean '{closest}'?")
            raise RuntimeError(f"Column '{missing_col}' not found. Available columns: {self.original_columns}")
            
        except Exception as e:
            raise RuntimeError(f"Execution error: {str(e)}")