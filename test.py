from convert import Convert
from maw import Analysis

if __name__ == '__main__':
    convert = Convert()
    maw = Analysis()
    print(convert.get_convert_to_list(text="Жена принца"))
    print(maw.morphological_analysis_text_and_converter("Жена принца"))
