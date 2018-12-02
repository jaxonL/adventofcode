import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;

public class ChronoCalibration {
  int currentFrequency = 0;

  public void calibrateFrequency(int calibrate) {
    currentFrequency += calibrate;
  }

  public void calibrateFromArray(ArrayList<Integer> calibrationArr) {
    for(int value : calibrationArr) {
      System.out.printf("Adding %n to current freq (%n).", value, this.currentFrequency);
      this.calibrateFrequency(value);
      System.out.printf("New freq: %n.", this.currentFrequency);
    }

    System.out.println("Current frequency is " + this.currentFrequency);
  }

  public void printCurrentFrequency() {
    System.out.println(this.currentFrequency);
  }

  public static void main(String[] args) {
    try {
      File in = new File("d1p1.in");
      Scanner scanner = new Scanner(in);
      ArrayList<Integer> calibrationValues = new ArrayList<Integer>();
      ChronoCalibration calibrator = new ChronoCalibration();

      while(scanner.hasNextInt()) {
        calibrationValues.add(scanner.nextInt());
      }
      calibrator.calibrateFromArray(calibrationValues);
    } catch (FileNotFoundException e) {
      System.out.println(e);
      System.exit(1);
    }

  }
}
