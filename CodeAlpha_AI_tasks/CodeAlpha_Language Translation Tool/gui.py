import tkinter as tk
from tkinter import ttk, messagebox
from translator import translate_text

# Available languages with their codes
LANGUAGES = {
    "Arabic": "ar",
    "English": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Chinese": "zh-cn"
}

def run_gui():
    # Main window
    root = tk.Tk()
    root.title("Language Translation Tool")
    root.geometry("500x400")
    root.resizable(False, False)

    # Input text label and box
    tk.Label(root, text="Enter text to translate:").pack(pady=5)
    input_text = tk.Text(root, height=5, width=50)
    input_text.pack()

    # Frame for language selection
    frame = tk.Frame(root)
    frame.pack(pady=10)

    # Source language dropdown
    tk.Label(frame, text="Source Language:").grid(row=0, column=0, padx=5)
    src_combo = ttk.Combobox(frame, values=list(LANGUAGES.keys()))
    src_combo.current(1)  # Default to English
    src_combo.grid(row=0, column=1)

    # Target language dropdown
    tk.Label(frame, text="Target Language:").grid(row=1, column=0, padx=5)
    dest_combo = ttk.Combobox(frame, values=list(LANGUAGES.keys()))
    dest_combo.current(0)  # Default to Arabic
    dest_combo.grid(row=1, column=1)

    # Result label and output text box
    result_label = tk.Label(root, text="Translated text:")
    result_label.pack(pady=5)
    output_text = tk.Text(root, height=5, width=50)
    output_text.pack()

    # Function to handle translation on button click
    def translate_action():
        text = input_text.get("1.0", tk.END).strip()  # Get text from input box
        if not text:
            messagebox.showerror("Error", "Please enter text to translate")
            return
        src_lang = LANGUAGES[src_combo.get()]  # Get selected source language code
        dest_lang = LANGUAGES[dest_combo.get()]  # Get selected target language code
        translated = translate_text(text, src_lang, dest_lang)  # Translate
        output_text.delete("1.0", tk.END)  # Clear previous output
        output_text.insert(tk.END, translated)  # Insert translated text

    # Translate button
    tk.Button(root, text="Translate", command=translate_action).pack(pady=10)

    root.mainloop()
