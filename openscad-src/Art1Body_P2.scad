
////////////////////////////////////////////////////////////////////////////
// AUXILIARY MODULES
module cylinder_outer(height,radius,fn,cen) {
   fudge = 1/cos(180/fn);
   cylinder(h=height,r=radius*fudge,$fn=fn,center=cen);
}

////////////////////////////////////////////////////////////////////////////
// RENDERS

print_part();


////////////////////////////////////////////////////////////////////////////
// MAIN MODULES
module Art1Body_P2() {
  difference() {
    import("ART1BODY_P2.stl",convexity=0.5);
    for(i=[-1,1]) {
      translate([i*55.5,-0.5,89.5]) {
        cylinder_outer(height = 20,radius = 1.6,fn = 8,cen=true);
        cube([25,5.8,2.7],center=true);
      }
    }
  }
}

module print_part() {
  render(convextity=1)
    translate([0,0,-25])
      Art1Body_P2();
}