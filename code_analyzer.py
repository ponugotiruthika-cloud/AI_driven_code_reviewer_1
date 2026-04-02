"""
from code_parser import parse_code_to_tree 
from error_detector import   AIReviewer 
from ai_suggester import get_ai_suggestions


def analyze_code_pipeline(code):
    syntax_result = parse_code_to_tree(code)
    if not syntax_result["success"]:
        return syntax_result["error"]["message"]

    tree = syntax_result["tree"]

    errors = report_unused(tree)

    ai_suggestions= get_ai_suggestions(code)

    return f""" 
    #unused_variables = {errors["unused_variable"]}

#AI Suggestions:
#
# {ai_suggestions}
"""
"""
"""
import ast
from error_detector import AIReviewer   # ✅ import the class
from ai_suggester import get_ai_suggestions   # ✅ your AI suggestions module


def analyze_code_pipeline(code: str) -> str:
    try:
        # Parse code into AST
        tree = ast.parse(code)

        # Run AIReviewer to detect unused variables
        reviewer = AIReviewer()
        reviewer.visit(tree)
        reviewer.report_unused()   # prints unused items
        # Collect unused variables
        unused_vars = reviewer.defined - reviewer.used

        # Get AI suggestions
        ai_suggestions = get_ai_suggestions(code)

        # Return formatted report
        return f"""
"""
--- AI REVIEW REPORT ---
Unused Variables and imports:
{list(unused_vars) if unused_vars else "None 🎉"}

AI Suggestions:
{ai_suggestions}
"""
"""
    except SyntaxError as e:
        return f"❌ Syntax Error: {e}"
    except Exception as e:
        return f"⚠️ Unexpected Error: {e}"
    """
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
