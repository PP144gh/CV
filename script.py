import subprocess
import sys

def convert_md_to_latex(md_file_path, latex_file_path):
    # LaTeX commands to adjust heading sizes
    header_tex_commands = r"""
\usepackage{titlesec}
\titleformat*{\section}{\Large\bfseries}
\titleformat*{\subsection}{\large\bfseries}
\titleformat*{\subsubsection}{\normalsize\bfseries}
"""

    # Write the LaTeX commands to a temporary file
    with open('header.tex', 'w') as header_file:
        header_file.write(header_tex_commands)

    try:
        # Command to convert Markdown to LaTeX using pandoc with additional LaTeX settings
        command = [
            'pandoc', md_file_path, '-s', 
            '-o', latex_file_path,
            '-V', 'geometry:margin=1in',         # Adjusts the page margins
            '-V', 'urlcolor=blue',               # Sets the color of hyperlinks
            '--pdf-engine=xelatex',              # Use XeLaTeX to better handle modern fonts
            '-V', 'mainfont="Trebuchet MS"',     # Specifies a modern typeface
            '-V', 'fontsize=10pt',               # Sets the font size
            '--include-in-header=header.tex'     # Includes custom LaTeX commands for heading sizes
        ]
        
        # Execute the command
        subprocess.run(command, check=True)
        print(f'Successfully converted {md_file_path} to {latex_file_path}')
    except subprocess.CalledProcessError as e:
        print(f'An error occurred while converting: {e}', file=sys.stderr)
    except Exception as e:
        print(f'An unexpected error occurred: {e}', file=sys.stderr)

# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_md_to_latex.py input.md output.tex")
    else:
        input_md = sys.argv[1]
        output_tex = sys.argv[2]
        convert_md_to_latex(input_md, output_tex)
