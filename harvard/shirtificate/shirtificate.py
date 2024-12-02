"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/09/24'

# .User Story:
#: Suppose that you’d like to implement a CS50 “shirtificate,” a PDF with an image of an I took
#: CS50 t-shirt, shirtificate.png, customized with a user’s own name.
#:
#:


# .Original Requirements:
#: 1.- In a file called shirtificate.py, implement a program that prompts the user for their name
#:     and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to
#:     this one for John Harvard, with these specifications:
#:
#:      Sample shirt https://cs50.harvard.edu/python/2022/psets/8/shirtificate/jharvard.pdf
#:      Source Image https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png
#:      Package https://pypi.org/project/fpdf2/
#:
#: 2.- The requirements are:
#:
#:     2.1.- The orientation of the PDF should be Portrait.
#:     2.2.- The format of the PDF should be A4, which is 210mm wide by 297mm tall.
#:     2.3.- The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
#:     2.4.- The shirt’s image should be centered horizontally.
#:     2.5.- The user’s name should be on top of the shirt, in white text.
#:
#: 3.- All other details we leave to you. You’re even welcome to add borders, colors, and lines.
#:     Your shirtificate needn’t match John Harvard’s precisely. And no need to wrap long names
#:     across multiple lines.
#:
#: 4.- Before writing any code, do read through fpdf2’s tutorial to learn how to use it. Then skim
#:     fpdf2’s API (application programming interface) to see all of its functions and parameters
#:     therefor.
#:
#: 5.- No need to submit any PDFs with your code. But, if you would like, you’re welcome (but not
#:     expected) to share a shirtificate with your name on it in any of CS50’s communities!
#:
#:


# .Hints:
#: 1.- Note that fpdf2 comes with a class called FPDF, which has quite a few methods, per
#:     py-pdf.github.io/fpdf2/fpdf/#fpdf.FPDF. You can install it with:
#:
#:                      pip install fpdf2
#:
#: 2.- Note that you can extend FPDF and instantiate your own subclass thereof in order to add a
#:     header to every page of a PDF, per
#:     py-pdf.github.io/fpdf2/Tutorial.html#tuto-2-header-footer-page-break-and-image. Or you can
#:     add it as text yourself.
#:
#: 3.- Note that you can disable automatic page breaks, which might otherwise cause your PDF to
#:     overflow from one page to two, with set_auto_page_break, per
#:     py-pdf.github.io/fpdf2/Margins.html.
#:
#: 4.- Note that a cell’s height can be negative, to move it upward.
#:
#: 5.- You can open shirtificate.pdf, once outputted, by clicking it in VS Code’s file explorer.
#:
#:


# .Extra work requirements:
#: None defined
#:
#:


# .My pseudo code approach:
#: 1.- Install fpdf2
#:
#: 2.- Create a class that inherits from the PDF class and adds additional methods to the parent
#:     class which will be responsible for making the PDF.  Class should have the following
#:     capabilities:
#:
#:     2.1.- One instance variable that holds the location and name where the output file will be
#:           saved to.
#:     2.2.- One instance variable that holds the location and name where the source file is
#:     2.3.- One instance method that saves the output file with the parameters described above
#:     2.4.- One instance method that writes the title
#:     2.5.- One instance method that adds the shirt to the PDF
#:     2.6.- One instance method that enters the shirt message
#:
#: 3.- The initial approach is to test things outside of the class first, and then add to the class
#:     if I have trouble.
#:


from fpdf import FPDF


# | ***********************************************************************************************
# | **********************           C L A S S    S E C T I O N            ************************
# | ***********************************************************************************************

class CS50Shirt(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.source_file_name = str()
        self.source_file_loc = str()
        self.student_name = str()
        self.pdf_file_name = str()
        self.pdf_file_loc = str()
        self.pdf_page_title = str()

    @property
    def student_name(self):
        return self._student_name

    @student_name.setter
    def student_name(self, name):
        self._student_name = name

    @property
    def pdf_page_title(self):
        return self._pdf_page_title

    @pdf_page_title.setter
    def pdf_page_title(self, title):
        self._pdf_page_title = title

    def src_file_info(self, name, loc):
        self.src_file_name = name
        self.src_file_loc = loc
        self.src_and_file = loc + name

    def tgt_file_info(self, name, loc):
        self.tgt_file_name = name
        self.tgt_file_loc = loc
        self.tgt_and_file = loc + name

    def output(self):
        super().output(self.tgt_and_file)

    def add_image(self):
        super().image(self.src_and_file, x=int((210-190)/2), y=50, w=190, keep_aspect_ratio=True)

# | ***********************************************************************************************
# | **********************    M A I N    P R O G R A M    S E C T I O N    ************************
# | ***********************************************************************************************


def main():
    # > This is an inline code comment.
    # > This is an inline code comment.

    # > pdf = FPDF()
    # > pdf.add_page()
    # > pdf.set_font('helvetica', size=12)
    # > pdf.cell(text="hello world")
    # >pdf.output("hello_world.pdf")

    # > Instantiate the name of the local object.
    my_shirt = CS50Shirt()
    my_shirt.student_name = input('Name: ').strip()

    print(f'The source file name is [{my_shirt.source_file_name}]')
    print(f'The source file location is {my_shirt.source_file_loc}')
    print(f'The student\'s name is [{my_shirt.student_name}]')
    print('=' * 100)
    print()

    # > Now lets load the source file name and location
    src_loc = ''
    src_name = 'shirtificate.png'
    my_shirt.src_file_info(src_name, src_loc)
    print(f'The source file name and location is [{my_shirt.src_and_file}]')

    # > Now set the target file information
    tgt_loc = ''
    tgt_name = 'shirtificate.pdf'
    my_shirt.tgt_file_info(tgt_name, tgt_loc)
    my_shirt.pdf_page_title = 'CS50 Shirtificate'
    print(f'The target file name and location is [{my_shirt.tgt_and_file}]')
    print(f'The target file title text is [{my_shirt.pdf_page_title}]')
    print('=' * 100)
    print()

    # > Now let's get the page sized, orientation and settings.  The The format
    # > of the PDF should be A4, which is 210mm wide by 297mm tall.
    my_shirt.add_page()
    my_shirt.set_page_background((255, 255, 255))
    my_shirt.set_font("helvetica", size=40)
    my_shirt.cell(w=210, h=9, text=my_shirt.pdf_page_title, border=0,
                  new_x="LMARGIN", new_y="NEXT", align='C', fill=False)
    my_shirt.add_image()
    my_shirt.set_font("helvetica", size=25, style='B')
    my_shirt.set_text_color(255, 255, 255)
    my_shirt.cell(w=190, h=200, text=f'{my_shirt.student_name} took CS50', border=0,
                  new_x="LMARGIN", new_y="NEXT", align='C', fill=False)
    my_shirt.output()


#
#
#
# | ***********************************************************************************************
# | **************************    F U N C T I O N     S E C T I O N    ****************************
# | ***********************************************************************************************
#
#
#
#
# | ***********************************************************************************************
# | **********************           C A L L   S E L F   M A I N           ************************
# | ***********************************************************************************************
# > Call main ONLY when intended
if __name__ == '__main__':
    main()
