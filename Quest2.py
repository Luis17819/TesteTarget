def check_a(text):
    text_lower = text.lower()

    amount_a = text_lower.count('a')

    if amount_a > 0:
        return f"A letra 'a' aparece {amount_a} vezes na string."
    else:
        return "A letra 'a' não foi encontrada na string."
    
search_text = input("Informe uma string: ")

print(check_a(search_text))
