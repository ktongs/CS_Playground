class animal{
	constructor(legs,voice,name){
		this.legs = legs;
		this.voice = voice;
		this.name = name;
	}
	speak(voice){console.log("I go "+voice+"!")};
}

class mammal extends animal{
	constructor(legs,voice,name,status){
		super(legs,voice,name);
		this.status = status;
	}
	// this.status = status
}
fish = new animal(0,'woob','William')
dog = new mammal(4,'bark','Bobby','friend');

console.log(dog.name);
console.log(dog.status);
dog.speak(dog.voice);

fish.speak(fish.voice);
