// James Moore
// M4HW2
// 6-15-2023
// A Time calculator that converts seconds into minutes, hours, or days.

import java.util.Scanner;
  
class Main {
  public static void main(final String[] args) {
    final Scanner keyboard = new Scanner(System.in);
    int sec, seconds, minutes, hours, days;
    System.out.print("Enter the number of seconds you want to convert  ");
    sec = keyboard.nextInt();
    if (sec >= 0  && sec < 60){
      seconds = sec % 60;
      System.out.println("Seconds: " + seconds);
    }
    else if (sec >= 60 && sec < 3600){
    
      minutes = sec / 60;
      seconds = sec % 60;
      System.out.println("Minutes: " + minutes);
      System.out.println("Seconds: " + seconds);
     } 
    else if (sec >= 3600 && sec < 86400){
      hours = sec / 3600;
      minutes = (sec % 3600) / 60;
      seconds = (sec % 3600) % 60;
      System.out.println("Hours: " + hours);
      System.out.println("Minutes: " + minutes);
      System.out.println("Seconds: " + seconds);
     } 
    else if (sec >= 86400) {
      days = sec / 86400;
      hours = (sec % 86400) / 3600;
      minutes = ((sec % 86400) % 3600) / 60;
      seconds = ((sec % 86400) % 3600) % 60;
      System.out.println("Days: " + days);
      System.out.println("Hours: " + hours);
      System.out.println("Minutes: " +  minutes);
      System.out.println("Seconds: " + seconds);
    }
  }
}
