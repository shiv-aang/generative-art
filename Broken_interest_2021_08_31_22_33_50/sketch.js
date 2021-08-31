let img;
let cnv;
function preload(){
  img = loadImage('assets/walk.jpg');
}

function setup() {
  cnv= createCanvas(img.width, img.height);
  let newCanvasX= (windowWidth - img.width)/2;
  let newCanvasY=(windowWidth -img.width)/2;
  cnv.position(newCanvasX, newCanvasY);
  for(let col= 0; col<img.width; col+=10){
    for(let row=0;row<img.height; row+=10){
      let xPos= col;
      let yPos= row;
      let zPos= col;
      let c = img.get(xPos, yPos,);
      push();
      translate(xPos, yPos, zPos);
      rotate(radians(random(120)))
      //noFill();
      fill(color(c));
      stroke(0);
      //stroke(color(c));
      strokeWeight(random(15))
      point(xPos, yPos,zPos);
      strokeWeight(random(5));
      //quad(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, [detailX], [detailY])

      quad(xPos, yPos, zPos, xPos*random(5), yPos*random(2), zPos*random(3), yPos*random(5), yPos*random(4), zPos*random(5), xPos*random(2), yPos*random(3), xPos*random(4));
      //triangle(x1, y1, x2, y2, x3, y3)
      //triangle(xPos,yPos, xPos*random(5), yPos*random(3), xPos*random(3), yPos*random(10));
      
      //curve(xPos, yPos, sin(xPos) * random(60), cos(xPos)*sin(yPos)*random(50), random(10), 0,cos(yPos)*sin(xPos)*random(140), cos(xPos)*sin(yPos)*50);
      pop();
    }
  }
}
