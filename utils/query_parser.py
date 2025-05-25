import google.generativeai as genai
import os
from dotenv import load_dotenv
import re

load_dotenv()

class QueryParser:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.safety_settings = [
            {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_NONE"},
        ]
        
    def _sanitize_code(self, code):
        """Enhanced code sanitization"""
        forbidden_patterns = [
            r"os\.", r"subprocess\.", r"shutil\.", r"sys\.", r"__import__",
            r"eval\(", r"exec\(", r"pickle\.", r"open\(", r"lambda.*:"
        ]
        for pattern in forbidden_patterns:
            if re.search(pattern, code):
                raise ValueError(f"Dangerous pattern detected: {pattern}")
        return code

    def parse_query(self, query, columns):
        """Enhanced prompt with column awareness"""
        try:
            model = genai.GenerativeModel('models/gemini-1.5-flash-latest', safety_settings=self.safety_settings)
            columns_list = ", ".join([f"'{col}'" for col in columns])
            
            prompt = f"""Convert this query to pandas code. Follow strictly:
- Use dataframe 'df'
- Available columns: {columns_list}
- Assign final result to 'result' variable
- Use EXACT column names from the list
- Handle spaces in column names with df['column name']
- Return ONLY code, no explanations
- Never use unmentioned columns

Example:
Query: Show sales over 100 in California
Code:
result = df[(df['Sales'] > 100) & (df['State'] == 'California')]

Query: {query}
Code:"""
            
            response = model.generate_content(prompt)
            code = response.text.strip().replace("```python", "").replace("```", "")
            return self._sanitize_code(code)
            
        except Exception as e:
            raise RuntimeError(f"Query parsing failed: {str(e)}")