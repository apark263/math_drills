from pylatex import Document, Section, Subsection, Command, Math, Alignat, MiniPage, LineBreak, VerticalSpace
from pylatex.utils import italic, NoEscape


def typeset_problems(filename, problems):
  geometry_options = {"margin": "0.5in"}
  doc = Document(font_size='large', geometry_options=geometry_options)
  doc.change_document_style("empty")
  doc.append(NoEscape(r'\noindent'))
  for i, (a, b) in enumerate(problems):
    with doc.create(MiniPage(width=r"0.33\textwidth")) as mp:
      with mp.create(Alignat(numbering=False, escape=False)) as agn:
        agn.append(f'{a} \\times {b}' + r'&= \rule{1.5cm}{0.15mm}')
    if (i % 3) == 2:
      doc.append(VerticalSpace("10pt"))
      doc.append(LineBreak())
  doc.generate_pdf(filename, clean_tex=True)


if __name__ == '__main__':
    problems = [(i, i+1) for i in range(25)]
    typeset_problems('minipage', problems)
