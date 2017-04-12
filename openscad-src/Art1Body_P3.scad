////////////////////////////////////////////////////////////////////////////
// VARIABLE DESCRIPTION

part = "both"; // Art1Body_P3A or Art1Body_P3B or both

////////////////////////////////////////////////////////////////////////////
// RENDERS

print_part();
  
////////////////////////////////////////////////////////////////////////////
// MAIN MODULES

module cylinder_outer(height,radius,fn,cen) {
   fudge = 1/cos(180/fn);
   cylinder(h=height,r=radius*fudge,$fn=fn,center=cen);
}

// Module with the holes and cutouts
module Art1Body_P3() {
  difference() {
      rotate([-90,0,0])
        translate([0,0,-132.4])
          import("ART1BODY_P3.stl");
      for(i=[-1,1])
        translate([i*15,50,0]) {
          translate([0,0,5])
            cylinder(d=5.0,h=35,$fn=50);
          translate([0,0,-5])
            cylinder(d=2,h=80,$fn=50);
          translate([0,0,-5]) 
            cube([4.6,4.3+5,2.0],center=true);
        }
       translate([-57.3,0,0])
         cube([0.35,16,14],center=true);
       translate([57.5,0,0])
         cube([1.1,16,14],center=true); 
  }
}

// Module for splitting in part A
module Art1Body_P3A() {
  difference() {
    Art1Body_P3();
    translate([-70,0,-60])
      cube([140,60,60]);
  }
}

// Module for splitting in part B
module Art1Body_P3B() {
  difference() {
    Art1Body_P3();
    translate([-70,0,0])
      cube([140,60,60]);
  }
}

module print_part() {
  if (part == "Art1Body_P3A")
    render(convextity=1)
      Art1Body_P3A();
  else if (part == "Art1Body_P3B") {
    render(convextity=1)
      rotate([180,0,0])
        Art1Body_P3B();
  }
  else if (part == "both") {
    render(convextity=1) {
      translate([0,10,0])
        Art1Body_P3A();
      translate([0,-10,0])
        rotate([180,0,0])
          Art1Body_P3B();
    }
  }
  else
    text("Choose one of the three options: Art1Body_P3A, Art1Body_P3B, both",halign ="center");
}





  




