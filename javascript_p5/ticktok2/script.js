var count = 0;
var variation = 0;
var direction = 1;
var stroke_color = 0;

function setup() {
    createCanvas(800,800);
    background(255)
    strokeWeight(15)
};

function draw() {
    variation += direction * 2
    
    if (Math.abs(variation) > 50){
      direction *=  -1
    }

    let red = [(250-stroke_color),0,0]
    let green = [0,(250-stroke_color),0]
    let blue = [0,0,(250-stroke_color)]
    let white_black = [stroke_color,stroke_color, stroke_color]

    let lines = [
      new ColorPoint(100,1,red),
      new ColorPoint(200,-1,green),
      new ColorPoint(300,1,blue),
      new ColorPoint(400,-1,white_black),
      new ColorPoint(500,1,blue),
      new ColorPoint(600,-1,green),
      new ColorPoint(700,1,red),
    ];
    lines.map(elm => elm.draw())
    
    count+=1
    if (count > 800){
      count = 0
      stroke_color += 25
      if (stroke_color > 250){
        stroke_color = 0
      }
    }
};