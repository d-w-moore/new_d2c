#!/usr/bin/perl

use Sys::Hostname;
use FindBin qw($RealBin);

$hostname = hostname();

$slurmdConfig = `slurmd -C`;

$node = (($slurmdConfig=~/NodeName=\S+/) ? "NodeName|" : "");

$slurmdConfig =~ s[(^| )(${node}ClusterName|Boards|TmpDisk|RealMemory|UpTime)=\S*][]gm;
$slurmdConfig =~ s[\n][\040]gs;

@template_files = <$RealBin/slurm.conf.*template>;

if (@template_files == 1) {
    die  "cannot open template file\n" unless open(my $tmp, "<", $template_files[0]);
    local $/=undef;
    $src =  <$tmp>;
    $src =~ s/<SLURMD-CONFIG-OUTPUT>/$slurmdConfig/es;
    $src =~ s/<YOUR-HOST-NAME>/$hostname/esg;
    print "$src";
}
else { print STDERR "please specify source template file to use"; }
