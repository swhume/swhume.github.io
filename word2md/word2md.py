from spire.doc import *
from spire.doc.common import *

def convert_document():
    # Create a Document object
    document = Document()

    # Load a Word file
    document.LoadFromFile("C:\\Users\\Administrator\\Desktop\\input.docx")

    # Save it as an MD file
    document.SaveToFile("output/ToMarkdown.md", FileFormat.Markdown)

    # Dispose resources
    document.Dispose()


