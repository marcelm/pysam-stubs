from pysam.libchtslib import *
from pysam.libcsamtools import *
from pysam.libcbcftools import *
from pysam.libcutils import *
from pysam.libcfaidx import *
from pysam.libctabix import *
from pysam.libctabixproxies import *
from pysam.libcsamfile import *
from pysam.libcalignmentfile import *
from pysam.libcalignedsegment import *
from pysam.libcvcf import *
from pysam.libcbcf import *
from pysam.libcbgzf import *
from pysam.utils import SamtoolsError
from pysam.samtools import *
from pysam.version import __version__, __samtools_version__

def get_include() -> List[str]: ...
def get_defines() -> List[str]: ...
def get_libraries() -> List[str]: ...
