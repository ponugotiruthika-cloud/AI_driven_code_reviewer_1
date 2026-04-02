 
import ast
from error_detector import AIReviewer
from ai_suggester import get_ai_suggestions

def analyze_code_pipeline(code: str) -> dict:
    try:
        tree = ast.parse(code)
        reviewer = AIReviewer()
        reviewer.visit(tree)

        unused_vars, unused_imports = reviewer.report_unused()

        # Build corrected code by removing unused items
        corrected_lines = []
        for line in code.splitlines():
            if any(imp in line for imp in unused_imports):
                continue
            if any(var in line for var in unused_vars):
                continue
            corrected_lines.append(line)
        corrected_code = "\n".join(corrected_lines)

        ai_suggestions = get_ai_suggestions(code)

        return {
            "report": "--- AI REVIEW REPORT ---",
            "unused_vars": f"Unused Variables: {list(unused_vars) if unused_vars else 'None 🎉'}",
            "unused_imports": f"Unused Imports: {list(unused_imports) if unused_imports else 'None 🎉'}",
            "suggestions": ai_suggestions,
            "original_code": code,
            "corrected_code": corrected_code,
        }
    except SyntaxError as e:
        return {"error": f"❌ Syntax Error: {e}"}
    except Exception as e:
        return {"error": f"⚠️ Unexpected Error: {e}"}
