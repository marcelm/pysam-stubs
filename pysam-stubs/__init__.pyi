from typing import List

from pysam.libchtslib import *
from pysam.libcsamtools import *
from pysam.libcbcftools import *
from pysam.libcutils import *
import pysam.libcutils as libcutils
import pysam.libcfaidx as libcfaidx
from pysam.libcfaidx import *
import pysam.libctabix as libctabix
from pysam.libctabix import *
import pysam.libctabixproxies as libctabixproxies
from pysam.libctabixproxies import *
import pysam.libcsamfile as libcsamfile
from pysam.libcsamfile import *
import pysam.libcalignmentfile as libcalignmentfile
from pysam.libcalignmentfile import *
import pysam.libcalignedsegment as libcalignedsegment
from pysam.libcalignedsegment import *
import pysam.libcvcf as libcvcf
from pysam.libcvcf import *
import pysam.libcbcf as libcbcf
from pysam.libcbcf import *
import pysam.libcbgzf as libcbgzf
from pysam.libcbgzf import *
from pysam.utils import SamtoolsError
import pysam.Pileup as Pileup
from pysam.samtools import *
import pysam.config
from pysam.version import __version__, __samtools_version__

def get_include() -> List[str]: ...
def get_defines() -> List[str]: ...
def get_libraries() -> List[str]: ...
