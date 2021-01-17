from dna_features_viewer import BiopythonTranslator, CircularGraphicRecord
from Bio import SeqIO


def generate_map():
    record = SeqIO.read("Genome.gb", "genbank")
    graphic_record = BiopythonTranslator().translate_record(record, record_class=CircularGraphicRecord)
    graphic_record.labels_spacing = 20
    ax, _ = graphic_record.plot(figure_width=15, figure_height=15, draw_line=True)
    ax.figure.savefig("solution.jpg")


generate_map()
