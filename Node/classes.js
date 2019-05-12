const readline = require('readline');

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

r1 = readline.createInterface({
	input:process.stdin,
	output:process.stdout
});

r1.question("Enter fish voice: ",(answer)=>{
	fish.voice = answer;
	fish.speak(fish.voice);
})
fish.speak(fish.voice);
