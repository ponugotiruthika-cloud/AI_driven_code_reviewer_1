"""
import reflex as rx
# Import your existing logic from your other files
from code_analyzer import analyze_code_pipeline
from ai_suggester import get_ai_suggestions

class AnalyzeState(rx.State):
    user_code: str = ""
    corrected_code: str = ""
    ai_suggestions: str = "Suggestions will appear here after analysis..."
    unused_vars: str = ""
    unused_imports: str = ""
    is_loading: bool = False
    user_question: str = ""
    chat_answer: str = ""
    is_chatting: bool = False

    #def set_user_question(self, value: str):
        #self.user_question = value
    
    async def ask_assistant(self):
        if not self.chat_question.strip():
            return
        
        self.is_chatting = True
        yield

        query = f"The user has this code:\n{self.user_code}\n\nQuestion: {self.user_question}"
        self.chat_answer = get_ai_suggestions(query)
        
        self.is_chatting = False
    
    async def process_code(self):
        if not self.user_code.strip():
            return
        
        self.is_loading = True
        yield # This tells Reflex to update the UI (show a spinner if you add one)

        # Call YOUR existing pipeline from code_analyzer.py
        results = analyze_code_pipeline(self.user_code)

        if "error" in results:
            self.ai_suggestions = results["error"]
            self.corrected_code = ""
        else:
            self.corrected_code = results["corrected_code"]
            self.ai_suggestions = results["suggestions"]
            self.unused_vars = results["unused_vars"]
            self.unused_imports = results["unused_imports"]
        
        self.is_loading = False

    def set_user_code(self, val):
        self.user_code = val
       """
import datetime
import reflex as rx
import sys
import os

# This line ensures Python can find code_analyzer.py in your main folder
sys.path.append(os.getcwd())

try:
    from code_analyzer import analyze_code_pipeline
    from ai_suggester import get_ai_suggestions
except ImportError:
    # Fallback so the app doesn't crash on startup
    def analyze_code_pipeline(code): return {"error": "Module not found"}
    def get_ai_suggestions(code): return "Error: AI module not found."

class AnalyzeState(rx.State):
    user_code: str = ""
    corrected_code: str = ""
    ai_suggestions: str = "Suggestions will appear here..."
    unused_vars: str = ""
    unused_imports: str = ""
    is_loading: bool = False
    
    user_question: str = ""
    chat_answer: str = ""
    is_chatting: bool = False

    show_about: bool = False
    show_contact: bool = False
    history: list[dict] = []

    def toggle_about(self):
        self.show_about = not self.show_about

    def toggle_contact(self):
        self.show_contact = not self.show_contact

    async def process_code(self):
        if not self.user_code.strip():
            return
        
        self.is_loading = True
        yield 

        try:
            # Call your background logic
            results = analyze_code_pipeline(self.user_code)

            if not results or "error" in results:
                self.ai_suggestions = results.get("error", "Error in analysis.")
            else:
                self.corrected_code = results.get("corrected_code", "")
                self.ai_suggestions = results.get("suggestions", "")
                self.unused_vars = results.get("unused_vars", "None")
                self.unused_imports = results.get("unused_imports", "None")

                # --- UPDATED: Save to History using standard datetime ---
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                self.history.append({
                    "timestamp": now, 
                    "original": self.user_code[:50] + "...", 
                    "suggestions": self.ai_suggestions[:100]
                })
        except Exception as e:
            self.ai_suggestions = f"Logic Error: {str(e)}"
        
        self.is_loading = False

    def clear_history(self):
        self.history = []

    async def ask_assistant(self):
        if not self.user_question.strip(): return
        self.is_chatting = True
        yield
        try:
            query = f"Code:\n{self.user_code}\n\nQuestion: {self.user_question}"
            self.chat_answer = get_ai_suggestions(query)
        except Exception as e:
            self.chat_answer = f"Assistant Error: {str(e)}"
        self.is_chatting = False

    def set_user_code(self, val: str): self.user_code = val
    def set_user_question(self, val: str): self.user_question = val