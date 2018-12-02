const fs = require('fs');

class ChronoCalibrator {
  constructor() {
    this.currentFrequency = 0;
    this.visitedFrequencies = { 0: 1 };
    this.timesCalibrated = 0;
  }

  calibrateFrequency(calibrateBy) {
    const old = this.currentFrequency;
    this.currentFrequency += calibrateBy;
    // console.log('Calibrated (old: %d, diff: %d, new: %d)', old, calibrateBy, this.currentFrequency);

    const visitedTimes = (this.visitedFrequencies[this.currentFrequency] != null) ?
      this.visitedFrequencies[this.currentFrequency] : 0;

    this.visitedFrequencies[this.currentFrequency] = visitedTimes + 1;
    this.timesCalibrated += 1;
    // console.log('visited ' + visitedTimes);
    // update the visited values with true/false if visited
    if(this.visitedFrequencies[this.currentFrequency] === 2) {
      return true;
    }

    return false;
  }

  calibrateFromArray(calibrationArr) {
    let calibrated = false;
    // kept a counter so that I was for sure not in an infinite loop (started from 10 -> 100 -> 1000)
    let times = 0;
    const totalLen = calibrationArr.length;
    while(!calibrated && times < 1000) {
      // console.time('ChronoCalibrator - Single Iteration (' + (times + 1) + ')');
      for(let i = 0; i < totalLen; i += 1) {
        calibrated = this.calibrateFrequency(calibrationArr[i]);
        if(calibrated) {
          // console.log('done!');
          break;
        }
      }
      // console.timeEnd('ChronoCalibrator - Single Iteration (' + (times + 1) + ')');
      times += 1;
    }
  }

  getFrequency() {
    return this.currentFrequency;
  }

  getTimesCalibrated() {
    return this.timesCalibrated;
  }

  isCorrectFrequency() {
    return this.visitedFrequencies[this.currentFrequency] === 2;
  }
}

function start() {
  const inputPath = './d1p1.in';
  const myChron = new ChronoCalibrator();
  console.time('ChronoCalibrator - Parse file');
  let parsedInput = fs.readFileSync(inputPath).toString().split("\n").map((value) => {
    return isNaN(parseInt(value)) ? 0 : parseInt(value);
  });
  parsedInput = parsedInput.slice(0, parsedInput.length - 1);
  console.timeEnd('ChronoCalibrator - Parse file');
  // console.log(parsedInput.length);

  console.time('ChronoCalibrator - Iterations');
  myChron.calibrateFromArray(parsedInput);
  console.timeEnd('ChronoCalibrator - Iterations');
  console.log(myChron.getFrequency());
  console.log('Frequency is correct: ', myChron.isCorrectFrequency());
  console.log('Required', myChron.getTimesCalibrated(), 'calibrations.');

}

console.time('ChronoCalibrator');
start();
console.timeEnd('ChronoCalibrator')
