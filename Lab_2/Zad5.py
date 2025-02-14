'''
System Dynamicznego Generowania Kodów Python (Metaprogramowanie)
Napisz narzędzie, które generuje dynamicznie kod w Pythonie na podstawie szablonów i danych
wejściowych, a następnie uruchamia ten kod. Narzędzie powinno:
• Przyjmować szablon kodu jako string (np. def funkcja(x): return x + 2).
• Uzupełniać szablon o brakujące fragmenty kodu (np. zmienne, funkcje) w czasie działania.
• Weryfikować poprawność generowanego kodu przed uruchomieniem.
Wskazówka: Wykorzystaj eval() i exec() w połączeniu z walidacją wejściową i generowaniem kodu z
szablonów.
'''

import ast
import re

def dynamic_code_generation(function_body, function_values):
    # Definicja szablonu funkcji z miejscami na parametry i ciało funkcji
    function_template = """
def dynamic_function({{ params }}):
    {{ body }}
"""
    function_code = function_template.replace("{{ body }}", function_body)
    
    pattern = r'(\w+)\s*='
    params_names = re.findall(pattern, function_values)
    params_without_values = ", ".join(params_names)
    
    function_code = function_code.replace("{{ params }}", params_without_values)
    
    try:
        ast.parse(function_code)
    except SyntaxError as e:
        raise ValueError(f'Podano złą funkcję lub jej wartości: {function_code} \n\n {function_values}') from e
    
    local_vars = {}
    exec(function_code, {}, local_vars)
    
    dynamic_function = local_vars.get('dynamic_function')
    
    if dynamic_function is None:
        raise ValueError('Nie udało się utworzyć funkcji dynamic_function.')
    
    return dynamic_function

    