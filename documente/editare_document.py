from docx import Document

document = Document('CONTRACT DE FORMARE PROFESIONALĂ.docx')

document_modificat = Document()
for element in document.element.body:
    document_modificat.element.body.append(element)

def scrie_in_document(document, model, inlocuire):
    f = open(document, 'r')
    for lines in f:
        if model in lines:
            output = model.replace ("X", inlocuire)
    return output


