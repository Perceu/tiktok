let sketch = function(p5) {
  let [width,height] = [800,800]
  class Drop {
    constructor(){
      [this.x,this.y] = [p5.random(width), p5.random(-200, -100)];
      [this.speed, this.size] = [p5.random(4,8),p5.random(4,8)]
    }
    drop(){
      let val = (this.y > height) ? p5.random(-200, -100) : (this.y+this.speed)
      this.y = val
    }
    draw(){
      p5.stroke(255);
      p5.line(this.x, this.y, this.x, this.y+this.size);
      this.drop();
    }
  }
  p5.setup = function() {
    p5.createCanvas(width,height );
    this.drops = new Array(2000).fill(undefined).map(() => new Drop());
  };
  p5.draw = function() {
    p5.background(0);
    this.drops.forEach(elm => elm.draw());
  };
};
let myp5 = new p5(sketch);