#!/usr/bin/perl

use strict;
use warnings;
use v5.28;
use Getopt::Long qw(GetOptions);
use File::Copy;
use Data::Dumper;


#provide the location in command line
my $loc;
GetOptions('loc=s' => \$loc) or die "Usage: $0 --loc <location>\n";
chomp $loc;

if($loc){
  say "The script will be ran againt the following folder: $loc";
}


sub create_folder_struct {
  our $base_folder_name = $loc . '/' . 'HWIO_IF';
  our $hwio = $base_folder_name . '/' . 'HWIO_IF_SPECIFIC';
  our $vios = $hwio . '/' . 'VIOS_IF';

  unless ( -e $base_folder_name and -d $base_folder_name ){
    mkdir($base_folder_name, 700);
    mkdir($hwio, 700);
    mkdir($vios, 700);
  }
  for ( $hwio, $vios){
    unless( -e $_ and -d $_ ){
      mkdir( $_, 700);
    }
  }
}


sub move_files {
  opendir(my $gh, $loc) or die "Cannot open dir: $loc\n";
  my @hwio_files = grep { /hwio/g && -f } readdir($gh);
  close $gh;

  my %hwio;
  my $temp_d;
  for my $i (@hwio_files){
    if ( $i =~ /hwio\w(\d+)/g) {
      my @temp = grep { /hwio\w$1/} @hwio_files;
      push @{ $hwio{"hwio_$1"} }, @temp;
      @hwio_files = grep { ! /hwio\w$1/ } @hwio_files
    }
  }
  print Dumper(\%hwio);
}


move_files;
