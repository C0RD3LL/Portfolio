
#code taken from https://bioperl.org/howtos/Local_Databases_HOWTO.html

use Bio::Index::Fastq;
use strict;

my $fastq_file = shift;
my $index_file = $fastq_file . ".index";

my $inx = Bio::Index::Fastq->new('-filename' => $index_file, '-write_flag' => 1);
$inx->make_index($fastq_file);
