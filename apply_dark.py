import re

filepath = r"c:\Users\tarus\OneDrive\Desktop\portfolio\index.html"
with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Add darkMode to config
text = text.replace('theme: {', "darkMode: 'class',\n            theme: {")

# 2. Body class
text = text.replace('<body class="bg-gray-50 text-slate-800 antialiased font-sans">', '<body class="bg-gray-50 text-slate-800 antialiased font-sans transition-colors duration-300 dark:bg-slate-900 dark:text-slate-100">')

# 3. Insert toggle button in nav
toggle_html = """                <div class="flex items-center">
                    <button id="theme-toggle" class="p-2 mr-2 text-slate-600 hover:text-primary-600 hover:bg-gray-100 rounded-md transition-colors dark:text-slate-300 dark:hover:bg-slate-800" aria-label="Toggle Dark Mode">
                        <i id="theme-toggle-icon" class='bx bx-moon text-2xl'></i>
                    </button>
                    <!-- Mobile Menu Button -->
                    <div class="-mr-2 flex md:hidden">"""

text = text.replace("""                <!-- Mobile Menu Button -->
                <div class="-mr-2 flex md:hidden">""", toggle_html)
text = text.replace("""                <!-- Mobile Menu Button -->""", "")

# Close the new div around mobile menu button
text = text.replace("""                    </button>
                </div>
            </div>""", """                    </button>
                </div>
                </div>
            </div>""")

# 4. Blanket class replacements for dark mode
# We will use regex to only match these classes as whole words within class="..." attributes.
# Let's do simple replaces but verify bounds.
def replace_class(html, target, replacement):
    return re.sub(r'(class="[^"]*?\b)' + re.escape(target) + r'(\b[^"]*?")', r'\1' + replacement + r'\2', html)

text = replace_class(text, 'bg-white/80', 'bg-white/80 dark:bg-slate-900/80')
text = replace_class(text, 'bg-white', 'bg-white dark:bg-slate-800')
text = replace_class(text, 'bg-gray-50', 'bg-gray-50 dark:bg-slate-900')
text = replace_class(text, 'text-slate-900', 'text-slate-900 dark:text-white')
text = replace_class(text, 'text-slate-800', 'text-slate-800 dark:text-slate-100')
text = replace_class(text, 'text-slate-700', 'text-slate-700 dark:text-slate-200')
text = replace_class(text, 'text-slate-600', 'text-slate-600 dark:text-slate-300')
text = replace_class(text, 'text-slate-500', 'text-slate-500 dark:text-slate-400')
text = replace_class(text, 'border-gray-100', 'border-gray-100 dark:border-slate-700')
text = replace_class(text, 'border-slate-200', 'border-slate-200 dark:border-slate-700')
text = replace_class(text, 'bg-slate-100', 'bg-slate-100 dark:bg-slate-700')
text = replace_class(text, 'bg-slate-50', 'bg-slate-50 dark:bg-slate-800/50')
text = replace_class(text, 'hover:bg-gray-100', 'hover:bg-gray-100 dark:hover:bg-slate-800')
text = replace_class(text, 'hover:bg-gray-50', 'hover:bg-gray-50 dark:hover:bg-slate-700')

with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)
print("Done index.html")
