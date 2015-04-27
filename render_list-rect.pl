#!/usr/bin/perl -w

# used to generate tiles of multiple zooms
use strict;

if( @ARGV < 7 ) {
    print <<EOF;
usage: render_list-rect.pl <zref> <x0> <x1> <y0> <y1> <z0> <z1> [ ... ]
Runs render_list with command-line options appropriate for rendering a
rectangular region in a range of zoom levels.  The region is given by <x0>,
<x1>, <y0> and <y1>, which are tile indices in zoom level <zref>.  The range of
zoom levels to render is <z0> to <z1>.  Both the rectagle and the zoom range
includes end points.  Any surplus arguments that may follow are passed through
to render_list.
EOF
    exit;
}

for (@ARGV[0..6]) {
    die "The first seven arguments have to be non-negative integers."
        unless /^\d+$/;
}

my ($zref, $x0, $x1, $y0, $y1, $z0, $z1, @rlargs)= @ARGV;

if( $x0 > $x1 ) {
    my $tmp= $x1;
    $x1= $x0;
    $x0= $tmp;
}

if( $y0 > $y1 ) {
    my $tmp= $y1;
    $y1= $y0;
    $y0= $tmp;
}

if( $z0 > $z1 ) {
    my $tmp= $z1;
    $z1= $z0;
    $z0= $tmp;
}

my $refmax= (1 << $zref) - 1;

die "X range $x0 .. $x1 out of range 0 .. $refmax."
    unless $x0 <= $refmax;

die "Y range $y0 .. $y1 out of range 0 .. $refmax."
    unless $y0 <= $refmax;

die "Zoom range out of range 0..18."
    unless $z0 <= 18;

if( $x1 > $refmax ) {
    print "Warning: x1 = $x1 out of range 0 .. $refmax.  Reduced to $refmax.\n";
    $x1= $refmax;
}

if( $y1 > $refmax ) {
    print "Warning: y1 = $y1 out of range 0 .. $refmax.  Reduced to $refmax.\n";
    $y1= $refmax;
}

if( $z1 > 18 ) {
    print "Warning: z1 = $z1 out of range 0 .. 18.  Reduced to 18.\n";
    $z1= 18;
}

for my $z ($z0..$z1) {
    my ($x, $X, $y, $Y);
    if( $z > $zref ) {
        my $mul= 1 << ($z - $zref);
        $x= $x0 * $mul;
        $X= $x1 * $mul + $mul - 1;
        $y= $y0 * $mul;
        $Y= $y1 * $mul + $mul - 1;
    }
    elsif( $z < $zref ) {
        my $div= 1 << ($zref - $z);
        $x= $x0 / $div;
        $X= $x1 / $div;
        $y= $y0 / $div;
        $Y= $y1 / $div;
    }
    else {
        ($x, $X, $y, $Y)= ($x0, $x1, $y0, $y1);
    }
    system "render_list", "-z", $z, "-Z", $z, "-a", "-x", $x, "-X", $X, "-y", $y, "-Y", $Y, @rlargs;
}


