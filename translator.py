import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Traducteur de Langues")
        
        self.translator = Translator()

        self.create_widgets()

    def create_widgets(self):
        # Texte à traduire
        self.input_text = tk.Text(self.root, height=10, width=50)
        self.input_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Sélection de la langue de départ
        self.src_lang_label = ttk.Label(self.root, text="De:")
        self.src_lang_label.grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.src_lang = ttk.Combobox(self.root, values=list(LANGUAGES.values()))
        self.src_lang.grid(row=1, column=1, sticky='w', padx=5, pady=5)
        self.src_lang.set('english')  # Langue par défaut

        # Sélection de la langue de destination
        self.dest_lang_label = ttk.Label(self.root, text="À:")
        self.dest_lang_label.grid(row=2, column=0, sticky='e', padx=5, pady=5)
        self.dest_lang = ttk.Combobox(self.root, values=list(LANGUAGES.values()))
        self.dest_lang.grid(row=2, column=1, sticky='w', padx=5, pady=5)
        self.dest_lang.set('french')  # Langue par défaut

        # Bouton Traduire
        self.translate_button = ttk.Button(self.root, text="Traduire", command=self.translate_text)
        self.translate_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Texte traduit
        self.output_text = tk.Text(self.root, height=10, width=50)
        self.output_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def translate_text(self):
        src_text = self.input_text.get("1.0", tk.END).strip()
        src_lang = self.get_language_key(self.src_lang.get())
        dest_lang = self.get_language_key(self.dest_lang.get())
        
        if src_text:
            translated = self.translator.translate(src_text, src=src_lang, dest=dest_lang)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated.text)

    def get_language_key(self, lang_name):
        for key, value in LANGUAGES.items():
            if value == lang_name:
                return key
        return 'en'  # Default to English if not found
