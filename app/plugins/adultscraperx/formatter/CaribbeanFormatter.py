from app.plugins.adultscraperx.formatter.basicFormatter import BasicFormater


class CaribbeanFormatter(BasicFormater):

    def format(code):
        code = code.replace('-',' ')
        code = code.replace('_',' ')
        if code[-4] != "-":
            if code[-4] == " ":
                return code.replace(" ", "-")
        return code