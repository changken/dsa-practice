let Harry = {
  name: 'Harry Potter',
  age: 40,
  married: true,
  sayHi() {
    console.log(this.name + ' says hi!');
  },
};

console.log(Harry);
