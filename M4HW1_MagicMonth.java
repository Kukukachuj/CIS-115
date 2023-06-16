//James Moore
//M4HW1
//06/12/2023

import java.util.Scanner;
class Main {
  public static void main(String[] args) {
    Scanner keyboard = new Scanner(System.in);
        
        Integer month,day,year,total;
        
        System.out.println("Enter the Month");
        month = keyboard.nextInt();
        System.out.println("Enter Day");
        day = keyboard.nextInt();
        System.out.println("Enter 2 digit Year");
        year = keyboard.nextInt();
        total = month * day;
        
        if (total == year)
        {
            System.out.print("The date is magic");
        }
        else
        {
            System.out.print("The date is not magic");
        }
  }
}
