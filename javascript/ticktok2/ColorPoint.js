class ColorPoint {
  constructor(start, movement, color){
    this.start = start;
    this.movement = movement;
    this.color = color;
  }
  draw(){
    stroke(...this.color)
    point(this.start+(variation*this.movement), count);
  }
}